from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import creds

password = creds.password
username = creds.username

driver = webdriver.Chrome(creds.webdriverPath)

usernameElem = driver.find_element(By.ID, "username")
passwordElem = driver.find_element(By.ID, "password")


# Login
def Login(username, password):
    driver.get("https://portal.rama-mainz.de")
    usernameElem.clear()
    usernameElem.send_keys(username)
    passwordElem.clear()
    passwordElem.send_keys(password)
    driver.find_element(By.ID, "bttSenden").click()


def GetTimeTable():
    Login(creds.username, creds.password)
    driver.get("https://portal.rama-mainz.de/stdplan.php")
    stdplan = driver.find_element(By.CLASS_NAME, "content")
    return stdplan


def GetVertretung():
    Login(creds.username, creds.password)
    driver.get("https://portal.rama-mainz.de/vertretung.php")
    dates = driver.find_elements(By.CLASS_NAME, "tagesbutton")
    infosOfTheDays = driver.find_elements(By.CLASS_NAME, "nzts")
    return dates, infosOfTheDays


dates, infosOfTheDays = GetVertretung()

with open('stundenplan.html', 'w') as f:
    f.write(GetTimeTable().get_attribute("innerHTML"))
    if (len(dates) != 0):
        with open('infosOfTheDay.txt', 'w') as f:
            f.writelines(dates[0].text + "\n")
            f.write(infosOfTheDays[0].text)

        dates[1].click()
        with open('infosOfTomorrow.txt', 'w') as f:
            f.writelines(dates[1].text + "\n")
            f.write(infosOfTheDays[1].text)
    else:
        print("Portal currently broken")

driver.quit()
