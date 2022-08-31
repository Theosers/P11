from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

url_root = 'http://127.0.0.1:5000/'
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


def test_End2End():
    driver.get(url_root)

    time.sleep(3)
    email_form = driver.find_element(By.ID, 'email')
    email_form.clear()
    time.sleep(1)
    email_form.send_keys("john@simplylift.co")
    time.sleep(1)
    button = driver.find_element(By.ID, "button")
    time.sleep(1)
    button.click()
    time.sleep(1)

    comp = driver.find_element(By.ID, "bookbutton")
    time.sleep(1)
    comp.click()
    time.sleep(1)

    form = driver.find_element(By.ID, "spots")
    form.clear()
    form.send_keys(1)
    time.sleep(1)
    button_book = driver.find_element(By.ID, "submitbutton")
    button_book.click()
    time.sleep(2)

    assert driver.find_element(By.CLASS_NAME, 'message')


test_End2End()
