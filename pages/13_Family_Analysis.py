import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset
df = pd.read_csv("data/application_train.csv", encoding="latin1")

st.title("👨‍👩‍👧 Family & Children Analysis")
st.write("Analysis of household characteristics and credit risk.")

# Calculate family metrics
average_children = df["CNT_CHILDREN"].mean()
average_family_members = df["CNT_FAM_MEMBERS"].mean()

customers_with_children = (
    df["CNT_CHILDREN"] > 0
).sum()

customers_without_children = (
    df["CNT_CHILDREN"] == 0
).sum()

# Calculate default rate by family status
family_status_risk = (
    df.groupby("NAME_FAMILY_STATUS")["TARGET"]
    .mean()
    .sort_values(ascending=False)
)

highest_risk_family = family_status_risk.idxmax()

# KPI Cards
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Average Children",
    f"{average_children:.2f}"
)

col2.metric(
    "Average Family Members",
    f"{average_family_members:.2f}"
)

col3.metric(
    "Customers with Children",
    f"{customers_with_children:,}"
)

col4.metric(
    "Customers without Children",
    f"{customers_without_children:,}"
)

col5.metric(
    "Highest Risk Family Type",
    highest_risk_family
)

st.divider()

# Customers by Number of Children
st.subheader("👶 Customers by Number of Children")

children_data = (
    df["CNT_CHILDREN"]
    .value_counts()
    .sort_index()
    .reset_index()
)

children_data.columns = [
    "Children",
    "Customers"
]

fig = px.bar(
    children_data,
    x="Children",
    y="Customers",
    color="Children",
    text="Customers",
    title="Customers by Number of Children"
)

fig.update_traces(
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Default Rate by Number of Children
st.subheader("⚠️ Default Rate by Number of Children")

children_risk = (
    df.groupby("CNT_CHILDREN")["TARGET"]
    .mean()
    .reset_index()
)

children_risk["Default Rate"] = (
    children_risk["TARGET"] * 100
)

fig = px.bar(
    children_risk,
    x="CNT_CHILDREN",
    y="Default Rate",
    color="Default Rate",
    text="Default Rate",
    title="Default Rate by Number of Children"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Customers by Family Size
st.subheader("👨‍👩‍👧 Customers by Family Size")

family_size = (
    df["CNT_FAM_MEMBERS"]
    .value_counts()
    .sort_index()
    .reset_index()
)

family_size.columns = [
    "Family Members",
    "Customers"
]

fig = px.bar(
    family_size,
    x="Family Members",
    y="Customers",
    color="Family Members",
    text="Customers",
    title="Customers by Family Size"
)

fig.update_traces(
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Default Rate by Family Size
st.subheader("⚠️ Default Rate by Family Size")

family_size_risk = (
    df.groupby("CNT_FAM_MEMBERS")["TARGET"]
    .mean()
    .reset_index()
)

family_size_risk["Default Rate"] = (
    family_size_risk["TARGET"] * 100
)

fig = px.bar(
    family_size_risk,
    x="CNT_FAM_MEMBERS",
    y="Default Rate",
    color="Default Rate",
    text="Default Rate",
    title="Default Rate by Family Size"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Applications by Family Status
st.subheader("🏠 Applications by Family Status")

family_status = (
    df["NAME_FAMILY_STATUS"]
    .value_counts()
    .reset_index()
)

family_status.columns = [
    "Family Status",
    "Applications"
]

fig = px.bar(
    family_status,
    x="Family Status",
    y="Applications",
    color="Family Status",
    text="Applications",
    title="Applications by Family Status"
)

fig.update_traces(
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Default Rate by Family Status
st.subheader("🚨 Default Rate by Family Status")

family_status_data = (
    df.groupby("NAME_FAMILY_STATUS")["TARGET"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

family_status_data["Default Rate"] = (
    family_status_data["TARGET"] * 100
)

fig = px.bar(
    family_status_data,
    x="Default Rate",
    y="NAME_FAMILY_STATUS",
    orientation="h",
    color="Default Rate",
    text="Default Rate",
    title="Default Rate by Family Status"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Income vs Family Size
st.subheader("💰 Income vs Family Size")

family_income = (
    df.groupby("CNT_FAM_MEMBERS")["AMT_INCOME_TOTAL"]
    .mean()
    .reset_index()
)

fig = px.bar(
    family_income,
    x="CNT_FAM_MEMBERS",
    y="AMT_INCOME_TOTAL",
    color="CNT_FAM_MEMBERS",
    text="AMT_INCOME_TOTAL",
    title="Average Income by Family Size"
)

fig.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside"
)

fig.update_layout(
    xaxis_title="Family Members",
    yaxis_title="Average Income"
)

st.plotly_chart(fig, use_container_width=True)