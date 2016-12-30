import unittest
import HTMLTestRunner
import os
from testrunner import RunTestCases

# get the directory path to output report file
dir = os.getcwd()

# get all tests from SearchProductTest and HomePageTest class
run_all_tests = unittest.TestLoader().loadTestsFromTestCase(RunTestCases)

# Create test suite:
smoke_test = unittest.TestSuite(run_all_tests)

# open the report file
outfile = open(dir + "\SmokeTestReport.html", "w")

# run the suite
# unittest.TextTestRunner(verbosity=2).run(smoke_test)

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Test Report', description='Smoke Tests')

# run the suite using HTMLTestRunner
runner.run(smoke_test)