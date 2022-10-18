from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.implicitly_wait(5)

try:
    browser.get(link)
    button = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button.click()
    result = calc(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.CLASS_NAME, 'form-control').send_keys(result)
    browser.find_element(By.ID, 'solve').click()
    button.get_attribute()

finally:
    time.sleep(10)
    browser.quit()

