from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

from allansm.file import File

config = File(".config")

op = Options()

op.add_argument("--private")
op.add_argument("--headless")

op.binary_location = config.lines()[0]

browser = webdriver.Firefox(options=op)
browser.get(input("url:"))

elem = browser.find_element(By.XPATH, "//*")
src = elem.get_attribute("outerHTML")

browser.quit()

print(src)
