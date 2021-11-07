import pytest
import logging

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions

logging.basicConfig(
    level=logging.INFO, filename=Path("logger.log").resolve(),
    format='%(asctime)s %(levelname)s %(filename)s %(message)s'
)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera"])
    parser.addoption("--url", action="store", default="https://demo.opencart.com/", help="This is default url")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")

    parser.addoption("--executor", action="store", default="192.168.0.107")
    parser.addoption("--bversion", action="store", default="92.0")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")

    logger = logging.getLogger('BrowserLogger')
    test_name = request.node.name

    logger.info(f"-----> Test '{test_name}' started -----")

    driver = None

    if executor == "local":
        caps = {'goog:chromeOptions': {}}

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                options.headless = True
            driver = webdriver.Chrome(options=options, desired_capabilities=caps)
        if browser == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.headless = True
            driver = webdriver.Firefox(options=options, desired_capabilities=caps)
        if browser == "opera":
            options = OperaOptions()
            if headless:
                options.headless = True
            driver = webdriver.Opera(options=options, desired_capabilities=caps)

        if maximized:
            driver.maximize_window()

    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        caps = {
            "browserName": browser,
            "browserVersion": version,
            "screenResolution": "1280x720",
            "name": "opencart",
            "selenoid:options": {
                "sessionTimeout": "60s",
                "enableVNC": vnc,
                "enableVideo": videos,
                "enableLog": logs
            },
            'acceptSslCerts': True,
            'acceptInsecureCerts': True,
            'timeZone': 'Europe/Moscow',
            'goog:chromeOptions': {}
        }

        logger.info(f"Browser {browser} started remote on {executor_url}. "
                    f"Browser caps: {caps}")

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )

        driver.maximize_window()

    def open(path=""):
        logger.info(f"Open url '{url}{path}'")
        return driver.get(url + path)

    driver.open = open
    driver.open()

    def fin():
        logger.info(f"-----> Test '{test_name}' finished -----")
        driver.quit()

    request.addfinalizer(fin)
    return driver


@pytest.fixture
def user():
    return "user", "bitnami"
