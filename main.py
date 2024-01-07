import urllib
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

url = "https://google.com"
options = Options()
# options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
driver.get(url)

time.sleep(100)

# element_present = EC.presence_of_element_located((By.CLASS_NAME, 'paginamanga'))
# WebDriverWait(driver, 360).until(element_present)

# img = driver.find_element(By.CLASS_NAME, 'paginamanga')
# src = img.get_attribute('src')

# urllib.urlretrieve(src, "test.png")

driver.close()