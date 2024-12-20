import selenium
from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
def test_if_button(browser):
    browser.get(link)
    time.sleep(10)
    assert browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')