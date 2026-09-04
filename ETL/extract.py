import pandas as pd
from pathlib import Path

path_dir = Path('D:/supply_chain_project/Data')
file_name = 'DataCoSupplyChainDataset.csv'

df_supplychain = pd.read_csv(path_dir/file_name, encoding_errors='ignore')

dim_customer = df_supplychain[['Customer Id', 'Customer Fname', 'Customer Lname', 
                    'Customer Segment', 'Customer City', 'Customer State',
                    'Customer Country', 'Customer Street', 'Customer Zipcode']].drop_duplicates(subset=['Customer Id']).reset_index(drop=True)
dim_customer['customer_key'] = dim_customer.index + 1 

df_supplychain = df_supplychain.merge(dim_customer[['Customer Id', 'customer_key']], on='Customer Id', how='left')

dim_product = df_supplychain[['Product Card Id','Product Category Id','Product Name','Product Price','Product Status']].drop_duplicates(subset=['Product Card Id']).reset_index(drop=True)

dim_product['product_key'] = dim_product.index + 1

df_supplychain = df_supplychain.merge(dim_product[['Product Card Id', 'product_key']], on='Product Card Id', how='left')

dim_geography = df_supplychain[['Order City', 'Order State', 'Order Country', 
                     'Order Region', 'Market', 'Latitude', 
                     'Longitude']].drop_duplicates().reset_index(drop=True)
dim_geography['geography_key'] = dim_geography.index + 1

df_supplychain = df_supplychain.merge(dim_geography, 
              on=['Order City', 'Order State', 'Order Country', 
                  'Order Region', 'Market', 'Latitude', 'Longitude'], 
              how='left')

dim_shipping = df_supplychain[['Shipping Mode', 'Delivery Status', 
                    'Late_delivery_risk', 'Order Status', 
                    'Type']].drop_duplicates().reset_index(drop=True)
dim_shipping['shipping_key'] = dim_shipping.index + 1

df_supplychain = df_supplychain.merge(dim_shipping, 
              on=['Shipping Mode', 'Delivery Status', 
                  'Late_delivery_risk', 'Order Status', 'Type'], 
              how='left')

df_supplychain['order date (DateOrders)'] = pd.to_datetime(df_supplychain['order date (DateOrders)'])
df_supplychain['shipping date (DateOrders)'] = pd.to_datetime(df_supplychain['shipping date (DateOrders)'])

all_dates = pd.concat([df_supplychain['order date (DateOrders)'], 
                        df_supplychain['shipping date (DateOrders)']]).drop_duplicates().reset_index(drop=True)

dim_date = pd.DataFrame({'full_date': all_dates})
dim_date['date_key'] = dim_date.index + 1
dim_date['year'] = dim_date['full_date'].dt.year
dim_date['month'] = dim_date['full_date'].dt.month
dim_date['week'] = dim_date['full_date'].dt.isocalendar().week
dim_date['day_of_week'] = dim_date['full_date'].dt.day_name()

df_supplychain = df_supplychain.merge(dim_date[['full_date', 'date_key']], 
              left_on='order date (DateOrders)', right_on='full_date', how='left')
df_supplychain = df_supplychain.rename(columns={'date_key': 'order_date_key'}).drop(columns='full_date')

df_supplychain = df_supplychain.merge(dim_date[['full_date', 'date_key']], 
              left_on='shipping date (DateOrders)', right_on='full_date', how='left')
df_supplychain = df_supplychain.rename(columns={'date_key': 'shipping_date_key'}).drop(columns='full_date')

fact_order_items = df_supplychain[[
    'Order Item Id',        # PK
    'Order Id',              # degenerate dimension
    'customer_key', 'product_key', 'geography_key', 'shipping_key',
    'order_date_key', 'shipping_date_key',
    'Benefit per order', 'Sales per customer',
    'Order Item Discount', 'Order Item Discount Rate',
    'Order Item Product Price', 'Order Item Profit Ratio',
    'Order Item Quantity', 'Sales', 'Order Item Total',
    'Order Profit Per Order',
    'Days for shipping (real)', 'Days for shipment (scheduled)'
]].rename(columns={'Order Item Id': 'order_item_id', 'Order Id': 'order_id'})

print(len(fact_order_items))
print(fact_order_items.isnull().sum())