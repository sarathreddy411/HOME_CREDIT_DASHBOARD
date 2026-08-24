import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv(r"D:\Assignments\home_credit_dashboard\data\application_train.csv", encoding="latin1")

# Page title
st.title("💳 Annuity Burden Analysis")
st.write("Analysis of repayment burden relative to customer income.")

# Calculate annuity-to-income ratio
df["Annuity_Income_Ratio"] = (
    df["AMT_ANNUITY"] / df["AMT_INCOME_TOTAL"]
)

# Remove missing and invalid ratio values
df = df[
    df["Annuity_Income_Ratio"].notna()
    & (df["Annuity_Income_Ratio"] >= 0)
]

# Show the distribution of annuity-to-income ratio
st.subheader("📊 Annuity-to-Income Distribution")

fig, ax = plt.subplots(figsize=(8, 4))

sns.histplot(
    df["Annuity_Income_Ratio"],
    bins=40,
    kde=True,
    ax=ax
)

ax.set_xlabel("Annuity-to-Income Ratio")
ax.set_ylabel("Number of Customers")

st.pyplot(fig)

# Create repayment burden groups
st.subheader("⚠️ Default Rate by Repayment Burden")

df["Burden Group"] = pd.cut(
    df["Annuity_Income_Ratio"],
    bins=[0, 0.2, 0.4, 0.6, float("inf")],
    labels=[
        "Low Repayment Burden",
        "Medium Repayment Burden",
        "High Repayment Burden",
        "Very High Repayment Burden"
    ]
)

# Calculate default rate for each burden group
burden_risk = (
    df.groupby("Burden Group", observed=False)["TARGET"]
    .mean()
    .reset_index()
)

burden_risk["Default Rate"] = burden_risk["TARGET"] * 100

# Display default rate by burden group
fig = px.bar(
    burden_risk,
    x="Burden Group",
    y="Default Rate",
    color="Default Rate",
    text="Default Rate",
    title="Default Rate by Repayment Burden"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Calculate average ratio by gender
st.subheader("👥 Ratio by Gender")

gender_ratio = (
    df.groupby("CODE_GENDER")["Annuity_Income_Ratio"]
    .mean()
    .reset_index()
)

# Display ratio by gender
fig = px.bar(
    gender_ratio,
    x="CODE_GENDER",
    y="Annuity_Income_Ratio",
    color="CODE_GENDER",
    text="Annuity_Income_Ratio",
    title="Average Annuity-to-Income Ratio by Gender"
)

fig.update_traces(
    texttemplate="%{text:.3f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Calculate average ratio by income type
st.subheader("💼 Ratio by Income Type")

income_ratio = (
    df.groupby("NAME_INCOME_TYPE")["Annuity_Income_Ratio"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

# Display ratio by income type
fig = px.bar(
    income_ratio,
    x="Annuity_Income_Ratio",
    y="NAME_INCOME_TYPE",
    orientation="h",
    color="Annuity_Income_Ratio",
    text="Annuity_Income_Ratio",
    title="Average Annuity-to-Income Ratio by Income Type"
)

fig.update_traces(
    texttemplate="%{text:.3f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Calculate average ratio by education
st.subheader("🎓 Ratio by Education")

education_ratio = (
    df.groupby("NAME_EDUCATION_TYPE")["Annuity_Income_Ratio"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

# Display ratio by education
fig = px.bar(
    education_ratio,
    x="Annuity_Income_Ratio",
    y="NAME_EDUCATION_TYPE",
    orientation="h",
    color="Annuity_Income_Ratio",
    text="Annuity_Income_Ratio",
    title="Average Annuity-to-Income Ratio by Education"
)

fig.update_traces(
    texttemplate="%{text:.3f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Take a random sample for the scatter plot
sample = df.sample(
    min(10000, len(df)),
    random_state=42
)

# Show relationship between ratio and default
st.subheader("🎯 Ratio vs TARGET")

fig = px.scatter(
    sample,
    x="Annuity_Income_Ratio",
    y="TARGET",
    color="TARGET",
    title="Annuity-to-Income Ratio vs Default",
    labels={
        "Annuity_Income_Ratio": "Annuity-to-Income Ratio",
        "TARGET": "Default"
    }
)

st.plotly_chart(fig, use_container_width=True)