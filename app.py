import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Home Credit Dashboard",
    page_icon="🏦",
    layout="wide"
)

df = pd.read_csv("data/application_train.csv", encoding="latin1")

st.title("🏦 Home Credit Default Risk Dashboard")
st.markdown("### Loan Application & Credit Risk Overview")

st.divider()

st.subheader("📊 Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Applications", f"{len(df):,}")
col2.metric("Total Features", f"{df.shape[1]:,}")
col3.metric("Default Customers", f"{(df['TARGET'] == 1).sum():,}")
col4.metric("Default Rate", f"{df['TARGET'].mean() * 100:.2f}%")

st.divider()

st.subheader("💰 Overall Financial Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Credit",
    f"{df['AMT_CREDIT'].sum():,.0f}"
)

col2.metric(
    "Average Credit",
    f"{df['AMT_CREDIT'].mean():,.0f}"
)

col3.metric(
    "Average Income",
    f"{df['AMT_INCOME_TOTAL'].mean():,.0f}"
)

col4.metric(
    "Average Annuity",
    f"{df['AMT_ANNUITY'].mean():,.0f}"
)

st.divider()

st.subheader("🎯 Default Overview")

target_data = pd.DataFrame({
    "Customer Type": [
        "Non-Default",
        "Default"
    ],
    "Customers": [
        (df["TARGET"] == 0).sum(),
        (df["TARGET"] == 1).sum()
    ]
})

fig = px.pie(
    target_data,
    names="Customer Type",
    values="Customers",
    hole=0.5,
    title="Default vs Non-Default Customers"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("👥 Applicant Overview")

col1, col2 = st.columns(2)

with col1:

    gender_data = (
        df["CODE_GENDER"]
        .value_counts()
        .reset_index()
    )

    gender_data.columns = [
        "Gender",
        "Applications"
    ]

    fig = px.bar(
        gender_data,
        x="Gender",
        y="Applications",
        color="Gender",
        text="Applications",
        title="Applications by Gender"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    contract_data = (
        df["NAME_CONTRACT_TYPE"]
        .value_counts()
        .reset_index()
    )

    contract_data.columns = [
        "Contract Type",
        "Applications"
    ]

    fig = px.bar(
        contract_data,
        x="Contract Type",
        y="Applications",
        color="Contract Type",
        text="Applications",
        title="Applications by Contract Type"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

st.subheader("📌 What This Dashboard Covers")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **👤 Customer Analysis**

    - Demographics
    - Age
    - Gender
    - Education
    - Family
    - Housing
    """)

with col2:
    st.markdown("""
    **💰 Financial Analysis**

    - Income
    - Credit
    - Annuity
    - Income vs Credit
    - Annuity Burden
    """)

with col3:
    st.markdown("""
    **⚠️ Risk Analysis**

    - Default Risk
    - Employment
    - External Scores
    - Regional Risk
    - Correlation
    - Customer Risk
    """)

st.divider()

st.info(
    "👈 Use the sidebar to explore the detailed analysis pages."
)