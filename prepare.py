def prep_data(df):
    '''
    This function takes in the telco data frame and prepares it for analysis by:


    '''
    #Convert strings in features that do not match "yes" or "no"
    df.replace({'No internet service': 'No', 'No phone service':'No'}, inplace=True)

    #Convert features with yes or no to 0s and 1s
    df.replace({'Yes': 1, 'No': 0}, inplace=True)

    #Columns to encode
    cols_to_encode = ['gender', 'contract_type', 'payment_type']

    #Encode
    dummies = pd.get_dummies(telco[cols_to_encode], drop_first=[True])

    #Concat dummies to original df
    df = pd.concat([telco, dummies], axis=1)

    #Columns to drop
    cols_to_drop = ['internet_service_type_id', 'contract_type_id', 'payment_type_id', 
    'gender','internet_service_type', 'contract_type', 'payment_type', 'customer_id']

    #drop columns
    df.drop(columns=cols_to_drop, inplace=True)

    #Fill empty values in total_charges column where tenure is less than 1 month
    df.total_charges = df.total_charges.replace(' ', 0.0)

    #Convert total_charges to float
    df.total_charges = df.total_charges.astype('float64')

    return df