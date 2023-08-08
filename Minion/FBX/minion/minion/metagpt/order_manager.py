from metagpt.integrations import SupplierAPI, ShippingAPI


def purchase_inventory():
    # Initialize supplier API
    supplier_api = SupplierAPI('your_supplier_api_key', 'supplier_api_endpoint')

    # Purchase inventory for orders
    orders = get_orders()
    for order in orders:
        supplier_api.purchase_inventory(order['product_id'], order['quantity'])


def generate_shipping_labels():
    # Initialize shipping API
    shipping_api = ShippingAPI('your_shipping_api_key', 'shipping_api_endpoint')

    # Generate shipping labels for orders
    orders = get_orders()
    for order in orders:
        shipping_api.generate_shipping_label(order['shipping_address'])


def send_email_notifications():
    # Send email notifications to customers on order status
    orders = get_orders()
    for order in orders:
        send_email_notification(order['customer_email'], 'Your order has been shipped', 'Your order has been shipped and is on its way to you.')