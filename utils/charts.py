import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def bar_chart(data, x, y, title):
    fig = px.bar(
        data,
        x=x,
        y=y,
        color=x,
        text=y,
        title=title
    )

    fig.update_traces(textposition="outside")

    return fig


def pie_chart(data, names, values, title):
    return px.pie(
        data,
        names=names,
        values=values,
        hole=0.45,
        title=title
    )


def histogram(data, column, title):
    fig, ax = plt.subplots(figsize=(8, 4))

    sns.histplot(
        data[column].dropna(),
        bins=40,
        kde=True,
        ax=ax
    )

    ax.set_title(title)
    ax.set_xlabel(column)
    ax.set_ylabel("Customers")

    return fig


def risk_bar(data, category, target, title):
    risk = (
        data.groupby(category)[target]
        .mean()
        .reset_index()
    )

    risk["Default Rate"] = risk[target] * 100

    fig = px.bar(
        risk,
        x=category,
        y="Default Rate",
        color="Default Rate",
        text="Default Rate",
        title=title
    )

    fig.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    return fig