import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\Assignments\home_credit_dashboard\data\application_train.csv",encoding="latin1")

st.title("💳 Annuity Analysis")
st.write("Analysis of customers' annual loan payment obligations.")

avg_annuity = df["AMT_ANNUITY"].mean()
median_annuity = df["AMT_ANNUITY"].median()
max_annuity = df["AMT_ANNUITY"].max()
default_avg_annuity = df[df["TARGET"] == 1]["AMT_ANNUITY"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Average Annuity", f"{avg_annuity:,.0f}")
col2.metric("Median Annuity", f"{median_annuity:,.0f}")
col3.metric("Maximum Annuity", f"{max_annuity:,.0f}")
col4.metric("Avg Annuity - Defaulters", f"{default_avg_annuity:,.0f}")

st.divider()

st.subheader("📊 Annuity Distribution")

fig, ax = plt.subplots(figsize=(8, 4))

sns.histplot(
    df["AMT_ANNUITY"].dropna(),
    bins=40,
    kde=True,
    ax=ax
)

ax.set_xlabel("Annuity")
ax.set_ylabel("Number of Customers")

st.pyplot(fig)

# 2. ANNUITY BY TARGET

st.subheader("🎯 Annuity by Target")

target_annuity = df.groupby("TARGET")["AMT_ANNUITY"].mean().reset_index()

target_annuity["TARGET"] = target_annuity["TARGET"].map({
    0: "Non-Default",
    1: "Default"
})

fig = px.bar(
    target_annuity,
    x="TARGET",
    y="AMT_ANNUITY",
    color="TARGET",
    text="AMT_ANNUITY",
    title="Average Annuity by Customer Status"
)

fig.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# 3. ANNUITY VS INCOME
st.subheader("💰 Annuity vs Income")

sample = df.sample(
    min(10000, len(df)),
    random_state=42
)

fig = px.scatter(
    sample,
    x="AMT_INCOME_TOTAL",
    y="AMT_ANNUITY",
    color="TARGET",
    title="Annuity vs Income",
    labels={
        "AMT_INCOME_TOTAL": "Income",
        "AMT_ANNUITY": "Annuity",
        "TARGET": "Default"
    }
)

st.plotly_chart(fig, use_container_width=True)

# 4. ANNUITY VS CREDIT

st.subheader("💳 Annuity vs Credit")

fig = px.scatter(
    sample,
    x="AMT_CREDIT",
    y="AMT_ANNUITY",
    color="TARGET",
    title="Annuity vs Credit",
    labels={
        "AMT_CREDIT": "Credit Amount",
        "AMT_ANNUITY": "Annuity",
        "TARGET": "Default"
    }
)

st.plotly_chart(fig, use_container_width=True)

# 5. AVERAGE ANNUITY BY INCOME TYPE

st.subheader("💼 Average Annuity by Income Type")

income_annuity = (
    df.groupby("NAME_INCOME_TYPE")["AMT_ANNUITY"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

fig = px.bar(
    income_annuity,
    x="NAME_INCOME_TYPE",
    y="AMT_ANNUITY",
    color="AMT_ANNUITY",
    title="Average Annuity by Income Type"
)

st.plotly_chart(fig, use_container_width=True)

# 6. DEFAULT RATE BY ANNUITY GROUP

st.subheader("⚠️ Default Rate by Annuity Group")

df["Annuity Group"] = pd.qcut(
    df["AMT_ANNUITY"],
    q=5,
    labels=[
        "Very Low",
        "Low",
        "Medium",
        "High",
        "Very High"
    ]
)

annuity_risk = (
    df.groupby("Annuity Group", observed=False)["TARGET"]
    .mean()
    .reset_index()
)

annuity_risk["Default Rate"] = (
    annuity_risk["TARGET"] * 100
)

fig = px.bar(
    annuity_risk,
    x="Annuity Group",
    y="Default Rate",
    color="Default Rate",
    text="Default Rate",
    title="Default Rate by Annuity Group"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(fig, use_container_width=True)

# INSIGHTS

st.subheader("💡 Key Insights")

highest_risk_group = annuity_risk.loc[
    annuity_risk["Default Rate"].idxmax()
]

st.write(
    f"• The average annuity is **{avg_annuity:,.0f}**."
)

st.write(
    f"• Defaulters have an average annuity of "
    f"**{default_avg_annuity:,.0f}**."
)

st.write(
    f"• The **{highest_risk_group['Annuity Group']}** "
    f"annuity group has the highest default rate "
    f"of **{highest_risk_group['Default Rate']:.2f}%**."
)