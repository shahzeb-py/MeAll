from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Set up Firefox options
firefox_options = Options()
firefox_options.add_argument("--headless")  # Run in headless mode if necessary

# Specify the path to geckodriver
service = Service("/data/data/com.termux/files/usr/bin/geckodriver")

# Initialize the WebDriver
driver = webdriver.Firefox(service=service, options=firefox_options)

# Open a webpage
driver.get("https://chatgpt.com/")
time.sleep(3)  # Wait for the page to load

# Print the title of the page
print(driver.title)

# Close the driver
driver.quit()
