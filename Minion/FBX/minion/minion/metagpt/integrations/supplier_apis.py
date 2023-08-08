import requests


class SupplierAPI:
    def __init__(self, api_key, endpoint):
        self.api_key = api_key
        self.endpoint = endpoint

    def perform_product_research(self):
        # Perform product research using supplier API
        response = requests.get(self.endpoint + '/product_research', headers={'Authorization': 'Bearer ' + self.api_key})
        return response.json()

    def generate_product_listings(self):
        # Generate product listings using supplier API
        response = requests.get(self.endpoint + '/generate_listings', headers={'Authorization': 'Bearer ' + self.api_key})
        return response.json()

    def process_orders(self):
        # Process orders using supplier API
        response = requests.get(self.endpoint + '/process_orders', headers={'Authorization': 'Bearer ' + self.api_key})
        return response.json()

    def track_metrics(self):
        # Track metrics using supplier API
        response = requests.get(self.endpoint + '/track_metrics', headers={'Authorization': 'Bearer ' + self.api_key})
        return response.json()