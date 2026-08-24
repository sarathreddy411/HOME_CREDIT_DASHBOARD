import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset
df = pd.read_csv("data/application_train.csv", encoding="latin1")

st.title("👥 Gender Analysis")
st.write("Comparison of credit characteristics across genders.")

# Calculate KPIs
male = df[df["CODE_GENDER"] == "M"]
female = df[df["CODE_GENDER"] == "F"]

male_count = len(male)
female_count = len(female)

male_default_rate = male["TARGET"].mean() * 100
female_default_rate = female["TARGET"].mean() * 100

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Male Applicants", f"{male_count:,}")
col2.metric("Female Applicants", f"{female_count:,}")
col3.metric("Male Default Rate", f"{male_default_rate:.2f}%")
col4.metric("Female Default Rate", f"{female_default_rate:.2f}%")

st.divider()

# Applicants by Gender
st.subheader("👥 Applicants by Gender")

gender_count = (
    df["CODE_GENDER"]
    .value_counts()
    .reset_index()
)

gender_count.columns = ["Gender", "Customers"]

fig = px.bar(
    gender_count,
    x="Gender",
    y="Customers",
    color="Gender",
    text="Customers",
    title="Applicants by Gender"
)

st.plotly_chart(fig, use_container_width=True)

# Default Customers by Gender
st.subheader("🚨 Default Customers by Gender")

default_gender = (
    df[df["TARGET"] == 1]["CODE_GENDER"]
    .value_counts()
    .reset_index()
)

default_gender.columns = ["Gender", "Defaults"]

fig = px.bar(
    default_gender,
    x="Gender",
    y="Defaults",
    color="Gender",
    text="Defaults",
    title="Default Customers by Gender"
)

st.plotly_chart(fig, use_container_width=True)

# Default Rate by Gender
st.subheader("⚠️ Default Rate by Gender")

gender_risk = (
    df.groupby("CODE_GENDER")["TARGET"]
    .mean()
    .reset_index()
)

gender_risk["Default Rate"] = gender_risk["TARGET"] * 100

fig = px.bar(
    gender_risk,
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

# Average Income
st.subheader("💰 Average Income by Gender")

income_gender = (
    df.groupby("CODE_GENDER")["AMT_INCOME_TOTAL"]
    .mean()
    .reset_index()
)

fig = px.bar(
    income_gender,
    x="CODE_GENDER",
    y="AMT_INCOME_TOTAL",
    color="CODE_GENDER",
    text="AMT_INCOME_TOTAL",
    title="Average Income by Gender"
)

fig.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Average Credit
st.subheader("💳 Average Credit by Gender")

credit_gender = (
    df.groupby("CODE_GENDER")["AMT_CREDIT"]
    .mean()
    .reset_index()
)

fig = px.bar(
    credit_gender,
    x="CODE_GENDER",
    y="AMT_CREDIT",
    color="CODE_GENDER",
    text="AMT_CREDIT",
    title="Average Credit by Gender"
)

fig.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Average Annuity
st.subheader("💵 Average Annuity by Gender")

annuity_gender = (
    df.groupby("CODE_GENDER")["AMT_ANNUITY"]
    .mean()
    .reset_index()
)

fig = px.bar(
    annuity_gender,
    x="CODE_GENDER",
    y="AMT_ANNUITY",
    color="CODE_GENDER",
    text="AMT_ANNUITY",
    title="Average Annuity by Gender"
)

fig.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Comparison Table
st.subheader("📋 Gender Comparison")

comparison = (
    df.groupby("CODE_GENDER")
    .agg(
        Customers=("TARGET", "count"),
        Defaults=("TARGET", "sum"),
        Default_Rate=("TARGET", "mean"),
        Avg_Income=("AMT_INCOME_TOTAL", "mean"),
        Avg_Credit=("AMT_CREDIT", "mean")
    )
    .reset_index()
)

comparison["Default Rate"] = comparison["Default_Rate"] * 100

comparison = comparison.drop(columns=["Default_Rate"])

st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
)