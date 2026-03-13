from pages.search_product import searchProduct
from utils.logger import logger
from utils.data_reader import load_test_data


def test_search_product(page):
    data = load_test_data("data/register_data.json")
    search = searchProduct(page)

    search.navigate_home()
    search.search_product_test()
