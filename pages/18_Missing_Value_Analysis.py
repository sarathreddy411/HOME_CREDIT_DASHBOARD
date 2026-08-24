import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("data/application_train.csv", encoding="latin1")

st.title("🔍 Missing Value Analysis")
st.write("Analysis of missing values and overall data quality.")

# Calculate missing value information
total_rows = df.shape[0]
total_columns = df.shape[1]
total_missing = df.isna().sum().sum()

missing_count = df.isna().sum()
missing_columns = (missing_count > 0).sum()
columns_over_50 = (missing_count > total_rows * 0.5).sum()

# KPI Cards
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Rows", f"{total_rows:,}")
col2.metric("Total Columns", total_columns)
col3.metric("Total Missing Values", f"{total_missing:,}")
col4.metric("Columns with Missing Values", missing_columns)
col5.metric("Columns >50% Missing", columns_over_50)

st.divider()

# Top 20 Columns with Missing Values
st.subheader("📊 Top 20 Columns with Missing Values")

missing_data = (
    missing_count[missing_count > 0]
    .sort_values(ascending=False)
    .head(20)
    .reset_index()
)

missing_data.columns = [
    "Column",
    "Missing Count"
]

fig = px.bar(
    missing_data,
    x="Missing Count",
    y="Column",
    orientation="h",
    color="Missing Count",
    text="Missing Count",
    title="Top 20 Columns with Missing Values"
)

fig.update_traces(textposition="outside")

st.plotly_chart(fig, use_container_width=True)

# Missing Percentage by Column
st.subheader("📈 Missing Percentage by Column")

missing_percentage = (
    df.isna().mean() * 100
).sort_values(ascending=False)

percentage_data = (
    missing_percentage[missing_percentage > 0]
    .head(20)
    .reset_index()
)

percentage_data.columns = [
    "Column",
    "Missing Percentage"
]

fig = px.bar(
    percentage_data,
    x="Missing Percentage",
    y="Column",
    orientation="h",
    color="Missing Percentage",
    text="Missing Percentage",
    title="Missing Percentage by Column"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# Missing Values Heatmap
st.subheader("🔥 Missing Values Heatmap")

sample = df.sample(
    min(5000, len(df)),
    random_state=42
)

fig, ax = plt.subplots(figsize=(12, 6))

sns.heatmap(
    sample.isna(),
    cbar=False,
    yticklabels=False
)

ax.set_xlabel("Columns")
ax.set_ylabel("Rows")

st.pyplot(fig)

# Missing Values by Data Type
st.subheader("📋 Missing Values by Data Type")

dtype_missing = (
    df.isna()
    .sum()
    .groupby(df.dtypes.astype(str))
    .sum()
    .reset_index()
)

dtype_missing.columns = [
    "Data Type",
    "Missing Values"
]

fig = px.bar(
    dtype_missing,
    x="Data Type",
    y="Missing Values",
    color="Data Type",
    text="Missing Values",
    title="Missing Values by Data Type"
)

fig.update_traces(textposition="outside")

st.plotly_chart(fig, use_container_width=True)

# Missing Value Table
st.subheader("📋 Missing Value Details")

missing_table = pd.DataFrame({
    "Column": df.columns,
    "Missing Count": df.isna().sum().values,
    "Missing %": (df.isna().mean() * 100).values,
    "Data Type": df.dtypes.astype(str).values
})

missing_table = (
    missing_table[missing_table["Missing Count"] > 0]
    .sort_values("Missing Count", ascending=False)
)

st.dataframe(
    missing_table,
    use_container_width=True,
    hide_index=True
)

# Recommended Actions
st.subheader("🛠️ Missing Value Actions")

st.write("• Numeric columns → Mean or Median")
st.write("• Categorical columns → Mode or 'Unknown'")
st.write("• Columns with very high missing values → Consider dropping")
st.write("• Important missing information → Create a Missing Indicator")