import time
from selenium import webdriver
from PIL import Image
from Screenshot import Screenshot
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')

driver=webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
url='https://www.youtube.com/feed/trending'
driver.get(url)

driver.save_screenshot('test.png')

screenshot=Image.open('test.png')

screenshot.show()



