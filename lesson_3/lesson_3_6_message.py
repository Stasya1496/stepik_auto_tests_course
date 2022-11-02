import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math




@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1'])
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    element = browser.find_element(By.TAG_NAME, "textarea")
    element.send_keys(math.log(int(time.time())))
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    message = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
    assert message == 'Correct!', f"Get massage: {message}"


