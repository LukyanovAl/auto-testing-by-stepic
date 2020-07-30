import pytest
import time
import math
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('numbers', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, numbers):
    browser.implicitly_wait(8)
    link = f"https://stepik.org/lesson/{numbers}/step/1"
    browser.get(link)
    #browser.find_element_by_css_selector("#login_link")
    time.sleep(2)
    input1 = browser.find_element_by_css_selector(".textarea")
    #time.sleep(2)
    input1.send_keys(str(math.log(int(time.time()))))

    #time.sleep(1)
    button1 = browser.find_element_by_class_name("submit-submission") 
    button1.click()
    time.sleep(1)
    message = browser.find_element_by_css_selector(".smart-hints__hint")
    time.sleep(1)
    print(message.text)
    assert "Correct!" == message.text ,  "Everything ok!"
    
