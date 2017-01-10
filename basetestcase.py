import unittest
from __builtin__ import classmethod
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    """
Here we want to share the single Chrome instance for all the test cases in the general.py file.
For this we are using setUpClass(), teardDownClass() and @classmethod decorator.
These methods allow us to initialize values at the class level instead of the method level and then
share these values between the test methods.

That means, we could use setUp() and tearDown() but in that case every time a new Chrome instance would create to run
each def in the general.py file.
    """
    @classmethod
    def setUpClass(cls):
        # Create new Chrome session
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

        # Navigate to SMDS Login page
        login_url = 'https://gmail.com/'
        cls.driver.get(login_url)

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()