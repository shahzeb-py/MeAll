import time
start_time = time.time()
import queue
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
elapsed_time = time.time() - start_time
print(f"Elapsed Time: {elapsed_time:.2f} seconds")
custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
firefox_options = Options()
firefox_options.add_argument("--headless")
firefox_options.set_preference("general.useragent.override", custom_user_agent)

service = Service("/data/data/com.termux/files/usr/bin/geckodriver")
def message(g):
    with webdriver.Firefox(service=service, options=firefox_options) as driver:
        elapsed_time = time.time() - start_time
        print(f"Elapsed Time: {elapsed_time:.2f} seconds")
        driver.get("https://www.whatismybrowser.com/")  
        user_agent = driver.execute_script("return navigator.userAgent;")
        print("User Agent:", user_agent)
        elapsed_time = time.time() - start_time
        print(f"Elapsed Time: {elapsed_time:.2f} seconds")


chrome_queue = queue.Queue()

for i in range(1,11):
    chrome_queue.put(i)

def process_chrome():
    while not chrome_queue.empty():
        account = chrome_queue.get()
        message(account)
        chrome_queue.task_done()

# Create a ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    # Submit the process_chrome function for each worker
    workers = [executor.submit(process_chrome) for _ in range(10)]
    
    # Wait for all tasks to complete
    chrome_queue.join()
