import os
import pytest
import logging

from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions

logging.basicConfig(level=logging.INFO, filename="logs/logger.log")


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera"])
    parser.addoption("--url", action="store", default="https://demo.opencart.com/", help="This is default url")


@pytest.fixture
def browser(request):
    current_browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")
    logger = logging.getLogger('BrowserLogger')
    test_name = request.node.name

    driver = None

    logger.info(f"====> Test {test_name} started ====")

    if current_browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = True
        driver = webdriver.Chrome(options=options)
    if current_browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(options=options)
    if current_browser == "opera":
        options = OperaOptions()
        if headless:
            options.headless = True
        driver = webdriver.Opera(options=options)

    if maximized:
        driver.maximize_window()

    logger.info(f"Browser {current_browser} started with {driver.desired_capabilities}")

    def open(path=""):
        logger.info(f"Open url {url}{path}")
        return driver.get(url + path)

    driver.open = open
    driver.open()

    def finalization():
        driver.quit()
        logger.info(f"===> Test {test_name} finished")

    request.addfinalizer(finalization)

    return driver


@pytest.fixture
def user():
    return "user", "bitnami"
