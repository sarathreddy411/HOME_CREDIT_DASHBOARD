import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset
df = pd.read_csv("data/application_train.csv", encoding="latin1")

# Page title
st.title("🎓 Education Analysis")
st.write("Analysis of applicants based on education level.")

# Calculate education metrics
education_count = df["NAME_EDUCATION_TYPE"].value_counts()

education_income = (
    df.groupby("NAME_EDUCATION_TYPE")["AMT_INCOME_TOTAL"]
    .mean()
    .sort_values(ascending=False)
)

education_default = (
    df.groupby("NAME_EDUCATION_TYPE")["TARGET"]
    .mean()
    .sort_values()
)

# Calculate credit-to-income ratio
df["Credit_Income_Ratio"] = (
    df["AMT_CREDIT"] / df["AMT_INCOME_TOTAL"]
)

education_ratio = (
    df.groupby("NAME_EDUCATION_TYPE")["Credit_Income_Ratio"]
    .mean()
    .sort_values(ascending=False)
)

# KPI Cards
most_common_education = education_count.idxmax()
highest_income_education = education_income.idxmax()
lowest_default_education = education_default.idxmin()
highest_default_education = education_default.idxmax()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Most Common Education",
    most_common_education
)

col2.metric(
    "Highest Income Education",
    highest_income_education
)

col3.metric(
    "Lowest Default Education",
    lowest_default_education
)

col4.metric(
    "Highest Default Education",
    highest_default_education
)

st.divider()

# Customers by Education
st.subheader("👥 Customers by Education")

education_data = education_count.reset_index()
education_data.columns = ["Education", "Customers"]

fig = px.bar(
    education_data,
    x="Education",
    y="Customers",
    color="Education",
    text="Customers",
    title="Customers by Education"
)

fig.update_traces(
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Default Rate by Education
st.subheader("⚠️ Default Rate by Education")

default_data = education_default.reset_index()
default_data.columns = ["Education", "Default Rate"]

default_data["Default Rate"] = (
    default_data["Default Rate"] * 100
)

fig = px.bar(
    default_data,
    x="Education",
    y="Default Rate",
    color="Default Rate",
    text="Default Rate",
    title="Default Rate by Education"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Income by Education
st.subheader("💰 Income by Education")

income_data = education_income.reset_index()
income_data.columns = ["Education", "Average Income"]

fig = px.bar(
    income_data,
    x="Average Income",
    y="Education",
    orientation="h",
    color="Average Income",
    text="Average Income",
    title="Average Income by Education"
)

fig.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Credit by Education
st.subheader("💳 Credit by Education")

credit_data = (
    df.groupby("NAME_EDUCATION_TYPE")["AMT_CREDIT"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

credit_data.columns = [
    "Education",
    "Average Credit"
]

fig = px.bar(
    credit_data,
    x="Average Credit",
    y="Education",
    orientation="h",
    color="Average Credit",
    text="Average Credit",
    title="Average Credit by Education"
)

fig.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Annuity by Education
st.subheader("💵 Annuity by Education")

annuity_data = (
    df.groupby("NAME_EDUCATION_TYPE")["AMT_ANNUITY"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

annuity_data.columns = [
    "Education",
    "Average Annuity"
]

fig = px.bar(
    annuity_data,
    x="Average Annuity",
    y="Education",
    orientation="h",
    color="Average Annuity",
    text="Average Annuity",
    title="Average Annuity by Education"
)

fig.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Credit-to-Income Ratio by Education
st.subheader("📊 Credit-to-Income Ratio by Education")

ratio_data = education_ratio.reset_index()
ratio_data.columns = [
    "Education",
    "Credit-to-Income Ratio"
]

fig = px.bar(
    ratio_data,
    x="Credit-to-Income Ratio",
    y="Education",
    orientation="h",
    color="Credit-to-Income Ratio",
    text="Credit-to-Income Ratio",
    title="Credit-to-Income Ratio by Education"
)

fig.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)