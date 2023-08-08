from goop.roles import Ecommerce, Marketing, Finance


class DropshippingWorkflow:
    def __init__(self, config):
        self.ecommerce = Ecommerce(config)
        self.marketing = Marketing(config)
        self.finance = Finance(config)

    def run(self):
        self.ecommerce.product_research()
        self.ecommerce.generate_product_listing()
        self.ecommerce.process_order()
        self.ecommerce.track_metrics()
        self.marketing.run_marketing_campaign()
        self.finance.generate_reports()