from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Set up Firefox options
firefox_options = Options()
firefox_options.add_argument("--headless")  # Optional: Run in headless mode

# Specify the path to geckodriver
service = Service("/data/data/com.termux/files/usr/bin/geckodriver")

# Using the with statement to manage the WebDriver
with webdriver.Firefox(service=service, options=firefox_options) as driver:
    # Open a webpage
    driver.get("https://www.whatismybrowser.com/")  # Example page to check user agent
    time.sleep(3)  # Wait for the page to load

    # Get the user agent using JavaScript
    user_agent = driver.execute_script("return navigator.userAgent;")
    print("User Agent:", user_agent)

# The driver will be automatically closed when the block exits
