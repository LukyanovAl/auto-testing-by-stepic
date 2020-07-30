import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", 
    	             help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en', 
    	             help="Choose language: ru, en, ... (etc.)")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if (browser_name == "chrome"):
        print("\nStart chrome browser for test...")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        yield browser
        print("\nquit browser..")
        browser.quit()
    elif (browser_name == "firefox"):
        print("\nStart firefox browser for test...")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        yield browser
        print("\nquit browser..")
        browser.quit()
    else:
        print("Browser {} still is not implemented".format(browser_name))
        yield browser
        print("\nQuit browser...")
        browser.quit()

