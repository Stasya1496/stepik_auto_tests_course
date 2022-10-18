from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/cats.html'
browser = webdriver.Chrome()

try:
    browser.find_element(By.ID, "button")


finally:
    browser.quit()