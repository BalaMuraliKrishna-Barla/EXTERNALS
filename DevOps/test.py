from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
path = "http://127.0.0.1:5000"
driver.get(path)


time.sleep(2)


driver.find_element(By.ID, "name").send_keys("Test User")
driver.find_element(By.ID, "email").send_keys("test@example.com")
driver.find_element(By.ID, "password").send_keys("strongpass")
driver.find_element(By.ID, "confirm-password").send_keys("strongpass")
driver.find_element(By.ID, "submit-btn").click()

time.sleep(1)

msg = driver.find_element(By.ID, "msg").text
print("Result:", msg)

driver.quit()
