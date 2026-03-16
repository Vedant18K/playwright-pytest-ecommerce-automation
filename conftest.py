import pytest
from utils.data_generator import generate_email, generate_mobile, generate_password
from utils.api_client import APIClient


@pytest.fixture(scope="session")
def user_data():
    return {
        "email": generate_email(),
        "password": generate_password(),
        "mobile": generate_mobile(),
    }


@pytest.fixture(scope="session")
def api_client():
    client = APIClient()
    yield client
    client.close()
