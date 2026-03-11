from playwright.sync_api import Page, expect
from utils.logger import logger
from utils.config_reader import BASE_URL

class RegisterPage:
    def __init__(self,page: Page):
        self.page = page
        
        #signup Information
        self.signup_login_btn = page.locator("//a[normalize-space()='Signup / Login']")
        self.name_input = page.locator("//input[@placeholder='Name']")
        self.email_input = page.locator("//input[@data-qa='signup-email']")
        self.signup_btn = page.locator("//button[normalize-space()='Signup']")
        
        # Account Information
        self.title = page.locator("//label[normalize-space()='Mr.']")
        self.password = page.locator("//input[@id='password']")
        self.dob_day = page.locator("//select[@id='days']")
        self.dob_month = page.locator("//select[@id='months']")
        self.dob_year = page.locator("//select[@id='years']")
       
        #Address Information
        self.first_name_input = page.locator("//input[@id='first_name']")
        self.last_name_input = page.locator("//input[@id='last_name']")
        self.company_input = page.locator("//input[@id='company']")
        self.address_input = page.locator("(//input[@id='address1'])[1]")
        self.address1_input = page.locator("//input[@id='address2']")
        self.country = page.locator("//select[@id='country']")
        self.state_input = page.locator("//input[@id='state']")
        self.city_input = page.locator("//input[@id='city']")
        self.zip_input = page.locator("//input[@id='zipcode']")
        self.mobile_number = page.locator("//input[@id='mobile_number']")
        
        #create account
        self.create_acc_btn = page.locator("//button[normalize-space()='Create Account']")
        
        
        
    
    def navigate_home(self):
        logger.info("home page is visible successfully ")
        self.page.goto(BASE_URL)
        
    def click_signup_login(self):
        logger.info("Click on 'Signup / Login' button")
        self.signup_login_btn.click()
    
    def signup_user(self, name, email):
        logger.info("Verify 'New User Signup!' is visible")
        logger.info("Enter name and email address")
        self.name_input.fill(name)
        self.email_input.fill(email)
        logger.info(" Click 'Signup' button")
        self.signup_btn.click()
        
    def account_information(self,password):
        self.title.click()
        self.password.fill(password)
        self.dob_day.select_option("5")
        self.dob_month.select_option("3")
        self.dob_year.select_option("2000")
    
    def address_information(self,firstName,lastName,company,address,address1,state,city,zip,mobileNumber):
        self.first_name_input.fill(firstName)
        self.last_name_input.fill(lastName)
        self.company_input.fill(company)
        self.address_input.fill(address)
        self.address1_input.fill(address1)
        self.country.select_option(value="India")
        self.state_input.fill(state)
        self.city_input.fill(city)
        self.zip_input.fill(zip)
        self.mobile_number.fill(mobileNumber)
        
    def create_account(self):
        self.create_acc_btn.click()