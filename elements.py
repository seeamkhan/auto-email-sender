from selenium.webdriver.support.ui import WebDriverWait
from basetestcase import BaseTestCase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import Conf_Reader
import os, time
from base import BasePage

class LoginPageCommonElements(BasePage):
    def __init__(self, driver):
        super(LoginPageCommonElements, self).__init__(driver)
        # Get username and password from the credential file
        credentials_file = os.path.join(os.path.dirname(__file__), 'login.credentials')
        self.username = Conf_Reader.get_value(credentials_file, 'LOGIN_USER')
        self.password = Conf_Reader.get_value(credentials_file, 'LOGIN_PASSWORD')

        # Page elements
        self._login_email_field = 'PrimaryEmail'
        self._login_pass_field = 'Password'
        self._login_button = 'Submit'

        # Selenium Actions for elements
        self.login_email = self.driver.find_element_by_id(self._login_email_field)
        self.login_pass = self.driver.find_element_by_id(self._login_pass_field)
        self.login_button = self.driver.find_element_by_id(self._login_button)


class AdminHomepageElements(BasePage):
    def __init__(self, driver):
        super(AdminHomepageElements, self).__init__(driver)

        # Admin Homepage elements
        self._admin_top_menu = "//li[contains(@class, 'subnav-carot')]/a/b"
        self._sw_org_hover = "//a[contains(text(), 'Switch Organization')]"
        self._sw_org_more_button = "//a[contains(@onclick, 'javascript:SwitchOrg()')]"

        # Selenium Actions for elements
        self.admin_top_menu = self.driver.find_element_by_xpath(self._admin_top_menu)