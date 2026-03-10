from pages.register_page import RegisterPage
from utils.logger import logger
from utils.data_reader import load_test_data

def test_register_user(page):
    data = load_test_data("data/register_data.json")
    register = RegisterPage(page)
    logger.info("Sign up initiated")
    register.navigate_home()
   
    register.click_signup_login()
    register.signup_user(data["name"],data["email"])
    logger.info("User registered successfully")
    