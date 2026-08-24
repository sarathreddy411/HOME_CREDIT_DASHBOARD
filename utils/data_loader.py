import pandas as pd
def load_data():
    return pd.read_csv(r"D:\Assignments\home_credit_dashboard\data\application_train.csv", encoding="latin1")