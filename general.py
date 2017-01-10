from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support import expected_conditions as EC


def email_sender():
    print 'The automated email is sending, please wait...'
    driver = webdriver.Chrome()
    driver.maximize_window()
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
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'COMPOSE')]"))
        )
    except:
        print 'Compose button not found, maybe login failed!'

    # Click Compose button
    driver.find_element_by_xpath("//div[contains(text(), 'COMPOSE')]").click()

    # verify composer box appears

    to_field = ".//*[@id=':nk']"
    subject_field = ".//*[@id=':n4']"
    body_field = ".//*[@id=':oa']"
    send_button = ".//*[@id=':mu']"
    sent_confirmation = ".//*[@id='link_vsm']"

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, to_field))
        )
    except:
        print 'To field not found, maybe composer box load failed!'

    # Enter data into to field
    # for i in xrange(4):
    #     try:
    #
    #         break
    #     except:
    #         print "Unknown Browse Server button."
    driver.find_element_by_xpath(to_field).clear()
    driver.find_element_by_xpath(to_field).send_keys('jacksparrow010203@gmail.com; zafi005@gmail.com')
    driver.find_element_by_xpath(subject_field).clear()
    driver.find_element_by_xpath(subject_field).send_keys('SINP IS OPEN')
    driver.find_element_by_xpath(body_field).clear()
    driver.find_element_by_xpath(body_field).send_keys('This is an automated alert email for Seeam and Saathi to notify that SINP has been opened. Good Luck!')

    time.sleep(5)
    quit()
    driver.find_element_by_xpath(send_button).click()
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, sent_confirmation)))
    except:
        print 'Email sent failed!'

    time.sleep(5)
    driver.quit()



email_sender()
raw_input("Automated email has been sent.\nPress enter to exit...")