from selenium.webdriver.common.by import By
import random
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
firstnam  = [
    'Aarohi', 'Abhilasha', 'Aishwarya', 'Akanksha', 'Alka', 'Amita', 'Ankita', 
    'Aparna', 'Aradhya', 'Avantika', 'Bhoomika', 'Chandni', 'Charvi', 'Chitra', 
    'Devika', 'Dhara', 'Disha', 'Elina', 'Esha', 'Garima', 'Gauri', 'Gunjan', 
    'Hiral', 'Indira', 'Isha', 'Jagruti', 'Jaya', 'Jyotsna', 'Kalyani', 'Kanika', 
    'Karishma', 'Kavya', 'Lavanya', 'Maanvi', 'Mahima', 'Malini', 'Mukta', 'Namita', 
    'Nandita', 'Nilima', 'Pragya', 'Purvi', 'Reema', 'Rekha', 'Renuka', 'Ritika', 
    'Ruhi', 'Sanjana', 'Sheela', 'Shikha', 'Shilpa', 'Shreya', 'Shweta', 'Simran', 
    'Smita', 'Sneha', 'Sonia', 'Soumya', 'Sukanya', 'Swati'
]

lastnam = [
    'Agarwal', 'Bansal', 'Bhardwaj', 'Chawla', 'Chopra', 'Desai', 'Deshmukh', 
    'Dubey', 'Gandhi', 'Ghosh', 'Gupta', 'Iyer', 'Jain', 'Joshi', 'Kapoor', 
    'Khanna', 'Khurana', 'Malhotra', 'Mehta', 'Menon', 'Mishra', 'Mukherjee', 
    'Nair', 'Patel', 'Rao', 'Reddy', 'Saxena', 'Sharma', 'Shetty', 'Singh', 
    'Srivastava', 'Verma'
]

date = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']
month = ['1', '2', '3', '4', '5', '6', '7','8', '9', '10', '11', '12']

year = ['1998','1999','1997','2000','2001']

def UserAgentss():
    user_agents =["Mozilla/5.0 (Linux; Android 13; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Mobile Safari/537.36"]
    current_user_agent =random.choice(user_agents)
    return current_user_agent
def generate_random_indian_number_with_country_code():
    country_code = "+91"
    first_digit = random.choice(['6', '7', '8', '9'])
    remaining_digits = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    return f"{country_code}{first_digit}{remaining_digits}"



# Instantiate Service and Options inside the thread
service = Service("/data/data/com.termux/files/usr/bin/geckodriver")
firefox_options = Options()
firefox_options.add_argument("--headless")
custom_user_agent = "Mozilla/5.0 (Linux; Android 15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.69 Mobile Safari/537.36"
firefox_options.set_preference("dom.webnotifications.enabled", False)
firefox_options.set_preference("privacy.popups.showBrowserMessage", False)
firefox_options.set_preference("browser.startup.homepage", "about:blank")
# Disable telemetry
firefox_options.set_preference("toolkit.telemetry.reportingpolicy.firstRun", False)
firefox_options.set_preference("toolkit.telemetry.enabled", False)

# Disable media playback
firefox_options.set_preference("media.autoplay.default", 1)

# Disable WebRTC (to prevent leaking local IP)
firefox_options.set_preference("media.peerconnection.enabled", False)

# Disable Firefox's default "Your browser is being controlled by automated test software" message
firefox_options.set_preference("dom.webdriver.enabled", False)

# Set the browser to appear as a regular user
firefox_options.set_preference("general.useragent.site_specific_overrides.enabled", False)

# Other general settings
firefox_options.set_preference("browser.cache.disk.enable", False)
firefox_options.set_preference("browser.cache.memory.enable", False)
firefox_options.set_preference("browser.cache.offline.enable", False)

firefox_options.set_preference("general.useragent.override", custom_user_agent)

