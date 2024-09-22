	
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")
print("Please check screenshot image")
driver.quit()
