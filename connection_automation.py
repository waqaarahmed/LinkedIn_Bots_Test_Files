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

# Waiting for the page to load
sleep(random.uniform(2, 5))


driver.get("https://www.linkedin.com/search/results/people/?keywords=Abdullah&origin=SWITCH_SEARCH_VERTICAL&sid=wYS")


sleep(random.uniform(2, 5))


try:
    connect_button = WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'artdeco-button--secondary') and span[text()='Connect']]"))
    )
    
    driver.execute_script("arguments[0].scrollIntoView(true);", connect_button)
    sleep(2)  
    try:
        connect_button.click()
        print("Clicked on the Connect button")
    except ElementClickInterceptedException:
        print("Element was blocked. Trying to click again after scrolling.")
        driver.execute_script("window.scrollBy(0, -300);")
        sleep(2)
        connect_button.click()
        print("Clicked on the Connect button after adjusting view.")


    try:
        add_note_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'artdeco-button--secondary') and span[text()='Add a note']]"))
        )
        add_note_button.click()
        sleep(random.uniform(2, 4))
        note_box = driver.find_element(By.XPATH, "//textarea[contains(@name, 'message')]")
        note_text = f"Hello Abdullah, I found your profile and wanted to connect with you regarding potential opportunities. Let's connect!"
        note_box.send_keys(note_text)
        send_button = driver.find_element(By.XPATH, "//button[contains(@class, 'artdeco-button--primary') and span[text()='Send']]")
        send_button.click()
        print("Connection request with a note sent.")

    except TimeoutException:
        print("Could not find the 'Add a note' button")

except TimeoutException:
    print("Timed out waiting for the 'Connect' button to become clickable.")

sleep(random.uniform(2, 5))

# Close the browser
driver.quit()

