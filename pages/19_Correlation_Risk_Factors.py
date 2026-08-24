import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("data/application_train.csv", encoding="latin1")

st.title("📊 Correlation & Risk Factor Analysis")
st.write("Analysis of numerical relationships associated with loan default.")

# Select numerical features
features = [
    "TARGET",
    "AMT_INCOME_TOTAL",
    "AMT_CREDIT",
    "AMT_ANNUITY",
    "AMT_GOODS_PRICE",
    "DAYS_BIRTH",
    "DAYS_EMPLOYED",
    "EXT_SOURCE_1",
    "EXT_SOURCE_2",
    "EXT_SOURCE_3",
    "CNT_CHILDREN",
    "CNT_FAM_MEMBERS"
]

corr = df[features].corr()

# Correlation Heatmap
st.subheader("🔥 Correlation Heatmap")

fig, ax = plt.subplots(figsize=(12, 8))

sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0,
    ax=ax
)

st.pyplot(fig)

# Correlation with TARGET
st.subheader("🎯 Correlation with TARGET")

target_corr = (
    corr["TARGET"]
    .drop("TARGET")
    .sort_values()
    .reset_index()
)

target_corr.columns = [
    "Feature",
    "Correlation"
]

fig = px.bar(
    target_corr,
    x="Correlation",
    y="Feature",
    orientation="h",
    color="Correlation",
    text="Correlation",
    title="Correlation of Features with TARGET"
)

fig.update_traces(
    texttemplate="%{text:.3f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Top Positive Correlations
st.subheader("📈 Top Positive Correlations")

positive_corr = (
    target_corr[target_corr["Correlation"] > 0]
    .sort_values("Correlation", ascending=False)
    .head(5)
)

fig = px.bar(
    positive_corr,
    x="Feature",
    y="Correlation",
    color="Correlation",
    text="Correlation",
    title="Top Positive Correlations with TARGET"
)

fig.update_traces(
    texttemplate="%{text:.3f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Top Negative Correlations
st.subheader("📉 Top Negative Correlations")

negative_corr = (
    target_corr[target_corr["Correlation"] < 0]
    .sort_values("Correlation")
    .head(5)
)

fig = px.bar(
    negative_corr,
    x="Feature",
    y="Correlation",
    color="Correlation",
    text="Correlation",
    title="Top Negative Correlations with TARGET"
)

fig.update_traces(
    texttemplate="%{text:.3f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Credit vs Income
st.subheader("💰 Credit vs Income")

sample = df.sample(
    min(10000, len(df)),
    random_state=42
)

fig = px.scatter(
    sample,
    x="AMT_INCOME_TOTAL",
    y="AMT_CREDIT",
    color="TARGET",
    title="Credit vs Income",
    labels={
        "AMT_INCOME_TOTAL": "Income",
        "AMT_CREDIT": "Credit Amount",
        "TARGET": "Default"
    }
)

st.plotly_chart(fig, use_container_width=True)

# External Score vs TARGET
st.subheader("📊 External Score vs TARGET")

external_data = df[
    ["EXT_SOURCE_1", "EXT_SOURCE_2", "EXT_SOURCE_3", "TARGET"]
].melt(
    id_vars="TARGET",
    var_name="External Score",
    value_name="Score"
)

external_data = external_data.dropna()

fig = px.box(
    external_data,
    x="TARGET",
    y="Score",
    color="External Score",
    title="External Scores by TARGET"
)

st.plotly_chart(fig, use_container_width=True)

# Risk Factor Analysis
st.subheader("⚠️ Important Risk Factors")

df["Credit_Income_Ratio"] = (
    df["AMT_CREDIT"] / df["AMT_INCOME_TOTAL"]
)

df["Annuity_Income_Ratio"] = (
    df["AMT_ANNUITY"] / df["AMT_INCOME_TOTAL"]
)

external_score = (
    df[
        ["EXT_SOURCE_1", "EXT_SOURCE_2", "EXT_SOURCE_3"]
    ].mean(axis=1)
)

risk_factors = {
    "Low External Credit Score": (
        external_score < external_score.quantile(0.25)
    ).mean() * 100,

    "High Credit-to-Income Ratio": (
        df["Credit_Income_Ratio"] >
        df["Credit_Income_Ratio"].quantile(0.75)
    ).mean() * 100,

    "High Annuity-to-Income Ratio": (
        df["Annuity_Income_Ratio"] >
        df["Annuity_Income_Ratio"].quantile(0.75)
    ).mean() * 100,

    "Younger Age Group": (
        abs(df["DAYS_BIRTH"]) / 365 < 30
    ).mean() * 100,

    "High Regional Risk Rating": (
        df["REGION_RATING_CLIENT"] == 3
    ).mean() * 100
}

risk_data = pd.DataFrame(
    list(risk_factors.items()),
    columns=["Risk Factor", "Customers (%)"]
)

fig = px.bar(
    risk_data,
    x="Customers (%)",
    y="Risk Factor",
    orientation="h",
    color="Customers (%)",
    text="Customers (%)",
    title="Potential Risk Indicators"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Occupation Risk
st.subheader("👷 Occupation Risk")

occupation_risk = (
    df.groupby("OCCUPATION_TYPE")["TARGET"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
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
    title="Top 10 Occupations by Default Rate"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Income Type Risk
st.subheader("💼 Income Type Risk")

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
    x="Default Rate",
    y="NAME_INCOME_TYPE",
    orientation="h",
    color="Default Rate",
    text="Default Rate",
    title="Default Rate by Income Type"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Employment History
st.subheader("💼 Employment History")

df["DAYS_EMPLOYED"] = pd.to_numeric(
    df["DAYS_EMPLOYED"],
    errors="coerce"
)

df["DAYS_EMPLOYED"] = df["DAYS_EMPLOYED"].replace(
    365243,
    float("nan")
)

df["Employment_Years"] = (
    df["DAYS_EMPLOYED"].abs() / 365
)

df["Employment_Group"] = pd.cut(
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
    df.groupby(
        "Employment_Group",
        observed=False
    )["TARGET"]
    .mean()
    .reset_index()
)

employment_risk["Default Rate"] = (
    employment_risk["TARGET"] * 100
)

fig = px.bar(
    employment_risk,
    x="Employment_Group",
    y="Default Rate",
    color="Default Rate",
    text="Default Rate",
    title="Default Rate by Employment History"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)