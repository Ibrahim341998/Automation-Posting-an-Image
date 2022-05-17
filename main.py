import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/immom/Downloads/chromedriver_win32/chromedriver"
imagepath = "C://Users/immom/Downloads/apple-fruit.jpg"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.maximize_window()
print("Current session is {}".format(driver.session_id))
try:
    driver.get("https://www.atg.party/article")
except Exception as e:
    print(e.message)
driver.implicitly_wait(10)

Login_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Login")
Login_button.click()
driver.implicitly_wait(20)

email_field = driver.find_element(By.ID, "email_landing")
email_field.send_keys('wiz_saurabh@rediffmail.com')
driver.implicitly_wait(10)

password_field = driver.find_element(By.ID, "password_landing")
password_field.send_keys('Pass@123')
driver.implicitly_wait(10)
password_field.send_keys(Keys.ENTER)
time.sleep(5)

upload_image = driver.find_element(By.ID, "cover_image").send_keys(imagepath)
time.sleep(5)
title = driver.find_element(By.ID, "title")
title.send_keys("An apple a day keeps a doctor a way")
time.sleep(5)
description = driver.find_element(By.CLASS_NAME, "ce-paragraph")
description.send_keys("Banao Techologies Task 2")
time.sleep(5)

post_article = driver.find_element(By.ID, "hpost_btn")
post_article.send_keys(Keys.ENTER)
time.sleep(5)

current_url = driver.current_url
print(current_url)
time.sleep(5)

f = open("Banao Task2.txt", "a")
f .write(current_url)
print("Record Completed")
f.close()


