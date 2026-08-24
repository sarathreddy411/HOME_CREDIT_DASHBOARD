import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("data/application_train.csv", encoding="latin1")

st.title("💼 Employment Analysis")
st.write("Analysis of employment status, work history and credit risk.")

# Clean DAYS_EMPLOYED special values
df["DAYS_EMPLOYED"] = df["DAYS_EMPLOYED"].replace(365243, float("nan"))
# Calculate employment years
df["Employment_Years"] = df["DAYS_EMPLOYED"].abs() / 365

# Calculate occupation default rate
occupation_default = (
    df.groupby("OCCUPATION_TYPE")["TARGET"]
    .mean()
    .sort_values(ascending=False)
)

# KPI calculations
average_employment = df["Employment_Years"].mean()

most_common_occupation = (
    df["OCCUPATION_TYPE"].mode().iloc[0]
)

most_common_income_type = (
    df["NAME_INCOME_TYPE"].mode().iloc[0]
)

highest_risk_occupation = occupation_default.idxmax()

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Average Employment Years",
    f"{average_employment:.2f}"
)

col2.metric(
    "Most Common Occupation",
    most_common_occupation
)

col3.metric(
    "Most Common Income Type",
    most_common_income_type
)

col4.metric(
    "Highest Risk Occupation",
    highest_risk_occupation
)

st.divider()

# Employment Years Distribution
st.subheader("📊 Employment Years Distribution")

fig, ax = plt.subplots(figsize=(8, 4))

sns.histplot(
    df["Employment_Years"].dropna(),
    bins=30,
    kde=True,
    ax=ax
)

ax.set_xlabel("Employment Years")
ax.set_ylabel("Number of Customers")

st.pyplot(fig)

# Default Rate by Employment Years
st.subheader("⚠️ Default Rate by Employment Years")

df["Employment Group"] = pd.cut(
    df["Employment_Years"],
    bins=[0, 2, 5, 10, 20, float("inf")],
    labels=[
        "0-2 Years",
        "2-5 Years",
        "5-10 Years",
        "10-20 Years",
        "20+ Years"
    ]
)

employment_risk = (
    df.groupby("Employment Group", observed=False)["TARGET"]
    .mean()
    .reset_index()
)

employment_risk["Default Rate"] = (
    employment_risk["TARGET"] * 100
)

fig = px.bar(
    employment_risk,
    x="Employment Group",
    y="Default Rate",
    color="Default Rate",
    text="Default Rate",
    title="Default Rate by Employment Years"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Applications by Income Type
st.subheader("💰 Applications by Income Type")

income_data = (
    df["NAME_INCOME_TYPE"]
    .value_counts()
    .reset_index()
)

income_data.columns = [
    "Income Type",
    "Applications"
]

fig = px.bar(
    income_data,
    x="Income Type",
    y="Applications",
    color="Income Type",
    text="Applications",
    title="Applications by Income Type"
)

fig.update_traces(
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Default Rate by Income Type
st.subheader("⚠️ Default Rate by Income Type")

income_risk = (
    df.groupby("NAME_INCOME_TYPE")["TARGET"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

income_risk["Default Rate"] = (
    income_risk["TARGET"] * 100
)

fig = px.bar(
    income_risk,
    x="NAME_INCOME_TYPE",
    y="Default Rate",
    color="Default Rate",
    text="Default Rate",
    title="Default Rate by Income Type"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Applications by Occupation
st.subheader("👷 Applications by Occupation")

occupation_data = (
    df["OCCUPATION_TYPE"]
    .dropna()
    .value_counts()
    .reset_index()
)

occupation_data.columns = [
    "Occupation",
    "Applications"
]

fig = px.bar(
    occupation_data,
    x="Applications",
    y="Occupation",
    orientation="h",
    color="Applications",
    text="Applications",
    title="Applications by Occupation"
)

fig.update_traces(
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Default Rate by Occupation
st.subheader("🚨 Default Rate by Occupation")

occupation_risk = (
    df.groupby("OCCUPATION_TYPE")["TARGET"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

occupation_risk["Default Rate"] = (
    occupation_risk["TARGET"] * 100
)

fig = px.bar(
    occupation_risk,
    x="Default Rate",
    y="OCCUPATION_TYPE",
    orientation="h",
    color="Default Rate",
    text="Default Rate",
    title="Default Rate by Occupation"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Default Rate by Organization Type
st.subheader("🏢 Default Rate by Organization Type")

organization_risk = (
    df.groupby("ORGANIZATION_TYPE")["TARGET"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

organization_risk["Default Rate"] = (
    organization_risk["TARGET"] * 100
)

fig = px.bar(
    organization_risk,
    x="Default Rate",
    y="ORGANIZATION_TYPE",
    orientation="h",
    color="Default Rate",
    title="Default Rate by Organization Type"
)

st.plotly_chart(fig, use_container_width=True)