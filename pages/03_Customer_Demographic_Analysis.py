import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset
df = pd.read_csv("data/application_train.csv", encoding="latin1")

st.title("👥 Customer Demographic Analysis")
st.write("Analysis of customer demographic characteristics.")

# Calculate age and family size
df["Age"] = abs(df["DAYS_BIRTH"]) / 365

# Filters
st.sidebar.header("🔎 Filters")

gender = st.sidebar.multiselect(
    "Gender",
    df["CODE_GENDER"].dropna().unique()
)

age_range = st.sidebar.slider(
    "Age",
    18,
    70,
    (18, 70)
)

family_status = st.sidebar.multiselect(
    "Family Status",
    df["NAME_FAMILY_STATUS"].dropna().unique()
)

education = st.sidebar.multiselect(
    "Education",
    df["NAME_EDUCATION_TYPE"].dropna().unique()
)

housing = st.sidebar.multiselect(
    "Housing Type",
    df["NAME_HOUSING_TYPE"].dropna().unique()
)

# Apply filters
filtered_df = df.copy()

if gender:
    filtered_df = filtered_df[
        filtered_df["CODE_GENDER"].isin(gender)
    ]

filtered_df = filtered_df[
    (filtered_df["Age"] >= age_range[0]) &
    (filtered_df["Age"] <= age_range[1])
]

if family_status:
    filtered_df = filtered_df[
        filtered_df["NAME_FAMILY_STATUS"].isin(family_status)
    ]

if education:
    filtered_df = filtered_df[
        filtered_df["NAME_EDUCATION_TYPE"].isin(education)
    ]

if housing:
    filtered_df = filtered_df[
        filtered_df["NAME_HOUSING_TYPE"].isin(housing)
    ]

# KPI values
total_customers = len(filtered_df)
average_age = filtered_df["Age"].mean()
male_customers = (filtered_df["CODE_GENDER"] == "M").sum()
female_customers = (filtered_df["CODE_GENDER"] == "F").sum()
average_family_size = filtered_df["CNT_FAM_MEMBERS"].mean()

# KPI Cards
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("Average Age", f"{average_age:.1f}")
col3.metric("Male Customers", f"{male_customers:,}")
col4.metric("Female Customers", f"{female_customers:,}")
col5.metric("Average Family Size", f"{average_family_size:.2f}")

st.divider()

# Customers by Gender
st.subheader("👨‍👩 Customers by Gender")

data = filtered_df["CODE_GENDER"].value_counts().reset_index()
data.columns = ["Gender", "Customers"]

fig = px.bar(
    data,
    x="Gender",
    y="Customers",
    color="Gender",
    text="Customers",
    title="Customers by Gender"
)

fig.update_traces(textposition="outside")

st.plotly_chart(fig, use_container_width=True)

# Customers by Age Group
st.subheader("🎂 Customers by Age Group")

filtered_df["Age Group"] = pd.cut(
    filtered_df["Age"],
    bins=[18, 25, 30, 35, 40, 45, 50, 55, 60, float("inf")],
    labels=[
        "18-25",
        "26-30",
        "31-35",
        "36-40",
        "41-45",
        "46-50",
        "51-55",
        "56-60",
        "61+"
    ]
)

age_data = (
    filtered_df["Age Group"]
    .value_counts()
    .sort_index()
    .reset_index()
)

age_data.columns = ["Age Group", "Customers"]

fig = px.bar(
    age_data,
    x="Age Group",
    y="Customers",
    color="Age Group",
    text="Customers",
    title="Customers by Age Group"
)

st.plotly_chart(fig, use_container_width=True)

# Family Status
st.subheader("🏠 Customers by Family Status")

data = (
    filtered_df["NAME_FAMILY_STATUS"]
    .value_counts()
    .reset_index()
)

data.columns = ["Family Status", "Customers"]

fig = px.bar(
    data,
    x="Family Status",
    y="Customers",
    color="Family Status",
    text="Customers",
    title="Customers by Family Status"
)

st.plotly_chart(fig, use_container_width=True)

# Education
st.subheader("🎓 Customers by Education")

data = (
    filtered_df["NAME_EDUCATION_TYPE"]
    .value_counts()
    .reset_index()
)

data.columns = ["Education", "Customers"]

fig = px.bar(
    data,
    x="Education",
    y="Customers",
    color="Education",
    text="Customers",
    title="Customers by Education"
)

st.plotly_chart(fig, use_container_width=True)

# Housing
st.subheader("🏠 Customers by Housing Type")

data = (
    filtered_df["NAME_HOUSING_TYPE"]
    .value_counts()
    .reset_index()
)

data.columns = ["Housing Type", "Customers"]

fig = px.bar(
    data,
    x="Housing Type",
    y="Customers",
    color="Housing Type",
    text="Customers",
    title="Customers by Housing Type"
)

st.plotly_chart(fig, use_container_width=True)

# Default Rate by Demographic Group
st.subheader("⚠️ Default Rate by Gender")

risk = (
    filtered_df.groupby("CODE_GENDER")["TARGET"]
    .mean()
    .reset_index()
)

risk["Default Rate"] = risk["TARGET"] * 100

fig = px.bar(
    risk,
    x="CODE_GENDER",
    y="Default Rate",
    color="CODE_GENDER",
    text="Default Rate",
    title="Default Rate by Gender"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)