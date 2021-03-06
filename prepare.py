import numpy as np
import pandas as pd
# datetime utilities
from datetime import timedelta, datetime
# visualization
import matplotlib.pyplot as plt
import seaborn as sns



def prepare_sales(sales):
    """
        This function takes in the gathered sales dataframe and returns a prepped dataframe
    """

    #Convert sales_date to datetime format
    sales.sale_date = pd.to_datetime(sales.sale_date)

    #plot the dists of sale_amount and item_price
    sales.sale_amount.hist()
    sales.item_price.hist()

    #Add a month and day of week column
    sales['month'] = sales.sale_date.dt.month
    sales['day_of_week'] = sales.sale_date.dt.day_name()

    #Remove the time portion of the date
    sales.sale_date = sales.sale_date.dt.date

    #Set the index to be the date and sort it
    sales = sales.set_index('sale_date').sort_index()

    #Add a sales_total column to the df
    sales['sales_total'] = sales.sale_amount * sales.item_price

    return sales

def prepare_energy(energy):
    """
        This function will take in the German Power Data dataframe and return a prepped dataframe
    """

    #Convert the Date column to a datetime format
    energy.Date = pd.to_datetime(energy.Date)

    #Add a month and a year column to dataframe
    energy['month'] = energy.Date.dt.month
    energy['year'] = energy.Date.dt.year

    #Set the Date column as the index
    energy = energy.set_index('Date').sort_index()

    #Fill missing values
    energy.Wind.fillna(0, inplace = True)
    energy.Solar.fillna(0, inplace = True)
    energy['Wind+Solar'].fillna(energy.Wind + energy.Solar, inplace = True)

    return energy

def prepare_merged_data(df):
    """
        This function will take in the merged_data dataframe and return a prepped dataframe
    """
    #Convert the Date column to a datetime format
    df.sale_date = pd.to_datetime(df.sale_date)
    
    #Add a month and a year column to dataframe
    df['month'] = df.sale_date.dt.month
    df['year'] = df.sale_date.dt.year
    
    #set datatime as index
    df = df.set_index('sale_date').sort_index()
    
    return df




