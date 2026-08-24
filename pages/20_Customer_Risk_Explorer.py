import streamlit as st
import pandas as pd

# Read the dataset
df = pd.read_csv("data/application_train.csv", encoding="latin1")

st.title("🔎 Customer Risk Explorer")
st.write("Explore individual customers and filtered applicant records.")

# Create calculated features
df["Age"] = abs(df["DAYS_BIRTH"]) / 365
df["Employment_Years"] = abs(
    df["DAYS_EMPLOYED"].replace(365243, pd.NA)
) / 365

df["Credit_Income_Ratio"] = (
    df["AMT_CREDIT"] / df["AMT_INCOME_TOTAL"]
)

df["Annuity_Income_Ratio"] = (
    df["AMT_ANNUITY"] / df["AMT_INCOME_TOTAL"]
)

df["Credit_Goods_Ratio"] = (
    df["AMT_CREDIT"] / df["AMT_GOODS_PRICE"]
)

df["Average_External_Score"] = df[
    ["EXT_SOURCE_1", "EXT_SOURCE_2", "EXT_SOURCE_3"]
].mean(axis=1)

# Search Customer
st.subheader("🔍 Search Customer")

customer_id = st.number_input(
    "Enter Customer ID",
    min_value=0,
    step=1
)

search_button = st.button("Search")

# Filters
st.subheader("🎛️ Filters")

col1, col2, col3 = st.columns(3)

with col1:
    target_filter = st.selectbox(
        "TARGET",
        ["All", "Non-Default", "Default"]
    )

    gender_filter = st.selectbox(
        "Gender",
        ["All"] + sorted(df["CODE_GENDER"].dropna().unique().tolist())
    )

    income_type_filter = st.selectbox(
        "Income Type",
        ["All"] + sorted(
            df["NAME_INCOME_TYPE"].dropna().unique().tolist()
        )
    )

with col2:
    education_filter = st.selectbox(
        "Education",
        ["All"] + sorted(
            df["NAME_EDUCATION_TYPE"].dropna().unique().tolist()
        )
    )

    occupation_filter = st.selectbox(
        "Occupation",
        ["All"] + sorted(
            df["OCCUPATION_TYPE"].dropna().unique().tolist()
        )
    )

    contract_filter = st.selectbox(
        "Contract Type",
        ["All"] + sorted(
            df["NAME_CONTRACT_TYPE"].dropna().unique().tolist()
        )
    )

with col3:
    housing_filter = st.selectbox(
        "Housing Type",
        ["All"] + sorted(
            df["NAME_HOUSING_TYPE"].dropna().unique().tolist()
        )
    )

    car_filter = st.selectbox(
        "Car Ownership",
        ["All", "Y", "N"]
    )

    property_filter = st.selectbox(
        "Property Ownership",
        ["All", "Y", "N"]
    )

# Age, Income and Credit Filters
col1, col2, col3 = st.columns(3)

with col1:
    age_range = st.slider(
        "Age Range",
        18,
        70,
        (18, 70)
    )

with col2:
    income_range = st.slider(
        "Income Range",
        float(df["AMT_INCOME_TOTAL"].min()),
        float(df["AMT_INCOME_TOTAL"].max()),
        (
            float(df["AMT_INCOME_TOTAL"].min()),
            float(df["AMT_INCOME_TOTAL"].max())
        )
    )

with col3:
    credit_range = st.slider(
        "Credit Range",
        float(df["AMT_CREDIT"].min()),
        float(df["AMT_CREDIT"].max()),
        (
            float(df["AMT_CREDIT"].min()),
            float(df["AMT_CREDIT"].max())
        )
    )

# Apply filters
filtered_df = df.copy()

if target_filter != "All":
    target_value = 1 if target_filter == "Default" else 0
    filtered_df = filtered_df[
        filtered_df["TARGET"] == target_value
    ]

if gender_filter != "All":
    filtered_df = filtered_df[
        filtered_df["CODE_GENDER"] == gender_filter
    ]

if income_type_filter != "All":
    filtered_df = filtered_df[
        filtered_df["NAME_INCOME_TYPE"] == income_type_filter
    ]

if education_filter != "All":
    filtered_df = filtered_df[
        filtered_df["NAME_EDUCATION_TYPE"] == education_filter
    ]

if occupation_filter != "All":
    filtered_df = filtered_df[
        filtered_df["OCCUPATION_TYPE"] == occupation_filter
    ]

