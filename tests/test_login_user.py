from pages.login_with_valid_user_page import loginPageValid
from pages.login_with_invalid_user import loginPageInvalid
from utils.logger import logger
from utils.data_reader import load_test_data


def test_login_user_with_correct_credentail(page):
    data = load_test_data("data/login_data.json")
    login = loginPageValid(page)

    logger.info("user Login initiated ")

    login.navigate_home()
    login.login_with_valid_credential(
        data["valid_credentials"]["email"], data["valid_credentials"]["password"]
    )

    logger.info("User login successfully")

    login.delete_login_account()
    logger.info("Account Deleted with correct Credential")


def test_login_user_with_incorrect_credential(page):
    data = load_test_data("data/login_data.json")
    login_invalid = loginPageInvalid(page)
    login_invalid.navigate_home()
    login_invalid.login_with_invalid_credential(data["invalid_credentials"]["email"],data["invalid_credentials"]["password"])
    