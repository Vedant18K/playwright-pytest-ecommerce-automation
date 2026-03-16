from playwright.sync_api import sync_playwright
from utils.config_reader import API_BASE_URL


class APIClient:

    def __init__(self):
        self.playwright = sync_playwright().start()

        self.context = self.playwright.request.new_context(
            base_url=API_BASE_URL,
            extra_http_headers={
                "Content-Type": "application/json"
            }
        )

    def get(self, endpoint, params=None):
        return self.context.get(endpoint, params=params)

    def post(self, endpoint, payload=None):
        return self.context.post(endpoint, data=payload)

    def put(self, endpoint, payload=None):
        return self.context.put(endpoint, data=payload)

    def delete(self, endpoint):
        return self.context.delete(endpoint)

    def close(self):
        self.context.dispose()
        self.playwright.stop()