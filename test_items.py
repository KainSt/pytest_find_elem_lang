import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


def test_page_has_btn_add_to_basket(browser, language):
    browser.get(link)
    time.sleep(3)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(language)
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, "#language_selector > button").click()
    time.sleep(3)
    assert browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"), "Element 'Basket button not found'"
    time.sleep(3)


