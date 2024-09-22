import re
import logging
import queue
import time
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ids import *
# Set logging level for selenium to WARNING to suppress INFO messages
logging.getLogger('selenium').setLevel(logging.WARNING)
user_input = input("start index: ")
user_input2 = input("Total Chromes: ")
# Define the message function
def message(account):
    start_time = time.time()
    post = "https://www.facebook.com/permalink.php?story_fbid=pfbid02DqogS977PeGU3ALXAawPRZxZXzpzNfgs7sSnp4brGYmCPnAMog3TFLtkqs9F2urJl&id=61565582983950"
    uids = []
    pattern = r"fbid=(\d+)"

    # Chrome options setup
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("--window-size=1920x1080")  # Set a fixed window size
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2})
    chrome_options.add_argument('--disable-extensions')  # Disable extensions
    chrome_options.add_argument('--start-maximized')  # Start maximized
    chrome_options.add_argument('--disable-popup-blocking')  # Disable popup blocking
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    # Start ChromeDriver
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.implicitly_wait(3)
        driver.get("https://www.facebook.com/login/")
        driver.find_element(By.XPATH, '//input[@id="email"]').send_keys(accounts[account][0])
        driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(accounts[account][1])
        driver.find_element(By.XPATH, '//button[@id="loginbutton"]').click()
        
        # Check login status
        current_url = driver.current_url
        if "checkpoint" in current_url or "device-based/regular/login/?login_attempt" in current_url:
            try:
                driver.find_element(By.XPATH,'//div[@aria-label="Dismiss"]').click()
            except:
                print(f"{account} - login issue detected.")
                driver.quit()
                return
        if "two_step_verification" in current_url:
            print(f"remove verification from {account}")
            driver.quit()
            return
        try:
            driver.get("https://mbasic.facebook.com/buddylist.php")
            active_elements = driver.find_elements(By.XPATH, '//a[@class="bq"]')

            # Extract user IDs
            for element in active_elements:
                href = element.get_attribute('href')
                if href:
                    match = re.search(pattern, href)
                    if match:
                        uids.append(match.group(1))
        except:
            print("getting error in mbasic") 
        # Send messages

        num_uids = len(uids)
        driver.implicitly_wait(20)
        for uid in uids:
            
            try:
                driver.get(f"https://www.facebook.com/messages/t/{uid}")
                textbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Message"]')))
                textbox.click()
                textbox.send_keys(post)
                textbox.send_keys(Keys.ENTER)
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Sent")]')))
                time.sleep(1)
            except Exception as e:
                print(e)
                pass
        time.sleep(2)
        end_time = time.time()  # End timing
        elapsed_time = end_time - start_time
        minutes, seconds = divmod(elapsed_time, 60)
        print(f"{num_uids} Messages by {account} time: {int(minutes)} minutes and {seconds:.2f} seconds")
        driver.quit()
        return
    except :
        driver.quit()
        print(f"having issue in {account}")
        return


start_index = user_input
max_workers = user_input2
chrome_queue = queue.Queue()

ending=len(accounts)
for i in range(start_index,ending):
    chrome_queue.put(i)

def process_chrome():
    while not chrome_queue.empty():
        account = chrome_queue.get()
        message(account)
        chrome_queue.task_done()

# Create a ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
    # Submit the process_chrome function for each worker
    workers = [executor.submit(process_chrome) for _ in range(max_workers)]
    
    # Wait for all tasks to complete
    chrome_queue.join()
