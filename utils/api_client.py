import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()

    def post(self, endpoint, json=None, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = self.session.post(url, json=json, **kwargs)
            return response
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            raise
