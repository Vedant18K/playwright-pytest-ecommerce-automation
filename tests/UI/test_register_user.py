from pages.register_page import RegisterPage
from pages.login_with_valid_user_page import loginPage
from utils.logger import logger
from utils.data_reader import load_test_data


def test_register_user(page, user_data):
    data = load_test_data("data/register_data.json")
    register = RegisterPage(page)
    
    
    email = user_data["email"]
    mobile = user_data["mobile"]
    password = user_data["password"]
        
    print(email,mobile,password)
         
    logger.info("Sign up initiated")
    register.navigate_home()
    register.click_signup_login()
    register.signup_user(data["name"], email)
    logger.info("Account Information initiated")
    register.account_information(password)
    logger.info("Address Information Initiated")
    register.address_information(
        data["first_name"],
        data["last_name"],
        data["company"],
        data["address"],
        data["address2"],
        data["state"],
        data["city"],
        data["zipcode"],
        mobile,
    )
    register.create_account()
    register.continue_account()
    logger.info("User registered successfully")
    
    