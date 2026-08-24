def clean_data(df):
    df = df.copy()
    df["DAYS_EMPLOYED"] = df["DAYS_EMPLOYED"].replace(365243, float("nan"))
    return df