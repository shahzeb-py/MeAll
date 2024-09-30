
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options



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
driver = webdriver.Firefox(service=service, options=firefox_options)
driver.get("https://www.whatismybrowser.com/")  
user_agent = driver.execute_script("return navigator.userAgent;")
print(f"User Agent {user_agent}")