if contract_filter != "All":
    filtered_df = filtered_df[
        filtered_df["NAME_CONTRACT_TYPE"] == contract_filter
    ]

if housing_filter != "All":
    filtered_df = filtered_df[
        filtered_df["NAME_HOUSING_TYPE"] == housing_filter
    ]

if car_filter != "All":
    filtered_df = filtered_df[
        filtered_df["FLAG_OWN_CAR"] == car_filter
    ]

if property_filter != "All":
    filtered_df = filtered_df[
        filtered_df["FLAG_OWN_REALTY"] == property_filter
    ]

filtered_df = filtered_df[
    (filtered_df["Age"] >= age_range[0]) &
    (filtered_df["Age"] <= age_range[1]) &
    (filtered_df["AMT_INCOME_TOTAL"] >= income_range[0]) &
    (filtered_df["AMT_INCOME_TOTAL"] <= income_range[1]) &
    (filtered_df["AMT_CREDIT"] >= credit_range[0]) &
    (filtered_df["AMT_CREDIT"] <= credit_range[1])
]

# Customer Risk Profile
if search_button:
    customer = df[df["SK_ID_CURR"] == customer_id]

    if not customer.empty:
        st.subheader("👤 Customer Risk Profile")

        customer = customer.iloc[0]

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Customer ID",
            int(customer["SK_ID_CURR"])
        )

        col2.metric(
            "TARGET",
            "Default" if customer["TARGET"] == 1 else "Non-Default"
        )

        col3.metric(
            "Age",
            f"{customer['Age']:.1f} Years"
        )

        col4.metric(
            "Gender",
            customer["CODE_GENDER"]
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Income",
            f"{customer['AMT_INCOME_TOTAL']:,.0f}"
        )

        col2.metric(
            "Credit Amount",
            f"{customer['AMT_CREDIT']:,.0f}"
        )

        col3.metric(
            "Annuity",
            f"{customer['AMT_ANNUITY']:,.0f}"
        )

        profile = pd.DataFrame({
            "Feature": [
                "Education",
                "Occupation",
                "Family Status",
                "Number of Children",
                "Housing Type",
                "External Score 1",
                "External Score 2",
                "External Score 3"
            ],
            "Value": [
                customer["NAME_EDUCATION_TYPE"],
                customer["OCCUPATION_TYPE"],
                customer["NAME_FAMILY_STATUS"],
                customer["CNT_CHILDREN"],
                customer["NAME_HOUSING_TYPE"],
                customer["EXT_SOURCE_1"],
                customer["EXT_SOURCE_2"],
                customer["EXT_SOURCE_3"]
            ]
        })

        st.dataframe(
            profile,
            use_container_width=True,
            hide_index=True
        )

        st.subheader("⚠️ Calculated Risk Indicators")

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric(
            "Credit-to-Income",
            f"{customer['Credit_Income_Ratio']:.2f}"
        )

        col2.metric(
            "Annuity-to-Income",
            f"{customer['Annuity_Income_Ratio']:.2f}"
        )

        col3.metric(
            "Credit-to-Goods",
            f"{customer['Credit_Goods_Ratio']:.2f}"
        )

        col4.metric(
            "Employment Years",
            f"{customer['Employment_Years']:.1f}"
        )

        col5.metric(
            "Average External Score",
            f"{customer['Average_External_Score']:.2f}"
        )

    else:
        st.warning("Customer ID not found.")

# Filtered Applicant Records
st.subheader("📋 Filtered Applicant Records")

st.write(
    f"Showing {len(filtered_df):,} customers"
)

display_columns = [
    "SK_ID_CURR",
    "TARGET",
    "Age",
    "CODE_GENDER",
    "AMT_INCOME_TOTAL",
    "AMT_CREDIT",
    "AMT_ANNUITY",
    "NAME_EDUCATION_TYPE",
    "OCCUPATION_TYPE",
    "NAME_FAMILY_STATUS",
    "CNT_CHILDREN",
    "NAME_HOUSING_TYPE",
    "Credit_Income_Ratio",
    "Annuity_Income_Ratio",
    "Credit_Goods_Ratio",
    "Employment_Years",
    "Average_External_Score"
]

st.dataframe(
    filtered_df[display_columns].head(1000),
    use_container_width=True,
    hide_index=True
)