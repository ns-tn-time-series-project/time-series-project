import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from env import get_db_url
from pydataset import data
import os



def get_superstore_df():
    '''
    Returns a dataframe from the superstore_db in Codeup's MySQL server
    '''
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
    df = df.sort_index()
    df.ship_date = pd.to_datetime(df.ship_date)
    df['ship_time'] = df.ship_date - df.order_date
    df = df.drop(columns= ['region_id', 'cat_id'])
    return df

def get_superstore_splits(df):
    '''
    Takes in a dataframe (of time-series indexed data),
    returns train, validate, and test splits of the dataframe
    '''
    train_size = round(len(df)*.5)
    validate_size = round(len(df)*.3)
    validate_end_idx = train_size + validate_size
    test_size = (len(df) - train_size - validate_size)

    train = df[:train_size]
    validate = df[train_size:validate_end_idx]
    test = df[validate_end_idx:]

    assert train_size + validate_size + test_size == len(df)

    return train, validate, test
    

    