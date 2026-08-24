import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("data/application_train.csv",encoding="latin1")

st.title("💰 Income vs Credit Analysis")
st.write("Analysis of credit amount in relation to customer income.")

# CREDIT-TO-INCOME RATIO

df["Credit_Income_Ratio"] = (
    df["AMT_CREDIT"] / df["AMT_INCOME_TOTAL"]
)

# Remove invalid values
df = df[
    df["Credit_Income_Ratio"].notna()
    & (df["Credit_Income_Ratio"] >= 0)
]

# KPI CARDS

average_ratio = df["Credit_Income_Ratio"].mean()

highest_ratio = df["Credit_Income_Ratio"].max()

high_ratio_default_rate = (
    df[df["Credit_Income_Ratio"] > 6]["TARGET"].mean() * 100
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Credit-to-Income Ratio",
    f"{average_ratio:.2f}"
)

col2.metric(
    "Highest Credit-to-Income Ratio",
    f"{highest_ratio:.2f}"
)

col3.metric(
    "Default Rate - High Ratio",
    f"{high_ratio_default_rate:.2f}%"
)

st.divider()

# 1. INCOME VS CREDIT

st.subheader("Income vs Credit")

sample = df.sample(
    min(10000, len(df)),
    random_state=42
)

fig = px.scatter(
    sample,
    x="AMT_INCOME_TOTAL",
    y="AMT_CREDIT",
    color="TARGET",
    title="Income vs Credit",
    labels={
        "AMT_INCOME_TOTAL": "Income",
        "AMT_CREDIT": "Credit Amount",
        "TARGET": "Default"
    }
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# 2. CREDIT/INCOME RATIO DISTRIBUTION

st.subheader("Credit-to-Income Ratio Distribution")

fig, ax = plt.subplots(figsize=(8, 4))

sns.histplot(
    df["Credit_Income_Ratio"],
    bins=40,
    kde=True,
    ax=ax
)

ax.set_xlabel("Credit-to-Income Ratio")
ax.set_ylabel("Number of Customers")

st.pyplot(fig)

# 3. DEFAULT RATE VS CREDIT/INCOME RATIO

st.subheader("Default Rate by Credit-to-Income Ratio")

df["Ratio Group"] = pd.cut(
    df["Credit_Income_Ratio"],
    bins=[0, 2, 4, 6, float("inf")],
    labels=[
        "Low (<2)",
        "Moderate (2-4)",
        "High (4-6)",
        "Very High (>6)"
    ]
)

ratio_risk = (
    df.groupby("Ratio Group", observed=False)["TARGET"]
    .mean()
    .reset_index()
)

ratio_risk["Default Rate"] = (
    ratio_risk["TARGET"] * 100
)

fig = px.bar(
    ratio_risk,
    x="Ratio Group",
    y="Default Rate",
    color="Default Rate",
    text="Default Rate",
    title="Default Rate by Credit-to-Income Ratio"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# 4. GENDER-WISE CREDIT/INCOME RATIO
st.subheader("Gender-wise Credit-to-Income Ratio")

gender_ratio = (
    df.groupby("CODE_GENDER")["Credit_Income_Ratio"]
    .mean()
    .reset_index()
)

fig = px.bar(
    gender_ratio,
    x="CODE_GENDER",
    y="Credit_Income_Ratio",
    color="CODE_GENDER",
    text="Credit_Income_Ratio",
    title="Average Credit-to-Income Ratio by Gender"
)

fig.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# 5. EDUCATION-WISE CREDIT/INCOME RATIO


st.subheader("Education-wise Credit-to-Income Ratio")

education_ratio = (
    df.groupby("NAME_EDUCATION_TYPE")["Credit_Income_Ratio"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

fig = px.bar(
    education_ratio,
    x="Credit_Income_Ratio",
    y="NAME_EDUCATION_TYPE",
    orientation="h",
    color="Credit_Income_Ratio",
    text="Credit_Income_Ratio",
    title="Average Credit-to-Income Ratio by Education"
)

fig.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

st.plotly_chart(
    fig,
    use_container_width=True
)