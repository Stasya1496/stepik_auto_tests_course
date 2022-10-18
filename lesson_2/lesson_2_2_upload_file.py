from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
try:

    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Smolensk")
    file_name = os.path.join(os.path.abspath(os.path.dirname(__file__)), "new.txt")
    file_uploader = browser.find_element(By.ID, 'file')
    file_uploader.send_keys(file_name)
   # input4 = browser.find_element(By.ID, "country")
   # input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



