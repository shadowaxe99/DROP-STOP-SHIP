import requests


class EcommercePlatformAPI:
    def __init__(self, api_key, endpoint):
        self.api_key = api_key
        self.endpoint = endpoint

    def get_sales_data(self):
        # Fetch sales data from ecommerce platform API
        response = requests.get(self.endpoint, headers={'Authorization': 'Bearer ' + self.api_key})
        return response.json()

    def add_product_to_catalog(self, product):
        # Add product to store catalog on ecommerce platform
        payload = {'product_id': product['product_id'], 'title': product['title'], 'description': product['description'], 'images': product['images']}
        response = requests.post(self.endpoint, headers={'Authorization': 'Bearer ' + self.api_key}, json=payload)
        return response.json()

    def remove_product_from_catalog(self, product_id):
        # Remove product from store catalog on ecommerce platform
        response = requests.delete(self.endpoint + '/' + product_id, headers={'Authorization': 'Bearer ' + self.api_key})
        return response.json()