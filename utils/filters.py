import streamlit as st

def apply_filters(df):
    filtered_df = df.copy()

    st.sidebar.header("🔎 Filters")

    gender = st.sidebar.multiselect(
        "Gender",
        df["CODE_GENDER"].dropna().unique()
    )

    education = st.sidebar.multiselect(
        "Education",
        df["NAME_EDUCATION_TYPE"].dropna().unique()
    )

    income_type = st.sidebar.multiselect(
        "Income Type",
        df["NAME_INCOME_TYPE"].dropna().unique()
    )

    if gender:
        filtered_df = filtered_df[
            filtered_df["CODE_GENDER"].isin(gender)
        ]

    if education:
        filtered_df = filtered_df[
            filtered_df["NAME_EDUCATION_TYPE"].isin(education)
        ]

    if income_type:
        filtered_df = filtered_df[
            filtered_df["NAME_INCOME_TYPE"].isin(income_type)
        ]

    return filtered_df