#This challanges covers automative fell up in broweser =>
#Using selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
LINK = "http://secure-retreat-92358.herokuapp.com/"

#Chromes options
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

#Creating driver  
driver = webdriver.Chrome()
driver.get(LINK)

#Workspace
#Defining main variables
name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
click_button = driver.find_element(By.CSS_SELECTOR, value="form button")
#Filling them with values
name.send_keys("Timur")
last_name.send_keys("Malik")
email.send_keys("timuleooo0212@gmail.com")
click_button.click()
