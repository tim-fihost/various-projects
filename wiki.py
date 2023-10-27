from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("datch",True)

driver = webdriver.Chrome()
driver.get(LINK)
articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(articles.text)
