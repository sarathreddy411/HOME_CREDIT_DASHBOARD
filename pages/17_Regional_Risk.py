import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset
df = pd.read_csv("data/application_train.csv", encoding="latin1")

st.title("🌍 Regional Risk Analysis")
st.write("Analysis of regional characteristics and customer default risk.")

# KPI values
most_common_rating = df["REGION_RATING_CLIENT"].mode()[0]

rating_risk = (
    df.groupby("REGION_RATING_CLIENT")["TARGET"]
    .mean()
    .sort_values(ascending=False)
)

highest_risk_rating = rating_risk.idxmax()

average_population = df["REGION_POPULATION_RELATIVE"].mean()

# KPI Cards
col1, col2, col3 = st.columns(3)

col1.metric(
    "Most Common Region Rating",
    most_common_rating
)

col2.metric(
    "Highest Risk Region Rating",
    highest_risk_rating
)

col3.metric(
    "Average Regional Population Indicator",
    f"{average_population:.4f}"
)

st.divider()

# Customers by Region Rating
st.subheader("📊 Customers by Region Rating")

region_count = (
    df["REGION_RATING_CLIENT"]
    .value_counts()
    .sort_index()
    .reset_index()
)

region_count.columns = [
    "Region Rating",
    "Customers"
]

fig = px.bar(
    region_count,
    x="Region Rating",
    y="Customers",
    color="Region Rating",
    text="Customers",
    title="Customers by Region Rating"
)

fig.update_traces(textposition="outside")

st.plotly_chart(fig, use_container_width=True)

# Default Rate by Region Rating
st.subheader("⚠️ Default Rate by Region Rating")

region_risk = (
    df.groupby("REGION_RATING_CLIENT")["TARGET"]
    .mean()
    .reset_index()
)

region_risk["Default Rate"] = region_risk["TARGET"] * 100

fig = px.bar(
    region_risk,
    x="REGION_RATING_CLIENT",
    y="Default Rate",
    color="Default Rate",
    text="Default Rate",
    title="Default Rate by Region Rating"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Credit by Region Rating
st.subheader("💳 Credit by Region Rating")

region_credit = (
    df.groupby("REGION_RATING_CLIENT")["AMT_CREDIT"]
    .mean()
    .reset_index()
)

fig = px.bar(
    region_credit,
    x="REGION_RATING_CLIENT",
    y="AMT_CREDIT",
    color="REGION_RATING_CLIENT",
    text="AMT_CREDIT",
    title="Average Credit by Region Rating"
)

fig.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Income by Region Rating
st.subheader("💰 Income by Region Rating")

region_income = (
    df.groupby("REGION_RATING_CLIENT")["AMT_INCOME_TOTAL"]
    .mean()
    .reset_index()
)

fig = px.bar(
    region_income,
    x="REGION_RATING_CLIENT",
    y="AMT_INCOME_TOTAL",
    color="REGION_RATING_CLIENT",
    text="AMT_INCOME_TOTAL",
    title="Average Income by Region Rating"
)

fig.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Region Mismatch vs Default
st.subheader("🔄 Region Mismatch vs Default")

region_mismatch = (
    df.groupby("REG_REGION_NOT_LIVE_REGION")["TARGET"]
    .mean()
    .reset_index()
)

region_mismatch["Default Rate"] = (
    region_mismatch["TARGET"] * 100
)

region_mismatch["Region Mismatch"] = (
    region_mismatch["REG_REGION_NOT_LIVE_REGION"]
    .map({
        0: "Same Region",
        1: "Different Region"
    })
)

fig = px.bar(
    region_mismatch,
    x="Region Mismatch",
    y="Default Rate",
    color="Region Mismatch",
    text="Default Rate",
    title="Default Rate by Region Mismatch"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# City Mismatch vs Default
st.subheader("🏙️ City Mismatch vs Default")

city_mismatch = (
    df.groupby("REG_CITY_NOT_LIVE_CITY")["TARGET"]
    .mean()
    .reset_index()
)

city_mismatch["Default Rate"] = (
    city_mismatch["TARGET"] * 100
)

city_mismatch["City Mismatch"] = (
    city_mismatch["REG_CITY_NOT_LIVE_CITY"]
    .map({
        0: "Same City",
        1: "Different City"
    })
)

fig = px.bar(
    city_mismatch,
    x="City Mismatch",
    y="Default Rate",
    color="City Mismatch",
    text="Default Rate",
    title="Default Rate by City Mismatch"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)