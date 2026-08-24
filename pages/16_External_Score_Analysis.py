import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("data/application_train.csv", encoding="latin1")

st.title("📊 External Credit Score Analysis")
st.write("Analysis of external credit scores and their relationship with customer default risk.")

# Calculate average external score
df["Average_External_Score"] = (
    df["EXT_SOURCE_1"] +
    df["EXT_SOURCE_2"] +
    df["EXT_SOURCE_3"]
) / 3

# Calculate missing external score records
missing_scores = (
    df[["EXT_SOURCE_1", "EXT_SOURCE_2", "EXT_SOURCE_3"]]
    .isna()
    .all(axis=1)
    .sum()
)

# KPI values
avg_score_1 = df["EXT_SOURCE_1"].mean()
avg_score_2 = df["EXT_SOURCE_2"].mean()
avg_score_3 = df["EXT_SOURCE_3"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Average EXT_SOURCE_1", f"{avg_score_1:.2f}")
col2.metric("Average EXT_SOURCE_2", f"{avg_score_2:.2f}")
col3.metric("Average EXT_SOURCE_3", f"{avg_score_3:.2f}")
col4.metric("Missing Score Records", f"{missing_scores:,}")

st.divider()

# EXT_SOURCE_1 Distribution
st.subheader("📈 EXT_SOURCE_1 Distribution")

fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(df["EXT_SOURCE_1"].dropna(), bins=30, kde=True, ax=ax)
ax.set_xlabel("EXT_SOURCE_1")
ax.set_ylabel("Customers")
st.pyplot(fig)

# EXT_SOURCE_2 Distribution
st.subheader("📈 EXT_SOURCE_2 Distribution")

fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(df["EXT_SOURCE_2"].dropna(), bins=30, kde=True, ax=ax)
ax.set_xlabel("EXT_SOURCE_2")
ax.set_ylabel("Customers")
st.pyplot(fig)

# EXT_SOURCE_3 Distribution
st.subheader("📈 EXT_SOURCE_3 Distribution")

fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(df["EXT_SOURCE_3"].dropna(), bins=30, kde=True, ax=ax)
ax.set_xlabel("EXT_SOURCE_3")
ax.set_ylabel("Customers")
st.pyplot(fig)

# External Scores by TARGET
st.subheader("🎯 External Scores by TARGET")

score_target = df.groupby("TARGET")[
    ["EXT_SOURCE_1", "EXT_SOURCE_2", "EXT_SOURCE_3"]
].mean().reset_index()

score_target["TARGET"] = score_target["TARGET"].map({
    0: "Non-Default",
    1: "Default"
})

score_target = score_target.melt(
    id_vars="TARGET",
    var_name="External Score",
    value_name="Average Score"
)

fig = px.bar(
    score_target,
    x="External Score",
    y="Average Score",
    color="TARGET",
    barmode="group",
    title="Average External Scores by TARGET"
)

st.plotly_chart(fig, use_container_width=True)

# EXT_SOURCE_1 vs EXT_SOURCE_2
st.subheader("🔍 EXT_SOURCE_1 vs EXT_SOURCE_2")

sample = df.sample(min(10000, len(df)), random_state=42)

fig = px.scatter(
    sample,
    x="EXT_SOURCE_1",
    y="EXT_SOURCE_2",
    color="TARGET",
    title="EXT_SOURCE_1 vs EXT_SOURCE_2"
)

st.plotly_chart(fig, use_container_width=True)

# EXT_SOURCE_2 vs EXT_SOURCE_3
st.subheader("🔍 EXT_SOURCE_2 vs EXT_SOURCE_3")

fig = px.scatter(
    sample,
    x="EXT_SOURCE_2",
    y="EXT_SOURCE_3",
    color="TARGET",
    title="EXT_SOURCE_2 vs EXT_SOURCE_3"
)

st.plotly_chart(fig, use_container_width=True)

# External Score vs Default Rate
st.subheader("⚠️ External Score vs Default Rate")

df["Score Group"] = pd.cut(
    df["Average_External_Score"],
    bins=[0, 0.2, 0.4, 0.6, 0.8, 1],
    labels=[
        "Very Low",
        "Low",
        "Medium",
        "High",
        "Very High"
    ]
)

score_risk = (
    df.groupby("Score Group", observed=False)["TARGET"]
    .mean()
    .reset_index()
)

score_risk["Default Rate"] = score_risk["TARGET"] * 100

fig = px.bar(
    score_risk,
    x="Score Group",
    y="Default Rate",
    color="Default Rate",
    text="Default Rate",
    title="Default Rate by Average External Score"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)