from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from base import BasePage
from elements import LoginPageCommonElements, AdminHomepageElements
from selenium.webdriver.common.action_chains import ActionChains


class Login(BasePage):
    def __init__(self, driver):
        super(Login, self).__init__(driver)
        self.com_elem = LoginPageCommonElements(self.driver)


    def login_as_admin(self):
        do = self.com_elem
        # print self.com_elem.username + '\n' + self.com_elem.password
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.com_elem._login_email_field)))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.com_elem._login_pass_field)))
        do.login_email.clear()
        do.login_email.send_keys(do.username)
        do.login_pass.clear()
        do.login_pass.send_keys(do.password)
        do.login_button.click()
        print 'Login Test Pass!'


class Switch_Organization(BasePage):
    def __init__(self, driver):
        super(Switch_Organization, self).__init__(driver)
        self.com_elem = AdminHomepageElements(self.driver)

    def switch_organization(self):
        do = self.com_elem
        # WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.ID, do.admin_top_menu)))
        # do.admin_top_menu.click()
        # time.sleep(10)
        self.driver.find_element_by_xpath(self.com_elem._admin_top_menu).click()
        # ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.com_elem._sw_org_hover))
        # self.driver.find_element_by_xpath(self.com_elem._sw_org_more_button).click()
        print "Switch Organization Pass!"