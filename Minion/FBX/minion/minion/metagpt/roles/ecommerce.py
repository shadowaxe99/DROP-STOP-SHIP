from goop.integrations import SupplierAPI, ShippingAPI, EmailAPI


class Ecommerce:
    def __init__(self, config):
        self.supplier_api = SupplierAPI(config['API_KEYS']['SUPPLIER_API_KEY'], config['ENDPOINTS']['SUPPLIER_API_ENDPOINT'])
        self.shipping_api = ShippingAPI(config['API_KEYS']['SHIPPING_API_KEY'], config['ENDPOINTS']['SHIPPING_API_ENDPOINT'])
        self.email_api = EmailAPI(config['API_KEYS']['EMAIL_API_KEY'], config['ENDPOINTS']['EMAIL_API_ENDPOINT'])

    def product_research(self):
        # Perform product research
        research_results = self.supplier_api.perform_product_research()
        # Process research results
        # ...

    def generate_product_listing(self):
        # Generate product listings
        listings = self.supplier_api.generate_product_listings()
        # Process listings
        # ...

    def process_order(self):
        # Process orders
        orders = self.supplier_api.process_orders()
        # Process orders
        # ...

    def track_metrics(self):
        # Track metrics
        metrics = self.supplier_api.track_metrics()
        # Process metrics
        # ...

    def send_email_notification(self):
        # Send email notification
        email = self.email_api.send_email()
        # Process email
        # ...