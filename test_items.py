#import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button_for_add_product(browser):
    browser.get(link)
    #time.sleep(30)
    el = browser.find_elements_by_xpath("//form[@id='add_to_basket_form']/button[@type='submit']")
    assert len(el) > 0, "Button was not found for some reason!"