from metagpt.integrations import SupplierAPI, EcommercePlatformAPI
import pandas as pd


def track_metrics():
    # Initialize supplier API and ecommerce platform API
    supplier_api = SupplierAPI('your_supplier_api_key', 'supplier_api_endpoint')
    ecommerce_platform_api = EcommercePlatformAPI('your_ecommerce_platform_api_key', 'ecommerce_platform_api_endpoint')

    # Fetch product performance data from supplier API
    product_performance_data = supplier_api.get_product_performance()

    # Fetch sales data from ecommerce platform API
    sales_data = ecommerce_platform_api.get_sales_data()

    # Convert data to DataFrames
    df_product_performance = pd.DataFrame(product_performance_data)
    df_sales = pd.DataFrame(sales_data)

    # Merge data on product_id
    df = pd.merge(df_product_performance, df_sales, on='product_id')

    # Calculate metrics
    df['profit'] = df['sales'] * df['profit_margin']
    df['roi'] = df['profit'] / df['cost']

    # Return DataFrame with metrics
    return df


def generate_reports(df):
    # Generate reports on store performance
    sales_report = df['sales'].sum()
    profit_report = df['profit'].sum()
    roi_report = df['roi'].mean()

    # Return reports
    return {'sales_report': sales_report, 'profit_report': profit_report, 'roi_report': roi_report}