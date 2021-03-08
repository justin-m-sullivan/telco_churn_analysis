import numpy as np
import pandas as pd
import os
from env import host, user, password

def prep_data(df):
    '''
    This function takes in the telco data frame and prepares it for analysis by:


    '''
    #Convert strings in features that do not match "yes" or "no"
    df.replace({'No internet service': 'No', 'No phone service':'No'}, inplace=True)

    #Convert features with yes or no to 0s and 1s
    df.replace({'Yes': 1, 'No': 0}, inplace=True)

    #Group payment_type_id in two subgroups(auto pay vs manual pay) with booleans (True = auto_pay)
    df.payment_type_id.replace({1: 0, 2: 0, 3: 1, 4: 1}, inplace=True)

    #Rename payment_type_id columns to auto_bill_pay 
    df.rename(columns={'payment_type_id': 'auto_bill_pay'}, inplace=True)

    
    #Columns to encode
    cols_to_encode = ['gender', 'contract_type', 'internet_service_type']

    #Encode
    dummies = pd.get_dummies(df[cols_to_encode], drop_first=[True])

    #Concat dummies to original df
    df = pd.concat([df, dummies], axis=1)

    #Columns to drop
    cols_to_drop = ['internet_service_type_id', 'contract_type_id', 
    'gender','internet_service_type', 'contract_type', 'payment_type', 'customer_id']

    #drop columns
    df.drop(columns=cols_to_drop, inplace=True)

    #Fill empty values in total_charges column where tenure is less than 1 month
    df.total_charges = df.total_charges.replace(' ', 0.0)

    #Convert total_charges to float
    df.total_charges = df.total_charges.astype('float64')

    #Replace 0s in total charges with monthly charge
    df.total_charges = np.where(df.total_charges==0.0, df.monthly_charges , df.total_charges)

    return df
