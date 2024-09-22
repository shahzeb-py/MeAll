from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run headless if you don't need a UI

# Initialize the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Example: Open a webpage
driver.get("https://www.example.com")
print(driver.title)

# Close the driver
driver.quit()
