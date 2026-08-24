import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("data/application_train.csv", encoding="latin1")

st.title("🏦 Executive Overview")
st.write("Overall analysis of loan applicants and credit risk.")

# Calculate KPIs
total_applications = len(df)
default_customers = (df["TARGET"] == 1).sum()
non_default_customers = (df["TARGET"] == 0).sum()
default_rate = df["TARGET"].mean() * 100
total_credit = df["AMT_CREDIT"].sum()
average_credit = df["AMT_CREDIT"].mean()
average_income = df["AMT_INCOME_TOTAL"].mean()
average_annuity = df["AMT_ANNUITY"].mean()

# Find important insights
most_common_income = df["NAME_INCOME_TYPE"].mode()[0]
most_common_education = df["NAME_EDUCATION_TYPE"].mode()[0]

income_risk = df.groupby("NAME_INCOME_TYPE")["TARGET"].mean()
highest_risk_segment = income_risk.idxmax()

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Applications", f"{total_applications:,}")
col2.metric("Default Customers", f"{default_customers:,}")
col3.metric("Non-Default Customers", f"{non_default_customers:,}")
col4.metric("Default Rate", f"{default_rate:.2f}%")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Credit", f"{total_credit:,.0f}")
col2.metric("Average Credit", f"{average_credit:,.0f}")
col3.metric("Average Income", f"{average_income:,.0f}")
col4.metric("Average Annuity", f"{average_annuity:,.0f}")

st.divider()

# Default vs Non-Default
st.subheader("🎯 Default vs Non-Default Customers")

target_data = pd.DataFrame({
    "Customer Type": ["Non-Default", "Default"],
    "Customers": [non_default_customers, default_customers]
})

fig = px.bar(
    target_data,
    x="Customer Type",
    y="Customers",
    color="Customer Type",
    text="Customers",
    title="Default vs Non-Default Customers"
)

fig.update_traces(textposition="outside")

st.plotly_chart(fig, use_container_width=True)

# Applications by Gender
st.subheader("👥 Applications by Gender")

gender_data = (
    df["CODE_GENDER"]
    .value_counts()
    .reset_index()
)

gender_data.columns = ["Gender", "Applications"]

fig = px.bar(
    gender_data,
    x="Gender",
    y="Applications",
    color="Gender",
    text="Applications",
    title="Applications by Gender"
)

fig.update_traces(textposition="outside")

st.plotly_chart(fig, use_container_width=True)

# Applications by Contract Type
st.subheader("📄 Applications by Contract Type")

contract_data = (
    df["NAME_CONTRACT_TYPE"]
    .value_counts()
    .reset_index()
)

contract_data.columns = ["Contract Type", "Applications"]

fig = px.bar(
    contract_data,
    x="Contract Type",
    y="Applications",
    color="Contract Type",
    text="Applications",
    title="Applications by Contract Type"
)

fig.update_traces(textposition="outside")

st.plotly_chart(fig, use_container_width=True)

# Applications by Income Type
st.subheader("💼 Applications by Income Type")

income_data = (
    df["NAME_INCOME_TYPE"]
    .value_counts()
    .reset_index()
)

income_data.columns = ["Income Type", "Applications"]

fig = px.bar(
    income_data,
    x="Income Type",
    y="Applications",
    color="Income Type",
    text="Applications",
    title="Applications by Income Type"
)

fig.update_traces(textposition="outside")

st.plotly_chart(fig, use_container_width=True)

# Credit Amount Distribution
st.subheader("💳 Credit Amount Distribution")

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

# Overall Applicant Summary
st.subheader("📊 Overall Applicant Summary")

summary = pd.DataFrame({
    "Metric": [
        "Default Rate",
        "Average Income",
        "Average Credit",
        "Average Annuity"
    ],
    "Value": [
        f"{default_rate:.2f}%",
        f"{average_income:,.0f}",
        f"{average_credit:,.0f}",
        f"{average_annuity:,.0f}"
    ]
})

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)

# Important Insights
st.subheader("💡 Important Insights")

st.write(f"• Overall Default Rate: **{default_rate:.2f}%**")
st.write(f"• Average Customer Income: **{average_income:,.0f}**")
st.write(f"• Average Loan Amount: **{average_credit:,.0f}**")
st.write(f"• Most Common Income Type: **{most_common_income}**")
st.write(f"• Most Common Education Level: **{most_common_education}**")
st.write(f"• Highest Risk Customer Segment: **{highest_risk_segment}**")