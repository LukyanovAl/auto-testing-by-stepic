import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_items_catalogue_link(browser):
    browser.get(link)
    time.sleep(10)
    button = len(browser.find_elements_by_css_selector("button"))
    assert button > 0, '!!!There is NO Basket Button!!!'
    
