
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from time import sleep
import random

#Loading Chromedriver
driver = webdriver.Chrome()

# Navigate to LinkedIn login page
driver.get("https://www.linkedin.com/login")
sleep(5)

# Log in to LinkedIn
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

# Enter your LinkedIn credentials here
username.send_keys("your email")
password.send_keys("your password")
password.send_keys(Keys.RETURN)

