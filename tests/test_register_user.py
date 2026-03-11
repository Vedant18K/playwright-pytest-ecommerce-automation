
from pages.register_page import RegisterPage
from utils.logger import logger
from utils.data_reader import load_test_data
from utils.data_generator import generate_email , generate_mobile

def test_register_user(page):
    data = load_test_data("data/register_data.json")
    register = RegisterPage(page)
    email = generate_email()
    print(email)
    mobile = generate_mobile()
    print(mobile)
    logger.info("Sign up initiated")
    register.navigate_home()
    register.click_signup_login()
    register.signup_user(data["name"],email)
    logger.info("Account Information initiated")
    register.account_information(data["password"])
    logger.info("Address Information Initiated")
    register.address_information(data["first_name"],data["last_name"],data["company"],data["address"],data["address2"],data["state"],data["city"],data["zipcode"],mobile)
    logger.info("Account Created")
    register.create_account()
    logger.info("User registered successfully")
    