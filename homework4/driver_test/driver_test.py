import time

from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://ceshiren.com")

time.sleep(4.0)

driver.quit()