import logging


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.logger = logging.getLogger(type(self).__name__)
