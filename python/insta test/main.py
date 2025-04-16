from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InstagramBot:
    def __init__(self):
        self.target = "chefsteps"
        self.user_name = "testerdef8"
        self.password = "abdullah123"

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.instagram.com/accounts/login/")

        # Wait for username and password fields to load
        self.username_feild = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div[1]/div[1]/div/label/input"))
        )
        self.password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div[1]/div[2]/div/label/input"))
        )


        self.login()

    def login(self):
        # Locate the login button
        button = self.driver.find_element(
            by=By.XPATH, value="//*[@id='loginForm']/div/div[3]/button"
        )

        # Enter username and password
        self.username_feild.send_keys(self.user_name)
        self.password_field.send_keys(self.password)
        # Click the login button
        button.click()

    def find_followers(self):
        pass

    def follow(self):
        pass


# Instantiate the bot
InstagramBot()


