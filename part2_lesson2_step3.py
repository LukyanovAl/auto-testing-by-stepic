from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

def summa(x, y):
  return str(int(x)+int(y))

#link = "http://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_css_selector("#num1")
    x = x_element.text
    y_element = browser.find_element_by_css_selector("#num2")
    y = y_element.text
    z = summa(x, y)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)

    button = browser.find_element_by_xpath("//button[text()='Submit']") 
    button.click()

finally:
    # успеваем скопировать код 
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла