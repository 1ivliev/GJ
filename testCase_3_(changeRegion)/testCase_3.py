import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from datetime import datetime

start_time = datetime.now()
password = 'bevkvbwejc23dj'
login = 'tvte@mail.ru'

WINDOW_SIZE = "1920,1080"

caps = DesiredCapabilities.FIREFOX
#chrome_options = Options()  
#chrome_options.add_argument("--headless")  
#chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
driver = webdriver.Remote('http://localhost:4444',desired_capabilities=caps, 
#options=chrome_options
)

driver.implicitly_wait(20)
driver.maximize_window()
link = "https://www.gloria-jeans.ru/"
driver.get(link)

try:

    element = driver.find_element_by_xpath("//*[text()='Да, верно']").click()
    element = driver.find_element_by_xpath("//span[@data-qa='account-link']").click()
    element = driver.find_element_by_xpath("//input[@data-qa='loginEmail']").send_keys(login)
    time.sleep(1)
    element = driver.find_element_by_xpath("//input[@data-qa='loginPassword']").send_keys(password)
    time.sleep(1)
    element = driver.find_element_by_xpath("//button[@data-qa='loginSubmit']").click()
    #time.sleep(4)
    WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-pop-up-name='region-delivery']"))).click()
    #element = driver.find_element_by_xpath("//span[@data-pop-up-name='region-delivery']").click()
    #time.sleep(1)

    WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-region-code='61']"))).click()

    
    #element = driver.find_element_by_xpath("//span[@data-region-code='61']").click()
    time.sleep(1)
    driver.save_screenshot('screenshot.png')
    print('Test Complited!')

finally:
    driver.quit()
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
