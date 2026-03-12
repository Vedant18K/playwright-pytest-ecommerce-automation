from playwright.sync_api import Page , expect
from utils.logger import logger
from utils.config_reader import BASE_URL

class loginPageInvalid():
    def __init__(self,page:Page):
        self.page = page
        self.signup_login_btn = page.locator("//a[normalize-space()='Signup / Login']")
        self.login_to_your_acc = page.get_by_text("Login to your account")
        self.email_input = page.locator("//input[@data-qa='login-email']")
        self.passwod_input = page.locator("//input[@placeholder='Password']")
        self.login_btn = page.locator("//button[normalize-space()='Login']")
        self.alert_message = page.get_by_text("Your email or password is incorrect!", exact=True)
        
    def navigate_home(self):
        self.page.goto(BASE_URL)
        self.signup_login_btn.click()
        expect(self.login_to_your_acc).to_be_visible()
    
        
    def login_with_invalid_credential(self,email,password):
        self.email_input.fill(email)
        self.passwod_input.fill(password)
        self.login_btn.click()
        #define verify message 
        expect(self.alert_message).to_be_visible()