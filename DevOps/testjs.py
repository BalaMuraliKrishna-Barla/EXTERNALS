from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
path = "http://127.0.0.1:5500/add.html" 
driver.get(path)  

driver.find_element(By.ID, "num1").send_keys("10")
driver.find_element(By.ID, "num2").send_keys("15")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(6)
driver.quit()