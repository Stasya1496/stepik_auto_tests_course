from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    browser.find_element(By.TAG_NAME, 'button').click()
    # confirm = browser.switch_to.alert
    # confirm.accept()
    new_window_name = browser.window_handles[1]
    browser.switch_to.window(new_window_name)
    result = calc(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.CLASS_NAME, 'form-control').send_keys(result)
    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(10)
    browser.quit()

