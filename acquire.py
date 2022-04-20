import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from env import get_db_url
from pydataset import data
import os



def get_superstore_df():
    filename = 'superstore_inner.csv'
    if os.path.exists(filename):
        print('Reading from CSV file...')
        return pd.read_csv(filename)
    
    url = get_db_url('superstore_db')
    query = '''
    SELECT * FROM orders
    JOIN categories USING(`Category ID`)
    JOIN customers USING(`Customer ID`)
    JOIN products USING(`Product ID`)
    JOIN regions USING(`Region ID`);
    '''
    df = pd.read_sql(query, url)
    print('Copying to CSV...')
    df.to_csv(filename)
    return df


def clean_superstore_df(df):
    '''
    Takes in the superstore dataset df, 
    returns a clean version for split
    '''
    
    df = df.rename(columns= {
    'Region ID': 'region_id', 
    'Product ID': 'product_id', 
    'Customer ID': 'customer_id',
    'Category ID': 'cat_id',
    'Order ID': 'order_id',
    'Order Date': 'order_date',
    'Ship Date': 'ship_date',
    'Ship Mode': 'ship_mode',
    'Segment': 'segment',
    'Country': 'country',
    'City': 'city',
    'State': 'state',
    'Postal Code': 'postal_code', 
    'Sales': 'sales',
    'Quantity': 'quantity',
    'Discount': 'discount',
    'Profit': 'profit',
    'Category': 'category',
    'Sub-Category': 'sub_cat',
    'Customer Name': 'cust_name',
    'Product Name': 'prod_name',
    'Region Name': 'region'
    })
    df.order_date = pd.to_datetime(df.order_date)
    df.order_date = df.order_date.sort_values()
    df = df.set_index(df.order_date)
    df.ship_date = pd.to_datetime(df.ship_date)
    df['ship_time'] = df.ship_date - df.order_date
    df = df.drop(columns= ['region_id', 'cat_id'])
    