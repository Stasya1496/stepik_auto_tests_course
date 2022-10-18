from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)
    x_value = browser.find_element(By.ID, "treasure")
    x_value = x_value.get_attribute('valuex')
    #x_int = x_value.text
    y = calc(x_value)
    input_place = browser.find_element(By.ID, 'answer')
    input_place.send_keys(y)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
