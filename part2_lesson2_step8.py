from selenium import webdriver
import time 
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    #browser.maximize_window()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("first")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("last")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("mymail")
    
    with open("test_2_2_8.txt", "w") as file:
        content = file.write("test1 for part 228")  # create test.txt file

    current_dir = os.path.abspath(os.path.dirname(" "))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, "test_2_2_8.txt")           # добавляем к этому пути имя файла 
    
    input4 = browser.find_element_by_name("file")
    input4.send_keys(file_path)

    button = browser.find_element_by_xpath("//button[text()='Submit']") 
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла