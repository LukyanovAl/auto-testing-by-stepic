from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    button1 = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button1 = browser.find_element_by_xpath("//button[text()='Book']")
    button1.click()

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    
    button2 = browser.find_element_by_xpath("//button[text()='Submit']") 
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
    button2.click()

    

finally:
    # успеваем скопировать код 
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла