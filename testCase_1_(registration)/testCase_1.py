import time
import random
import string

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from datetime import datetime

start_time = datetime.now()

password = 'bevkvbwejc23dj'
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
    rand_string = ''.join(random.choice(string.ascii_lowercase) for i in range(4))
    email = rand_string + '@mail.ru'
    element = driver.find_element_by_xpath("//*[text()='Да, верно']").click()
    element = driver.find_element_by_xpath("//span[@data-qa='account-link']").click()
    element = driver.find_element_by_xpath("(//div[@data-block-name='registration'])[1]").click()
    element = driver.find_element_by_xpath("//input[@name='firstName']").send_keys("тест")
    element = driver.find_element_by_xpath("//div[@class='suggestions-suggestions']").click()
    time.sleep(1)
    element = driver.find_element_by_xpath("//input[@data-qa='regEmail']").send_keys(email)
    time.sleep(1)
    element = driver.find_element_by_xpath("//input[@data-qa='regPassword']").send_keys(password)
    time.sleep(1)
    element = driver.find_element_by_xpath("//button[@data-qa='regSubmitBtn']").click()
    time.sleep(10)

    #while True:
    #    element = driver.find_element_by_xpath("//p[text()='Добро пожаловать!']").click()
    #    break
    #else:
    #    time.sleep(1)

    driver.save_screenshot('screenshot.png')
    print('Test Complited!')

finally:
    driver.quit()
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))