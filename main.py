from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import creds

password = creds.password
username = creds.username

driver = webdriver.Chrome(creds.webdriverPath)

driver.get("https://portal.rama-mainz.de")

usernameElem = driver.find_element(By.ID, "username")
passwordElem = driver.find_element(By.ID, "password")

#Login
usernameElem.clear()
usernameElem.send_keys(username)
passwordElem.clear()
passwordElem.send_keys(password)

driver.find_element(By.ID, "bttSenden").click()

driver.get("https://portal.rama-mainz.de/stdplan.php")

stdplan = driver.find_element(By.CLASS_NAME, "content")

with open('stundenplan.html', 'w') as f:
    f.write(stdplan.get_attribute("innerHTML"))

driver.get("https://portal.rama-mainz.de/vertretung.php")

dates = driver.find_elements(By.CLASS_NAME, "tagesbutton")
print(len(dates))
infosOfTheDays = driver.find_elements(By.CLASS_NAME, "nzts")
if(len(dates) != 0):
    with open('infosOfTheDay.txt', 'w') as f:
        f.writelines(dates[0].text + "\n")
        f.write(infosOfTheDays[0].text)


    dates[1].click()
    with open('infosOfTomorrow.txt', 'w') as f:
        f.writelines(dates[1].text + "\n")
        f.write(infosOfTheDays[1].text)

driver.quit()