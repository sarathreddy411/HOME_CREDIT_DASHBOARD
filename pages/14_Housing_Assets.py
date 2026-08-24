import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset
df = pd.read_csv("data/application_train.csv", encoding="latin1")

st.title("🏠 Housing & Asset Analysis")
st.write("Analysis of property and vehicle ownership.")

# Calculate KPI values
car_owners = (df["FLAG_OWN_CAR"] == "Y").sum()
property_owners = (df["FLAG_OWN_REALTY"] == "Y").sum()

both_owners = (
    (df["FLAG_OWN_CAR"] == "Y") &
    (df["FLAG_OWN_REALTY"] == "Y")
).sum()

property_default_rate = (
    df[df["FLAG_OWN_REALTY"] == "Y"]["TARGET"].mean() * 100
)

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Car Owners",
    f"{car_owners:,}"
)

col2.metric(
    "Property Owners",
    f"{property_owners:,}"
)

col3.metric(
    "Customers Owning Both",
    f"{both_owners:,}"
)

col4.metric(
    "Default Rate of Property Owners",
    f"{property_default_rate:.2f}%"
)

st.divider()

# Car Ownership Distribution
st.subheader("🚗 Car Ownership Distribution")

car_data = (
    df["FLAG_OWN_CAR"]
    .value_counts()
    .reset_index()
)

car_data.columns = [
    "Car Ownership",
    "Customers"
]

fig = px.pie(
    car_data,
    names="Car Ownership",
    values="Customers",
    hole=0.4,
    title="Car Ownership Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# Property Ownership Distribution
st.subheader("🏠 Property Ownership Distribution")

property_data = (
    df["FLAG_OWN_REALTY"]
    .value_counts()
    .reset_index()
)

property_data.columns = [
    "Property Ownership",
    "Customers"
]

fig = px.pie(
    property_data,
    names="Property Ownership",
    values="Customers",
    hole=0.4,
    title="Property Ownership Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# Default Rate by Car Ownership
st.subheader("⚠️ Default Rate by Car Ownership")

car_risk = (
    df.groupby("FLAG_OWN_CAR")["TARGET"]
    .mean()
    .reset_index()
)

car_risk["Default Rate"] = car_risk["TARGET"] * 100

fig = px.bar(
    car_risk,
    x="FLAG_OWN_CAR",
    y="Default Rate",
    color="FLAG_OWN_CAR",
    text="Default Rate",
    title="Default Rate by Car Ownership"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Default Rate by Property Ownership
st.subheader("⚠️ Default Rate by Property Ownership")

property_risk = (
    df.groupby("FLAG_OWN_REALTY")["TARGET"]
    .mean()
    .reset_index()
)

property_risk["Default Rate"] = (
    property_risk["TARGET"] * 100
)

fig = px.bar(
    property_risk,
    x="FLAG_OWN_REALTY",
    y="Default Rate",
    color="FLAG_OWN_REALTY",
    text="Default Rate",
    title="Default Rate by Property Ownership"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Applicants by Housing Type
st.subheader("🏘️ Applicants by Housing Type")

housing_data = (
    df["NAME_HOUSING_TYPE"]
    .value_counts()
    .reset_index()
)

housing_data.columns = [
    "Housing Type",
    "Applicants"
]

fig = px.bar(
    housing_data,
    x="Applicants",
    y="Housing Type",
    orientation="h",
    color="Applicants",
    text="Applicants",
    title="Applicants by Housing Type"
)

fig.update_traces(
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Default Rate by Housing Type
st.subheader("🚨 Default Rate by Housing Type")

housing_risk = (
    df.groupby("NAME_HOUSING_TYPE")["TARGET"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

housing_risk["Default Rate"] = (
    housing_risk["TARGET"] * 100
)

fig = px.bar(
    housing_risk,
    x="Default Rate",
    y="NAME_HOUSING_TYPE",
    orientation="h",
    color="Default Rate",
    text="Default Rate",
    title="Default Rate by Housing Type"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Average Credit by Housing Type
st.subheader("💳 Average Credit by Housing Type")

housing_credit = (
    df.groupby("NAME_HOUSING_TYPE")["AMT_CREDIT"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

housing_credit.columns = [
    "Housing Type",
    "Average Credit"
]

fig = px.bar(
    housing_credit,
    x="Average Credit",
    y="Housing Type",
    orientation="h",
    color="Average Credit",
    text="Average Credit",
    title="Average Credit by Housing Type"
)

fig.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)