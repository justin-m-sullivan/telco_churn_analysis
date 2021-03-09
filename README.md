# telco_churn_analysis
My project repo for working through the data science pipeline with the Telco Customer Churn dataset 


## Project Description
This project seeks to answer the question: What drives customer churn at Telco?

By working through every stage of the data science pipeline (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and delivery), the project goal is to determine drivers of churn, develop a model for predicting customer churn, and deliver reccomendations and analysis.


## Project Planning
To view my process for working through the data science pipeline, check out my Trello Board.

Project Trello Board: https://trello.com/b/BjV7lF8l/telco-customer-churn-project


## Data Dictionary

| Target| Description | Data Type |
|---------|-------------|-----------|
| churn | Indicates if a customer has churned or if they are still a Telco customer | int64 |

| Categorical Features | Description | Data Type |
|---------|-------------|-----------|
|senior_citizen| indicates if the customer is a senior citizen | int64 |
dependents | indicates if the customer has dependents | int64
phone_service | indicates if the customer has phone service with Telco | int64 |
multiple_lines | indicates if the customer with phone service has multiple lines | int64 |
online_security | indicates if the customer has online security services| int 64 |
online_backup | indicates if the customer has online backup services | int64 |
device_protection | indicates if the customer has device protection services | int64 |
tech_support | indicates if the customer has tech support services | int64 |
streaming_tv | indicates if the customer has tv streaming services | int64 |
streaming_movies | indicates if the customer has movie streaming services | int64 |
paperless_billing | indicates if the customer in enrolled in paperless billing | int64 |
internet_service_type_id | indicates which internet service (if any) the customer has | int64
gender_Male | indicates the the customers' gender identity | uint8
contract_type_id | indicates the type of contract the customer has with Telco | int64|
auto_bill_pay | indicates if the customer is enrolled in auto bill pay or not | int64|

| Continuous Features | Description | Data Type |
|---------|-------------|-----------|
| tenure | Indicates how many months the customer has been with Telco | int64 |
| monthly_charges | Indicates the customer's monthly bill | float64 |
| total_charges | Indicates the total amount the customer has been charged during their tenure | float64



## Project Replication Tips

### Technical Skills
- Python
    - Pandas
    - Seaborn
    - Matplotlib
    - Numpy
    -Sklearn
    
- SQL

- Statistical Analysis
    - Descriptive Stats
    - Hypothesis Testing
        - T-test
        - Chi^2 Test
        
- Classifcation Modeling
    - Logistical Regression
    - Random Forest
    - KNN
    - Baseline Accuracy
    
### Modules
- acquire.py
- prepare.py
- explore.py



## Key Findings

- **27% of Telco customers churn**
- **Bill pay method is a driver of churn supported by the Chi^2 statistical test at 95% confidence interval**
- **Monthly Charges is a driver of churn supported by the T-test statistical test with a 95% confidence interval**
- **Model 4 is a Random Forest Classifier model devloped to predict customer churn. It performed with 80% accuracy on out of sample data, beating the basline accuracy model.**


## Reccomendations

- **1. Incentivize customers for enrolling in auto bill pay.**
- **2. Monthly charges is a driver of churn but we do not want to decrease revenue. Instead, since the majority of our customers do not currently utilize additional support services such as device protection, Telco should identfiy this as an opportunity to promote these services by offering free-trials to customers. Not only will these assist with promoting these services, but it will also improve the perceived value of the monthly charges.**