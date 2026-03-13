from pages.contact_us_page import contactUsFrom
from utils.logger import logger
from utils.data_reader import load_test_data


def test_contact_us_form(page):
    data = load_test_data("data/login_data.json")
    contact = contactUsFrom(page)

    contact.navigate_home()
    contact.get_in_touch_from(
        data["contact_us_form"]["name"],
        data["contact_us_form"]["email"],
        data["contact_us_form"]["subject"],
        data["contact_us_form"]["message"],
        data["contact_us_form"]["file_path"]
    )
