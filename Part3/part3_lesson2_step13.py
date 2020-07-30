from selenium import webdriver
import time
import unittest


class test_link(unittest.TestCase):
    def test_link1(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("input:required.first")
        input1.send_keys("My Req")
        input2 = browser.find_element_by_css_selector("input:required.second")
        input2.send_keys("My Req")
        input3 = browser.find_element_by_css_selector("input:required.third")
        input3.send_keys("My Req")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться:
        time.sleep(1) # ждем загрузки страницы

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "You are registered")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(6)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_link2(self):
        link = "http://suninjuly.github.io/registration2.html" #Тест должен падать с ошибкой NoSuchElementException
        browser = webdriver.Chrome()
        browser.get(link)

        # Код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("input:required.first")
        input1.send_keys("My Req")
        input2 = browser.find_element_by_css_selector("input:required.second")
        input2.send_keys("My Req")
        input3 = browser.find_element_by_css_selector("input:required.third")
        input3.send_keys("My Req")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться:
        time.sleep(1) # ждем загрузки страницы

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "You are registered")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(6)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()   
# Оставляем пустую строку в конце файла