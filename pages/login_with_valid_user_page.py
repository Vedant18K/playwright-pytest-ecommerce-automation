from playwright.sync_api import Page , expect
from utils.logger import logger
from utils.config_reader import BASE_URL


class loginPageValid:
    def __init__(self,page:Page):
        self.page = page
        #Login User
        self.signup_login_btn = page.locator("//a[normalize-space()='Signup / Login']")
        self.login_to_your_acc = page.get_by_text("Login to your account")
        self.email_input = page.locator("//input[@data-qa='login-email']")
        self.passwod_input = page.locator("//input[@placeholder='Password']")
        self.login_btn = page.locator("//button[normalize-space()='Login']")
        self.alert_message = page.get_by_text("Your email or password is incorrect!", exact=True)
        
        #delete user 
        self.delete_acc_btn = page.locator("a[href='/delete_account']")
        self.acc_delete_continue = page.get_by_text("Continue")
        
    def navigate_home(self):
        self.page.goto(BASE_URL)
        self.signup_login_btn.click()
        expect(self.login_to_your_acc).to_be_visible()
    
    def login_with_valid_credential(self,email,password):
        self.email_input.fill(email)
        self.passwod_input.fill(password)
        self.login_btn.click()
        

        
    def delete_login_account(self):
        self.delete_acc_btn.click()
        self.acc_delete_continue.click()