# Start the WebDriver
def Create():
    random_number = str(random.randint(1000000, 9999999))
    random_numbers = str(random.randint(100, 99999))
    forth= random.randint(1,8)
    third= random.randint(0,4)
    fn = random.choice(firstnam)
    ln = random.choice(lastnam)
    dt = random.choice(date)
    mt = random.choice(month)
    yr = random.choice(year)
    driver = webdriver.Firefox(service=service, options=firefox_options)
    try:
        driver.implicitly_wait(6)
        GetStarted= driver.find_element(By.XPATH,'//div[@aria-label="Get Started" and @role="button"]')
        GetStarted.click()
    except:
        driver.quit()
        return
    try:
        firstname = driver.find_element(By.XPATH,'//input[@aria-label="First name"]')
        firstname.send_keys(fn)
        time.sleep(1)
        lastname = driver.find_element(By.XPATH,'//input[@aria-label="Surname"]')
        lastname.send_keys(ln)
        time.sleep(1)
        next = driver.find_element(By.XPATH,'//div[@aria-label="Next" and @role="button"]')
        next.click()
    
        
        date_input = driver.find_element(By.CSS_SELECTOR, 'input[type="date"]')
        date_input.clear()
        time.sleep(1)
        date_input.send_keys(f'{mt}{dt}{yr}')
        date_input.send_keys(Keys.RETURN)
        next = driver.find_element(By.XPATH,'//div[@aria-label="Next" and @role="button"]')
        next.click()
        female = driver.find_element(By.XPATH,'//div[@aria-label="Female"]')
        #male = driver.find_element(By.XPATH,'//div[@aria-label="Male"]')
        #gender_elements = [female, male]
        gender = female#random.choice(gender_elements)
        gender.click()
        next = driver.find_element(By.XPATH,'//div[@aria-label="Next" and @role="button"]')
        next.click()
        time.sleep(6)
        Number= driver.find_element(By.XPATH,'//input[@aria-label="Mobile number"]')
        Number.click()
        Number.send_keys(f"03{third}{forth} {random_number}")
        next = driver.find_element(By.XPATH,'//div[@aria-label="Next" and @role="button"]')
        next.click()
    
        putpassword = driver.find_element(By.XPATH,'//input[@aria-label="Password"]')
        password=f"{fn}{yr}gf2S"
        putpassword.send_keys(password)
        next = driver.find_element(By.XPATH,'//div[@aria-label="Next" and @role="button"]')
        next.click()
    except:
            
        driver.quit()
        return 
    
    savelogin=driver.find_element(By.XPATH,'//div[@aria-label="Save"]')
    savelogin.click()
    agreeterms=driver.find_element(By.XPATH,'//div[@aria-label="I agree"]')
    agreeterms.click()
    timee =random.randint(6,8)
    time.sleep(timee)
    driver.implicitly_wait(30)
    
    try:
        driver.find_element(By.XPATH,'//div[@aria-label="Continue"]').click()
    except:
            
            pass
    driver.implicitly_wait(5)
    driver.get("https://m.facebook.com/confirmemail.php?soft=hjk")
    try:
        didNotRecieved = driver.find_element(By.LINK_TEXT,"I Didn't Receive the Code")
        didNotRecieved.click()
        sendcodeagain = driver.find_element(By.LINK_TEXT,"Send Code Again")
        sendcodeagain.click()
        didNotRecieved = driver.find_element(By.LINK_TEXT,"I Didn't Receive the Code")
        didNotRecieved.click()
    except:
        try:
            didNotRecieved = driver.find_element(By.LINK_TEXT,"I didn't get the code")
            didNotRecieved.click()
            sendcodeagain = driver.find_element(By.LINK_TEXT,"Send Code Again")
            sendcodeagain.click()
            didNotRecieved = driver.find_element(By.LINK_TEXT,"I didn't get the code")
            didNotRecieved.click()
        except:
                
            driver.quit()
            return  
    confirmbyemail= driver.find_element(By.XPATH,'//a[@class="_6if8 _8x0i _8xqj _8x0k" and @href="/changeemail/" and @target="_self" and @sigil="no_mpc"]')
    confirmbyemail.click()
    email= driver.find_element(By.XPATH,'//input[@name="new"]')
    email.click()

    copiedText = input("enter email")
    try:
        email.send_keys(copiedText)
        add= driver.find_element(By.XPATH,'//button[@type="submit" and @value="Add"]')
        add.click()
    except:
        driver.quit()
        return 
    code=input("enter code")
    putcode = driver.find_element(By.XPATH,'//input[@type="number"]')
    putcode.click()
    putcode.send_keys(code)
    confirm= driver.find_element(By.XPATH,"//a[contains(text(), 'Confirm')]")
    confirm.click()
    print(f"{copiedText}|{password}")
    time.sleep(10)
    driver.quit()
    return
Create()
