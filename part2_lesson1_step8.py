from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_valuex = browser.find_element_by_id("treasure")
    x_element = x_valuex.get_attribute("valuex")
    x = x_element
    y = calc(x)

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()

    button = browser.find_element_by_css_selector(".btn-default") 
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла