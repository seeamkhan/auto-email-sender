import unittest, time
from basetestcase import BaseTestCase
from testcases import Login
from testcases import Switch_Organization


class RunTestCases(BaseTestCase):
    def test_login(self):
        Login(self.driver).login_as_admin()
    def test_switch_organization(self):
        Switch_Organization(self.driver).switch_organization()

        time.sleep(3)
if __name__ == '__main__':
    unittest.main(verbosity=2)