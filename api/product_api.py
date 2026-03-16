class ProductsAPI:

    def __init__(self, client):
        self.client = client

    def get_all_products(self):
        return self.client.get("/api/productsList")

    def search_products(self, product_name):
        payload = {"search_product": product_name}
        return self.client.post("/api/searchProduct", payload)
