class BasePage(object):
    """All page objects inherit from this."""

    def __init__(self, driver):
        self.driver = driver