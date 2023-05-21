# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["platformName"] = "android"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(5)
el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Clock")
el1.click()
el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Cities")
el2.click()

el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Search")
el3.click()
el4 = driver.find_element(by=AppiumBy.ID, value="com.android.deskclock:id/search_src_text")
el4.send_keys("beijing")
el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Beijing")
el5.click()
el6 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
el6.click()

driver.quit()