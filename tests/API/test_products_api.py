from api.product_api import ProductsAPI


def test_get_all_product_list(api_client):

    product_api = ProductsAPI(api_client)

    response = product_api.get_all_products()

    assert response.status == 200

    data = response.json()

    assert "products" in data
    assert len(data["products"]) > 0


def test_search_product(api_client):
    product_api = ProductsAPI(api_client)
    response = product_api.search_products("Top")
    # assert response.status == 405

    # data = response.json()
    # assert data["message"] == "This request method is not supported."
    
