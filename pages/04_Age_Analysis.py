import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("data/application_train.csv", encoding="latin1")

st.title("🎂 Age Analysis")
st.write("Analysis of age and credit risk.")

# Calculate age
df["Age"] = abs(df["DAYS_BIRTH"]) / 365

# Create age groups
df["Age Group"] = pd.cut(
    df["Age"],
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

# Calculate KPIs
average_age = df["Age"].mean()
youngest = df["Age"].min()
oldest = df["Age"].max()

age_risk = (
    df.groupby("Age Group", observed=False)["TARGET"]
    .mean()
)

highest_risk_group = age_risk.idxmax()

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Average Age", f"{average_age:.1f}")
col2.metric("Youngest Customer", f"{youngest:.1f}")
col3.metric("Oldest Customer", f"{oldest:.1f}")
col4.metric("Highest Risk Age Group", highest_risk_group)

st.divider()

# Age Distribution
st.subheader("📊 Age Distribution")

fig, ax = plt.subplots(figsize=(8, 4))

sns.histplot(
    df["Age"],
    bins=40,
    kde=True,
    ax=ax
)

ax.set_xlabel("Age")
ax.set_ylabel("Customers")

st.pyplot(fig)

# Applications by Age Group
st.subheader("👥 Applications by Age Group")

age_data = (
    df["Age Group"]
    .value_counts()
    .sort_index()
    .reset_index()
)

age_data.columns = ["Age Group", "Applications"]

fig = px.bar(
    age_data,
    x="Age Group",
    y="Applications",
    color="Age Group",
    text="Applications",
    title="Applications by Age Group"
)

st.plotly_chart(fig, use_container_width=True)

# Default Rate by Age
st.subheader("⚠️ Default Rate by Age")

age_default = (
    df.groupby("Age", observed=False)["TARGET"]
    .mean()
    .reset_index()
)

age_default["Default Rate"] = age_default["TARGET"] * 100

fig = px.scatter(
    age_default,
    x="Age",
    y="Default Rate",
    title="Default Rate by Age"
)

st.plotly_chart(fig, use_container_width=True)

# Default Rate by Age Group
st.subheader("🚨 Default Rate by Age Group")

age_risk = (
    df.groupby("Age Group", observed=False)["TARGET"]
    .mean()
    .reset_index()
)

age_risk["Default Rate"] = age_risk["TARGET"] * 100

fig = px.bar(
    age_risk,
    x="Age Group",
    y="Default Rate",
    color="Default Rate",
    text="Default Rate",
    title="Default Rate by Age Group"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Credit Amount by Age
st.subheader("💳 Credit Amount by Age")

credit_age = (
    df.groupby("Age", observed=False)["AMT_CREDIT"]
    .mean()
    .reset_index()
)

fig = px.line(
    credit_age,
    x="Age",
    y="AMT_CREDIT",
    title="Average Credit Amount by Age"
)

st.plotly_chart(fig, use_container_width=True)

# Income by Age
st.subheader("💰 Income by Age")

income_age = (
    df.groupby("Age", observed=False)["AMT_INCOME_TOTAL"]
    .mean()
    .reset_index()
)

fig = px.line(
    income_age,
    x="Age",
    y="AMT_INCOME_TOTAL",
    title="Average Income by Age"
)

st.plotly_chart(fig, use_container_width=True)