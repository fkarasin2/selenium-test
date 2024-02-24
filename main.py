from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

service = Service('./chromedriver')
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://www.apple.com')