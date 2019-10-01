import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    #time.sleep(30)
    assert len(browser.find_elements_by_class_name("btn-add-to-basket")) == 1, "Unable to locate element or selector is not unique"
