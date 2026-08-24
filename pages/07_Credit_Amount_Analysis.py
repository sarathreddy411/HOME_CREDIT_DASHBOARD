import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("data/application_train.csv", encoding="latin1")

st.title("💳 Credit Amount Analysis")
st.write("Analysis of credit requested by applicants.")

# Calculate KPIs
total_credit = df["AMT_CREDIT"].sum()
average_credit = df["AMT_CREDIT"].mean()
median_credit = df["AMT_CREDIT"].median()
maximum_credit = df["AMT_CREDIT"].max()
minimum_credit = df["AMT_CREDIT"].min()

# Create credit groups
df["Credit Group"] = pd.cut(
    df["AMT_CREDIT"],
    bins=[0, 100000, 300000, 500000, 700000, 1000000, float("inf")],
    labels=[
        "Below 100K",
        "100K-300K",
        "300K-500K",
        "500K-700K",
        "700K-1M",
        "Above 1M"
    ]
)

# KPI Cards
col1, col2, col3 = st.columns(3)

col1.metric("Total Credit", f"{total_credit:,.0f}")
col2.metric("Average Credit", f"{average_credit:,.0f}")
col3.metric("Median Credit", f"{median_credit:,.0f}")

col1, col2 = st.columns(2)

col1.metric("Maximum Credit", f"{maximum_credit:,.0f}")
col2.metric("Minimum Credit", f"{minimum_credit:,.0f}")

st.divider()

# Credit Distribution
st.subheader("📊 Credit Amount Distribution")

fig, ax = plt.subplots(figsize=(8, 4))

sns.histplot(
    df["AMT_CREDIT"],
    bins=40,
    kde=True,
    ax=ax
)

ax.set_xlabel("Credit Amount")
ax.set_ylabel("Customers")

st.pyplot(fig)

# Credit Amount by TARGET
st.subheader("🎯 Credit Amount by TARGET")

fig = px.box(
    df,
    x="TARGET",
    y="AMT_CREDIT",
    color="TARGET",
    title="Credit Amount by TARGET"
)

st.plotly_chart(fig, use_container_width=True)

# Average Credit by Gender
st.subheader("👥 Average Credit by Gender")

gender_credit = (
    df.groupby("CODE_GENDER")["AMT_CREDIT"]
    .mean()
    .reset_index()
)

fig = px.bar(
    gender_credit,
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

# Credit by Income Type
st.subheader("💼 Credit by Income Type")

income_credit = (
    df.groupby("NAME_INCOME_TYPE")["AMT_CREDIT"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

fig = px.bar(
    income_credit,
    x="AMT_CREDIT",
    y="NAME_INCOME_TYPE",
    orientation="h",
    color="AMT_CREDIT",
    text="AMT_CREDIT",
    title="Average Credit by Income Type"
)

fig.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Credit by Education
st.subheader("🎓 Credit by Education")

education_credit = (
    df.groupby("NAME_EDUCATION_TYPE")["AMT_CREDIT"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

fig = px.bar(
    education_credit,
    x="AMT_CREDIT",
    y="NAME_EDUCATION_TYPE",
    orientation="h",
    color="AMT_CREDIT",
    text="AMT_CREDIT",
    title="Average Credit by Education"
)

fig.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Credit by Contract Type
st.subheader("📄 Credit by Contract Type")

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

# Default Rate by Credit Range
st.subheader("⚠️ Default Rate by Credit Range")

credit_risk = (
    df.groupby("Credit Group", observed=False)["TARGET"]
    .mean()
    .reset_index()
)

credit_risk["Default Rate"] = credit_risk["TARGET"] * 100

fig = px.bar(
    credit_risk,
    x="Credit Group",
    y="Default Rate",
    color="Default Rate",
    text="Default Rate",
    title="Default Rate by Credit Range"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)