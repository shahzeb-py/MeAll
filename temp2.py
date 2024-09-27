import time
start_time = time.time()

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
elapsed_time = time.time() - start_time
print(f"Elapsed Time: {elapsed_time:.2f} seconds")

custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"

# Set up Firefox options
firefox_options = Options()
firefox_options.add_argument("--headless")  # Optional: Run in headless mode
firefox_options.set_preference("general.useragent.override", custom_user_agent)

# Specify the path to geckodriver
service = Service("/data/data/com.termux/files/usr/bin/geckodriver")

# Using the with statement to manage the WebDriver
with webdriver.Firefox(service=service, options=firefox_options) as driver:
    elapsed_time = time.time() - start_time
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")

    # Open a webpage
    driver.get("https://www.whatismybrowser.com/")  # Example page to check user agent
    # Get the user agent using JavaScript
    user_agent = driver.execute_script("return navigator.userAgent;")
    print("User Agent:", user_agent)
    elapsed_time = time.time() - start_time
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")

# The driver will be automatically closed when the block exits
