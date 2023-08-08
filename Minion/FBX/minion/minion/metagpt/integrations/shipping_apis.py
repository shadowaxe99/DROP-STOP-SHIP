import requests


class ShippingAPI:
    def __init__(self, api_key, endpoint):
        self.api_key = api_key
        self.endpoint = endpoint

    def generate_shipping_label(self, shipping_address):
        # Generate shipping label using shipping API
        payload = {'shipping_address': shipping_address}
        headers = {'Authorization': 'Bearer ' + self.api_key}
        response = requests.post(self.endpoint + '/generate_label', json=payload, headers=headers)
        return response.json()