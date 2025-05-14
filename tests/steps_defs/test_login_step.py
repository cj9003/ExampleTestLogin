from pytest_bdd import given, when, then, scenarios, parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


URL = "https://practicetestautomation.com/practice-test-login/"

scenarios("login.feature")

    
@given('Open the login page', target_fixture="browser") 
def browser():
    driver = webdriver.Chrome()  # Initialize the WebDriver (e.g., Chrome)
    driver.get(URL)
    # Wait for the page to load 
    driver.implicitly_wait(10)
    yield driver
    driver.quit()  # Ensure the browser is closed after the test
    

#when steps

@when(parsers.parse('I enter {user} and {passw}'))
def valid_credentials(browser, user, passw):
    browser.find_element(By.ID, "username").send_keys(user)
    browser.find_element(By.ID, "password").send_keys(passw)
    browser.find_element(By.ID, "submit").click()
    browser.implicitly_wait(10)

#then steps

@then('I should be redirected to the dashboard')
def logged(browser):
    if browser.current_url == "https://practicetestautomation.com/practice-test-login/":
       assert browser.find_element(By.ID, "error").is_displayed()
    else:
        assert browser.current_url == "https://practicetestautomation.com/logged-in-successfully/", "wrong credentials"



    