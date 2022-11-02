import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def test_add_to_caard_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(5)
    #element = browser.find_element(By.CLASS_NAME, "btn-add-to-basket").is_displayed()
    assert browser.find_element(By.CLASS_NAME, "btn-add-to-basket").is_displayed(), f"There isn't button add to basket"
