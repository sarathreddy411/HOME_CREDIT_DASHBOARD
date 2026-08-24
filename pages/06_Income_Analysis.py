import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("data/application_train.csv", encoding="latin1")

st.title("💰 Income Analysis")
st.write("Analysis of customer income and credit risk.")

# Calculate KPIs
total_income = df["AMT_INCOME_TOTAL"].sum()
average_income = df["AMT_INCOME_TOTAL"].mean()
median_income = df["AMT_INCOME_TOTAL"].median()
maximum_income = df["AMT_INCOME_TOTAL"].max()
default_income = df[df["TARGET"] == 1]["AMT_INCOME_TOTAL"].mean()

# Create income groups
df["Income Group"] = pd.cut(
    df["AMT_INCOME_TOTAL"],
    bins=[0, 50000, 100000, 150000, 200000, 300000, 500000, float("inf")],
    labels=[
        "Below 50K",
        "50K-100K",
        "100K-150K",
        "150K-200K",
        "200K-300K",
        "300K-500K",
        "Above 500K"
    ]
)

# KPI Cards
col1, col2, col3 = st.columns(3)

col1.metric("Total Income", f"{total_income:,.0f}")
col2.metric("Average Income", f"{average_income:,.0f}")
col3.metric("Median Income", f"{median_income:,.0f}")

col1, col2 = st.columns(2)

col1.metric("Maximum Income", f"{maximum_income:,.0f}")
col2.metric("Average Income of Defaulters", f"{default_income:,.0f}")

st.divider()

# Income Distribution
st.subheader("📊 Income Distribution")

fig, ax = plt.subplots(figsize=(8, 4))

sns.histplot(
    df["AMT_INCOME_TOTAL"],
    bins=40,
    kde=True,
    ax=ax
)

ax.set_xlabel("Income")
ax.set_ylabel("Customers")

st.pyplot(fig)

# Customers by Income Group
st.subheader("👥 Customers by Income Group")

income_group = (
    df["Income Group"]
    .value_counts()
    .sort_index()
    .reset_index()
)

income_group.columns = ["Income Group", "Customers"]

fig = px.bar(
    income_group,
    x="Income Group",
    y="Customers",
    color="Income Group",
    text="Customers",
    title="Customers by Income Group"
)

st.plotly_chart(fig, use_container_width=True)

# Default Rate by Income Group
st.subheader("⚠️ Default Rate by Income Group")

income_risk = (
    df.groupby("Income Group", observed=False)["TARGET"]
    .mean()
    .reset_index()
)

income_risk["Default Rate"] = income_risk["TARGET"] * 100

fig = px.bar(
    income_risk,
    x="Income Group",
    y="Default Rate",
    color="Default Rate",
    text="Default Rate",
    title="Default Rate by Income Group"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Income vs Credit
st.subheader("💳 Income vs Credit")

sample = df.sample(
    min(10000, len(df)),
    random_state=42
)

fig = px.scatter(
    sample,
    x="AMT_INCOME_TOTAL",
    y="AMT_CREDIT",
    color="TARGET",
    title="Income vs Credit"
)

st.plotly_chart(fig, use_container_width=True)

# Income vs Annuity
st.subheader("💵 Income vs Annuity")

fig = px.scatter(
    sample,
    x="AMT_INCOME_TOTAL",
    y="AMT_ANNUITY",
    color="TARGET",
    title="Income vs Annuity"
)

st.plotly_chart(fig, use_container_width=True)

# Income by Education
st.subheader("🎓 Income by Education")

education_income = (
    df.groupby("NAME_EDUCATION_TYPE")["AMT_INCOME_TOTAL"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

fig = px.bar(
    education_income,
    x="AMT_INCOME_TOTAL",
    y="NAME_EDUCATION_TYPE",
    orientation="h",
    color="AMT_INCOME_TOTAL",
    text="AMT_INCOME_TOTAL",
    title="Average Income by Education"
)

fig.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Income by Occupation
st.subheader("💼 Income by Occupation")

occupation_income = (
    df.groupby("OCCUPATION_TYPE")["AMT_INCOME_TOTAL"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

fig = px.bar(
    occupation_income,
    x="AMT_INCOME_TOTAL",
    y="OCCUPATION_TYPE",
    orientation="h",
    color="AMT_INCOME_TOTAL",
    text="AMT_INCOME_TOTAL",
    title="Average Income by Occupation"
)

fig.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)