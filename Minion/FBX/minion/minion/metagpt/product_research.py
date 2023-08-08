from metagpt.integrations import SupplierAPI
import pandas as pd


def perform_product_research():
    # Initialize supplier API
    supplier_api = SupplierAPI('your_supplier_api_key', 'supplier_api_endpoint')

    # Fetch product data from supplier API
    product_data = supplier_api.get_product_data()

    # Convert product data to DataFrame
    df = pd.DataFrame(product_data)

    # Analyze product data to identify trending and profitable products
    trending_products = df[df['sales'] > df['sales'].quantile(0.9)]
    profitable_products = df[df['profit_margin'] > df['profit_margin'].quantile(0.9)]

    # Return the intersection of trending and profitable products
    return pd.merge(trending_products, profitable_products, how='inner', on=['product_id'])