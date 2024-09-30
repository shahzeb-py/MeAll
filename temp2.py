
import random
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
custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
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
    driver = webdriver.Firefox(service=service, options=firefox_options)
    driver.get("https://www.whatismybrowser.com/")  
    user_agent = driver.execute_script("return navigator.userAgent;")
    print(f"User Agent {user_agent}")


Create()
