from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from __builtin__ import classmethod
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import unittest, time, re
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import Conf_Reader


def email_sender():
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
    driver.find_element_by_id('Passwd').send_keys('test1111')

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

    # to_field = "//textarea[contains(@id, ':nr')]"
    # to_field = "//textarea"
    to_field = ".//*[@id=':nk']"
    subject_field = ".//*[@id=':n4']"
    body_field = ".//*[@id=':oa']"
    send_button = ".//*[@id=':mu']"

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, to_field))
        )
    except:
        print 'To field not found, maybe composer box load failed!'

    # Enter data into to field
    for i in xrange(4):
        try:
            driver.find_element_by_xpath(to_field).clear()
            break
        except:
            print "Unknown Browse Server button."
    # driver.find_elements_by_id(to_field).clear()
    driver.find_element_by_xpath(to_field).send_keys('jacksparrow010203@gmail.com')
    driver.find_element_by_xpath(subject_field).clear()
    driver.find_element_by_xpath(subject_field).send_keys('Test automated email')
    driver.find_element_by_xpath(body_field).clear()
    driver.find_element_by_xpath(body_field).send_keys('Body of the automated test email')
    driver.find_element_by_xpath(send_button).click()


    time.sleep(5)
    driver.quit()

email_sender()