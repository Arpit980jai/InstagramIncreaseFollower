import time
import random
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import os

# Insta email and password
email = 'your_email'
password = 'yourpassword'

insta_url = "https://www.instagram.com/"
similar_account = "flutter.developers"  # insta user whom followers bot will follow


class InstaFollower:
    """
    Insta follower bot.
        Login to insta,
        Find followers,
        Follow them,
        Logout.
    """

    def __init__(self):
        """ Initialize Selenium Web Driver """
        self.driver = webdriver.Chrome(executable_path='C:\Development\chromedriver.exe')

    def login_insta(self):
        """ Login to Insta """
        self.driver.get(insta_url)
        time.sleep(3)

        # Get hold of email and password entries
        email_entry = self.driver.find_element(By.NAME, "username")
        password_entry = self.driver.find_element(By.NAME, "password")

        # Type in email & password and press Enter key
        email_entry.send_keys(email)
        password_entry.send_keys(password)
        password_entry.send_keys(Keys.ENTER)
        time.sleep(5)

        # Close the Notification Popup
        self.driver.find_element(By.CSS_SELECTOR, '._ac8f button').click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, '._a9_1').click()

    def find_followers(self):
            # Chefsteps instagram page link.
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{similar_account}")
        time.sleep(10)

        # button that leads to the followers pop-up.
        followers_button = self.driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/div')
        followers_button.click()
        time.sleep(20)

        # To access the followers pop-up.
        f_body = self.driver.find_element(By.XPATH, "//div[@class='_aano']")
        print(f_body)

        # To scroll down thrice in the followers pop-up.
        for i in range(3):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", f_body)
            time.sleep(5)

    def follow(self):
        time.sleep(2)
        for num in range(1, 50):
            time.sleep(5)
            follow_button = self.driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div/div[2]/div/div/"
                                                               f"div[1]/div/div[2]/div/div/div/div/div/div/div/"
                                                               f"div[2]/div[1]/div/div[{num}]/div[3]/button")
            if follow_button.text == "Follow":
                follow_button.click()
            else:
                pass
    def logout_insta(self):
        """ Logout user from the insta """
        # Find profile img and click on it
        profile_img = self.driver.find_element(By.XPATH,
                                               '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img')
        profile_img.click()
        time.sleep(1)
        # Find logout from the drop down menu and click it
        log_out = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div')
        log_out.click()


bot = InstaFollower()
bot.login_insta()
bot.find_followers()
bot.follow()
