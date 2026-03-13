from playwright.sync_api import Page , expect
from utils.logger import logger 
from utils.config_reader import BASE_URL

class searchProduct:
    def __init__(self, page:Page):
        self.page = page
        self.product_link = page.locator("//a[@href='/products']")
        self.search_product_text = page.get_by_role("textbox", name="Search Product")
        self.all_product_text = page.get_by_role("heading", name="All Products")
        self.search_product = page.locator("//input[@id='search_product']")
        self.search_product_text = page.get_by_role("heading", name="Searched Products")
        self.search_btn = page.locator("//button[@id='submit_search']")
        
    def navigate_home(self):
        logger.info("Home Page is visible successfully")
        self.page.goto(BASE_URL)
        
    
    def search_product_test(self,):
        logger.info("Search Product initiated")
        # expect(self.product_link).to_be_visible()
        # print("Product is visible")
        # self.product_link.click()
        self.page.goto("https://automationexercise.com/products")
        print("CLicked on product")
        
        # expect(self.search_product_text).to_be_visible()
        expect(self.all_product_text).to_be_visible()
        self.search_product.fill("Blue Top")
        self.search_btn.click()
        expect(self.search_product_text).to_be_visible()
        