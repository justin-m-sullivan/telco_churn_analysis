import numpy as np
import pandas as pd
import os
from env import host, user, password

def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the CodeUp db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


def get_telco_data():
    '''
    This function reads in telco data from Codeup database.
    It joins the tables internet_service_types, contract_types,
    and payment types on customers table to return a single dataframe
    '''

    df = pd.read_sql('''
            SELECT *
            FROM customers
            JOIN internet_service_types USING (internet_service_type_id)
            JOIN contract_types USING(contract_type_id)
            JOIN payment_types USING (payment_type_id);
            ''', 
            get_connection('telco_churn'))
          
    return df