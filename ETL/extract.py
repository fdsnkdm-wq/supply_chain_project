import pandas as pd
from pathlib import Path

path_dir = Path('D:/supply_chain_project/Data')
file_name = 'DataCoSupplyChainDataset.csv'

df_supplychain = pd.read_csv(path_dir/file_name, encoding_errors='ignore')

dim_customer = df_supplychain[['Customer Id', 'Customer Fname', 'Customer Lname', 
                    'Customer Segment', 'Customer City', 'Customer State',
                    'Customer Country', 'Customer Street', 'Customer Zipcode']].drop_duplicates(subset=['Customer Id']).reset_index(drop=True)
dim_customer['customer_key'] = dim_customer.index + 1 

#df_supplychain = df_supplychain.merge(dim_customer[['Customer Id', 'customer_key']], on='Customer Id', how='left')

print(dim_customer)