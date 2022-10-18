from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x_value = browser.find_element(By.ID, "input_value")
    y = calc(x_value.text)
    input_place = browser.find_element(By.CLASS_NAME, 'form-control')
    input_place.send_keys(y)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true)", button)
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()
    button.click()

finally:
    time.sleep(10)
    browser.quit()
