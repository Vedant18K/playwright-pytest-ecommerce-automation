from playwright.sync_api import Page
from utils.logger import logger
from utils.config_reader import BASE_URL

class RegisterPage:
    def __init__(self,page: Page):
        self.page = page
        self.signup_login_btn = page.locator("//a[normalize-space()='Signup / Login']")
        self.name_input = page.locator("//input[@placeholder='Name']")
        self.email_input = page.locator("//input[@data-qa='signup-email']")
        self.signup_btn = page.locator("//button[normalize-space()='Signup']")
        
    
    def navigate_home(self):
        logger.info("Home Page ")
        self.page.goto(BASE_URL)
        
    def click_signup_login(self):
        self.signup_login_btn.click()
    
    def signup_user(self, name, email):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.signup_btn.click()