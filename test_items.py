from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def test_btn_available(browser):
    
    link=" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    assert browser.find_element(By.XPATH,'//button[@class="btn btn-lg btn-primary btn-add-to-basket"]').is_enabled()