from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestRegistration(unittest.TestCase):
    def test_reg_1(self):
        browser = webdriver.Chrome()
        try:
            link = "http://suninjuly.github.io/registration1.html"
            # link = "http://suninjuly.github.io/registration2.html"
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
            input3.send_keys("Smolensk")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be "
                                                                                                 "successfully "
                                                                                                 "registred")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            # time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_reg_2(self):
        browser = webdriver.Chrome()
        try:
            # link = "http://suninjuly.github.io/registration1.html"
            link = "http://suninjuly.github.io/registration2.html"
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
            input3.send_keys("Smolensk")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be "
                                                                                                 "successfully "
                                                                                                 "registred")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            # time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()
