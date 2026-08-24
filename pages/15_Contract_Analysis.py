import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset
df = pd.read_csv("data/application_train.csv", encoding="latin1")

st.title("📄 Contract Type Analysis")
st.write("Analysis of credit applications according to loan contract type.")

# Calculate KPI values
cash_applications = (
    df["NAME_CONTRACT_TYPE"] == "Cash loans"
).sum()

revolving_applications = (
    df["NAME_CONTRACT_TYPE"] == "Revolving loans"
).sum()

cash_default_rate = (
    df[df["NAME_CONTRACT_TYPE"] == "Cash loans"]["TARGET"].mean() * 100
)

revolving_default_rate = (
    df[df["NAME_CONTRACT_TYPE"] == "Revolving loans"]["TARGET"].mean() * 100
)

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Cash Loan Applications",
    f"{cash_applications:,}"
)

col2.metric(
    "Revolving Loan Applications",
    f"{revolving_applications:,}"
)

col3.metric(
    "Cash Loan Default Rate",
    f"{cash_default_rate:.2f}%"
)

col4.metric(
    "Revolving Loan Default Rate",
    f"{revolving_default_rate:.2f}%"
)

st.divider()

# Applications by Contract Type
st.subheader("📊 Applications by Contract Type")

contract_count = (
    df["NAME_CONTRACT_TYPE"]
    .value_counts()
    .reset_index()
)

contract_count.columns = [
    "Contract Type",
    "Applications"
]

fig = px.bar(
    contract_count,
    x="Contract Type",
    y="Applications",
    color="Contract Type",
    text="Applications",
    title="Applications by Contract Type"
)

fig.update_traces(
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Default Rate by Contract Type
st.subheader("⚠️ Default Rate by Contract Type")

contract_default = (
    df.groupby("NAME_CONTRACT_TYPE")["TARGET"]
    .mean()
    .reset_index()
)

contract_default["Default Rate"] = (
    contract_default["TARGET"] * 100
)

fig = px.bar(
    contract_default,
    x="NAME_CONTRACT_TYPE",
    y="Default Rate",
    color="Default Rate",
    text="Default Rate",
    title="Default Rate by Contract Type"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Average Credit by Contract Type
st.subheader("💳 Average Credit by Contract Type")

contract_credit = (
    df.groupby("NAME_CONTRACT_TYPE")["AMT_CREDIT"]
    .mean()
    .reset_index()
)

fig = px.bar(
    contract_credit,
    x="NAME_CONTRACT_TYPE",
    y="AMT_CREDIT",
    color="NAME_CONTRACT_TYPE",
    text="AMT_CREDIT",
    title="Average Credit by Contract Type"
)

fig.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Average Income by Contract Type
st.subheader("💰 Average Income by Contract Type")

contract_income = (
    df.groupby("NAME_CONTRACT_TYPE")["AMT_INCOME_TOTAL"]
    .mean()
    .reset_index()
)

fig = px.bar(
    contract_income,
    x="NAME_CONTRACT_TYPE",
    y="AMT_INCOME_TOTAL",
    color="NAME_CONTRACT_TYPE",
    text="AMT_INCOME_TOTAL",
    title="Average Income by Contract Type"
)

fig.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Average Annuity by Contract Type
st.subheader("💵 Average Annuity by Contract Type")

contract_annuity = (
    df.groupby("NAME_CONTRACT_TYPE")["AMT_ANNUITY"]
    .mean()
    .reset_index()
)

fig = px.bar(
    contract_annuity,
    x="NAME_CONTRACT_TYPE",
    y="AMT_ANNUITY",
    color="NAME_CONTRACT_TYPE",
    text="AMT_ANNUITY",
    title="Average Annuity by Contract Type"
)

fig.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Credit-to-Income Ratio by Contract Type
st.subheader("📈 Credit-to-Income Ratio by Contract Type")

df["Credit_Income_Ratio"] = (
    df["AMT_CREDIT"] / df["AMT_INCOME_TOTAL"]
)

contract_ratio = (
    df.groupby("NAME_CONTRACT_TYPE")["Credit_Income_Ratio"]
    .mean()
    .reset_index()
)

fig = px.bar(
    contract_ratio,
    x="NAME_CONTRACT_TYPE",
    y="Credit_Income_Ratio",
    color="NAME_CONTRACT_TYPE",
    text="Credit_Income_Ratio",
    title="Credit-to-Income Ratio by Contract Type"
)

fig.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)