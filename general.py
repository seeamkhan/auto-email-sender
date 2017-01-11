# coding: utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support import expected_conditions as EC


def write_error_log(Error):
    """
Error parameter should contains the string of the error message when the file could not open.
    :param Error:
    """
    target = open("Error_log.txt", 'a')
    target.write(Error)
    target.close()


def sinp_checker():
    print 'SINP site is checking'
    # driver = webdriver.Chrome()
    driver = webdriver.PhantomJS()
    # driver.maximize_window()
    sinp_url = 'https://www.saskatchewan.ca/residents/moving-to-saskatchewan/immigrating-to-saskatchewan/saskatchewan-immigrant-nominee-program/maximum-number-of-sinp-applications'
    # sinp_url = 'http://google.com/'
    driver.get(sinp_url)

    oid_close_msg = ".//*[contains(text(), 'The International Skilled Worker – Occupations In-Demand sub-category is closed to applications at this time.')]"
    express_close_msg = ".//*[contains(text(), 'International Skilled Worker – Saskatchewan Express Entry sub-category is closed to applications at this time.')]"

    oid_is_open = False
    express_entry_is_open = False
    sinp_is_open = False

    try:
        driver.find_element_by_xpath(oid_close_msg)
        print 'Checking OID close message'
    except:
        print "Alert! OID is not Closed, may be it's OPEN"
        oid_is_open = True
        print "OID status: %r" % oid_is_open

    try:
        driver.find_element_by_xpath(express_close_msg)
        print 'Checking Express Entry close message.'
    except:
        print "Alert! SINP Express Entry is not Closed, may be it's OPEN"
        express_entry_is_open = True
        print "OID status: %r" % express_entry_is_open

    if oid_is_open is True or express_entry_is_open is True:
        sinp_is_open = True
    time.sleep(1)
    driver.save_screenshot("SINP-screen.png")
    driver.quit()
    return sinp_is_open



def email_sender(status):
    if status is True:
        print 'The automated email is sending, please wait...'
        # driver = webdriver.Chrome()
        driver = webdriver.PhantomJS()
        # driver.maximize_window()
        base_url = 'https://gmail.com/'
        driver.get(base_url)

        # enter email
        driver.find_element_by_id('Email').clear()
        driver.find_element_by_id('Email').send_keys('jacksparrow010203')

        # click next
        driver.find_element_by_id('next').click()
        time.sleep(2)

        # enter password
        driver.find_element_by_id('Passwd').clear()
        driver.find_element_by_id('Passwd').send_keys('')

        # click login
        driver.find_element_by_id('signIn').click()

        # verify inbox present
        basic_compose_link = ".//*[@accesskey='c']"
        # basic_compose_link = "//a[contains(text(), 'Compose Mail')]"
        new_compose_link = "//div[contains(text(), 'COMPOSE')]"
        final_compose_link = "html/body/table[3]/tbody/tr/td[1]/table[1]/tbody/tr[1]/td/b/a"

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, basic_compose_link))
            )
            final_compose_link = basic_compose_link
        except:
            print 'Basic Compose button not found, maybe login failed!'

            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, new_compose_link))
                )
                final_compose_link = new_compose_link
            except:
                print 'Compose button not found, maybe login failed!'

        # driver.save_screenshot('screen.png')  # save a screenshot to disk

        # Click Compose button
        driver.find_element_by_xpath(final_compose_link).click()

        # verify composer box appears
        to_field = ".//*[@id='to']"
        cc_field = ".//*[@id='cc']"
        subject_field = ".//*[@name='subject']"
        body_field = ".//*[@name='body']"
        send_button = ".//*[@value='Send']"
        sent_confirmation = ".//*[contains(text(), 'Your message has been sent.')]"

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, to_field))
            )
        except:
            print 'To field not found, maybe composer box load failed!'

        driver.find_element_by_xpath(to_field).clear()
        driver.find_element_by_xpath(to_field).send_keys('jacksparrow010203@gmail.com; zafi005@gmail.com')
        driver.find_element_by_xpath(subject_field).clear()
        driver.find_element_by_xpath(subject_field).send_keys('SINP IS OPEN')
        driver.find_element_by_xpath(body_field).clear()
        driver.find_element_by_xpath(body_field).send_keys(
            'This is an automated alert email for Seeam and Saathi to notify that SINP has been opened. Good Luck!')

        try:
            all_send_buttons = driver.find_elements_by_xpath(send_button)
            all_send_buttons[0].click()
        except:
            print 'Send button was not clicked'

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, sent_confirmation)))
        # except NoSuchElementException, e:
        #     selenium_error = str(e)
        #     error_msg = "%s. \nPlease check the file name and try again.\n" % selenium_error
        #     write_error_log(error_msg)
        except:
            print 'Email sent failed!'

        time.sleep(1)
        driver.save_screenshot('Email-screenshoot.png')  # save a screenshot to disk
        driver.quit()
    else:
        print 'Sorry, SINP is still Close.'
    print 'Email Job completed.'

status = sinp_checker()
email_sender(status)
raw_input("\nPress enter to exit...")
