from selenium import webdriver
from selenium.webdriver.common.by import By

# open the swag labs test site
driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")

assert "Swag Labs" in driver.title

# Click on the Login button
login_btn = driver.find_element(By.ID, "login-button")
login_btn.click()

# wait for element to be found
driver.implicitly_wait(10)

# Find the username and password fields
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")

# Enter username and password
username.send_keys("standard_user")
password.send_keys("secret_sauce")

# submit the login form
login_btn.click()
driver.implicitly_wait(10)

burger_btn = driver.find_element(By.ID, "react-burger-menu-btn")
burger_btn.click()

logout_btn = driver.find_element(By.ID, "logout_sidebar_link")
assert logout_btn.is_displayed()
#logout_btn.click()

driver.close() 