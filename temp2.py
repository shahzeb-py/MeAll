from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run headless if you don't need a UI

# Initialize the driver
service = Service('/data/data/com.termux/files/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=options)

# Example: Open a webpage
driver.get("https://www.example.com")
print(driver.title)

# Close the driver
driver.quit()
