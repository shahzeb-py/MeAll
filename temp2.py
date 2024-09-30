import time
import queue
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Measure total elapsed time
start_time = time.time()

custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"

chrome_queue = queue.Queue()

# Populate the queue
for i in range(1, 11):
    chrome_queue.put(i)

def message(g):
    # Instantiate Service and Options inside the thread
    service = Service("/data/data/com.termux/files/usr/bin/geckodriver")
    firefox_options = Options()
    firefox_options.add_argument("--headless")
    firefox_options.set_preference("general.useragent.override", custom_user_agent)

    # Start the WebDriver
    with webdriver.Firefox(service=service, options=firefox_options) as driver:
        driver.get("https://www.whatismybrowser.com/")  
        user_agent = driver.execute_script("return navigator.userAgent;")
        print(f"User Agent for task {g}: {user_agent}")

# Process the Chrome queue
def process_chrome():
    while not chrome_queue.empty():
        account = chrome_queue.get()
        message(account)
        chrome_queue.task_done()

# Create a ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:  # Reduce max_workers
    # Submit the process_chrome function for each worker
    workers = [executor.submit(process_chrome) for _ in range(5)]  # Reduce to 5 workers
    # Wait for all tasks to complete
    chrome_queue.join()

# Final elapsed time
elapsed_time = time.time() - start_time
print(f"Total Elapsed Time: {elapsed_time:.2f} seconds")
