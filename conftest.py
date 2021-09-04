import pytest
import logging

from selenium import webdriver

logging.basicConfig(level=logging.INFO, filename="logs/logger.log",
                    format='%(asctime)s %(levelname)s %(filename)s %(message)s')


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

    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")

    logger = logging.getLogger('BrowserLogger')
    test_name = request.node.name

    logger.info(f"-----> Test '{test_name}' started -----")

    if executor == "local":
        caps = {'goog:chromeOptions': {}}

        driver = webdriver.Chrome(desired_capabilities=caps)

    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        caps = {
            "browserName": browser,
            "browserVersion": version,
            "screenResolution": "1280x720",
            "name": "opencart",
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": videos,
                "enableLog": logs
            },
            'acceptSslCerts': True,
            'acceptInsecureCerts': True,
            'timeZone': 'Europe/Moscow',
            'goog:chromeOptions': {}
        }

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )

    def open(path=""):
        logger.info(f"Open url '{url}{path}'")
        return driver.get(url + path)

    driver.open = open
    driver.open()

    driver.maximize_window()

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver


@pytest.fixture
def user():
    return "user", "bitnami"
