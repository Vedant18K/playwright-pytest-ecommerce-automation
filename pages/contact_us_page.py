from playwright.sync_api import Page , expect
from utils.logger import logger
from utils.config_reader import BASE_URL

class contactUsFrom():
    def __init__(self,page:Page):
        self.page = page
        self.contact_us_page = page.locator("a[href='/contact_us']")
        self.name_input = page.locator("input[placeholder='Nameee']")
        self.email_input = page.locator("//input[@placeholder='Email']")
        self.subject_input = page.locator("input[placeholder='Subject']")
        self.message_input = page.locator("//textarea[@id='message']")
        self.upload_input = page.locator("input[name='upload_file']")
        self.submit_btn = page.locator("input[value='Submit']")
        
    def navigate_home(self):
        self.page.goto(BASE_URL)
        self.contact_us_page.click()
    
    def get_in_touch_from(self,name,email,subject,message,file_path):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.subject_input.fill(subject)
        self.message_input.fill(message)
        # File Upload
        expect(self.upload_input).to_be_visible
        self.upload_input.set_input_files(file_path)
        
        self.submit_btn.click()
              