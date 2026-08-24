import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset
df = pd.read_csv("data/application_train.csv", encoding="latin1")

st.title("🎯 Target / Default Analysis")
st.write("Analysis of the main TARGET variable.")

# Calculate target values
non_default = (df["TARGET"] == 0).sum()
default = (df["TARGET"] == 1).sum()

default_rate = default / len(df) * 100
non_default_rate = non_default / len(df) * 100

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("TARGET = 0", f"{non_default:,}")
col2.metric("TARGET = 1", f"{default:,}")
col3.metric("Default Rate", f"{default_rate:.2f}%")
col4.metric("Non-Default Rate", f"{non_default_rate:.2f}%")

st.divider()

# TARGET Count
st.subheader("📊 TARGET Count")

target_data = pd.DataFrame({
    "TARGET": ["Non-Default", "Default"],
    "Customers": [non_default, default]
})

fig = px.bar(
    target_data,
    x="TARGET",
    y="Customers",
    color="TARGET",
    text="Customers",
    title="TARGET Count"
)

fig.update_traces(textposition="outside")

st.plotly_chart(fig, use_container_width=True)

# TARGET Percentage
st.subheader("🥧 TARGET Percentage")

fig = px.pie(
    target_data,
    names="TARGET",
    values="Customers",
    hole=0.45,
    title="Default vs Non-Default Percentage"
)

st.plotly_chart(fig, use_container_width=True)

# Default Rate by Gender
st.subheader("👥 Default Rate by Gender")

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

# Default Rate by Income Type
st.subheader("💼 Default Rate by Income Type")

income_risk = (
    df.groupby("NAME_INCOME_TYPE")["TARGET"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

income_risk["Default Rate"] = income_risk["TARGET"] * 100

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

# Default Rate by Education
st.subheader("🎓 Default Rate by Education")

education_risk = (
    df.groupby("NAME_EDUCATION_TYPE")["TARGET"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

education_risk["Default Rate"] = education_risk["TARGET"] * 100

fig = px.bar(
    education_risk,
    x="Default Rate",
    y="NAME_EDUCATION_TYPE",
    orientation="h",
    color="Default Rate",
    text="Default Rate",
    title="Default Rate by Education"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Default Rate by Contract Type
st.subheader("📄 Default Rate by Contract Type")

contract_risk = (
    df.groupby("NAME_CONTRACT_TYPE")["TARGET"]
    .mean()
    .reset_index()
)

contract_risk["Default Rate"] = contract_risk["TARGET"] * 100

fig = px.bar(
    contract_risk,
    x="NAME_CONTRACT_TYPE",
    y="Default Rate",
    color="NAME_CONTRACT_TYPE",
    text="Default Rate",
    title="Default Rate by Contract Type"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)