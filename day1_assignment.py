# assignment 1 -from scratch(new project-venv..) to 3 open ecommerce
from selenium import webdriver
import time

opti=webdriver.ChromeOptions()
opti.add_experimental_option('detach',True)
chrome_driver=webdriver.Chrome(opti)
print('opening amazon')
chrome_driver.get('https://amazon.in')
time.sleep(5)
print('title: ',chrome_driver.title)
print('opening flipkart')
chrome_driver.get('https://flipkart.com')
time.sleep(5)
print('Title now.. ',chrome_driver.title)
print('opening myntra')
chrome_driver.get('https://myntra.com')
time.sleep(5)
print('and now title-> ',chrome_driver.title)

chrome_driver.close()
# assignment 1
