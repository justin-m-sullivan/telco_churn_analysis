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
    This function reads in telco data from Codeup database and writes data to
    a csv file, returns df.
    '''
    filename = 'telco.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)

    else:
        #Read fresh data from db into a DataFrame.
        df = pd.read_sql('''
            SELECT *
            FROM customers
            JOIN internet_service_types USING (internet_service_type_id)
            JOIN contract_types USING(contract_type_id)
            JOIN payment_types USING (payment_type_id);
            ''', 
            get_connection('telco_churn'))
        
        #Write DataFrame to a csv file.
        df.to_csv(filename)
          
    return df