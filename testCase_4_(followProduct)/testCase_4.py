import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
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
    time.sleep(5)
    #element = driver.find_element_by_xpath("//button[text()='Да, верно']").click()

    

    element = driver.find_element_by_xpath("//div[@data-url='https://www.gloria-jeans.ru/c/girls']").click()
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(7)

    element = driver.find_element_by_xpath("(//a[@class='listing-item__info-price-wrapper'])[1]").click()
    time.sleep(3)
    driver.execute_script("window.scrollBy(0, 600);")
    element = driver.find_element_by_xpath("//div[text()='XXS-XS/164']").click()
    element = driver.find_element_by_xpath("(//*[contains(@class, 'js-add-to-wish-button')])[2]").click()
    element = driver.find_element_by_xpath("//a[@href='/wishlist']").click()
    driver.execute_script("window.scrollBy(0, 600);")

    driver.save_screenshot('screenshot.png')
    print('Test Complited!')

finally:
    driver.quit()
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
