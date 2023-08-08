from metagpt.integrations import EcommercePlatformAPI


class StoreManager:
    def __init__(self, config):
        self.ecommerce_platform_api = EcommercePlatformAPI(config['API_KEYS']['ECOMMERCE_PLATFORM_API_KEY'], config['ENDPOINTS']['ECOMMERCE_PLATFORM_API_ENDPOINT'])

    def add_product_to_catalog(self, product):
        return self.ecommerce_platform_api.add_product_to_catalog(product)

    def remove_product_from_catalog(self, product_id):
        return self.ecommerce_platform_api.remove_product_from_catalog(product_id)