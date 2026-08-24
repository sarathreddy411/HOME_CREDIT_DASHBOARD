def get_basic_kpis(df):
    return {
        "total_applications": len(df),
        "default_customers": (df["TARGET"] == 1).sum(),
        "non_default_customers": (df["TARGET"] == 0).sum(),
        "default_rate": df["TARGET"].mean() * 100,
        "total_credit": df["AMT_CREDIT"].sum(),
        "average_credit": df["AMT_CREDIT"].mean(),
        "average_income": df["AMT_INCOME_TOTAL"].mean(),
        "average_annuity": df["AMT_ANNUITY"].mean()
    }