from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x, y):
    return str(int(x) + int(y))


browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser.get(link)
    x_value = browser.find_element(By.ID, "num1")
    y_value = browser.find_element(By.ID, "num2")
    x_value = x_value.text
    y_value = y_value.text
    result = calc(x_value, y_value)
   # roster = Select(browser.find_element(By.ID, 'dropdown'))
    roster = Select(browser.find_element(By.TAG_NAME, 'select'))
    roster.select_by_value(result)
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
