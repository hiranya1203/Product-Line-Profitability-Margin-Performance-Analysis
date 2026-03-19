import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(
    page_title="Nassau Candy Profitability Dashboard",
    layout="wide"
)

# Dashboard Title
st.title("Nassau Candy Distributor Profitability Dashboard")

st.markdown("""
Product Line Profitability & Margin Performance Analysis  
This dashboard analyzes product profitability, division performance,
cost diagnostics, and profit concentration.
""")

# Load Dataset
df = pd.read_csv(r"cleaned_nassau_sales.csv")

# Sidebar Filters
st.sidebar.header("Dashboard Filters")

division = st.sidebar.selectbox(
    "Select Division",
    ["All"] + list(df["Division"].unique())
)

product = st.sidebar.selectbox(
    "Select Product",
    ["All"] + list(df["Product Name"].unique())
)

# Apply Filters
filtered_df = df.copy()

if division != "All":
    filtered_df = filtered_df[filtered_df["Division"] == division]

if product != "All":
    filtered_df = filtered_df[filtered_df["Product Name"] == product]

# KPI Calculations
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Gross Profit"].sum()
avg_margin = (total_profit / total_sales) * 100

# KPI Row
col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Average Margin", f"{avg_margin:.2f}%")

st.markdown("---")

# =============================
# Product Profitability Chart
# =============================

product_profit = (
    filtered_df.groupby("Product Name")["Gross Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig_product, ax = plt.subplots(figsize=(6,4))

sns.barplot(
    x=product_profit.values,
    y=product_profit.index,
    ax=ax
)

ax.set_title("Top Products by Profit")
ax.set_xlabel("Profit")
ax.set_ylabel("Product")

# =============================
# Division Performance
# =============================

division_perf = (
    filtered_df.groupby("Division")[["Sales","Gross Profit"]]
    .sum()
)

fig_division, ax2 = plt.subplots(figsize=(6,4))

division_perf.plot(kind="bar", ax=ax2)

ax2.set_title("Revenue vs Profit by Division")
ax2.set_ylabel("Amount")

# =============================
# Cost vs Sales Diagnostics
# =============================

cost_analysis = (
    filtered_df.groupby("Product Name")[["Sales","Cost"]]
    .sum()
    .reset_index()
)

fig_cost, ax3 = plt.subplots(figsize=(6,4))

sns.scatterplot(
    data=cost_analysis,
    x="Cost",
    y="Sales",
    ax=ax3
)

ax3.set_title("Cost vs Sales Diagnostic")

# =============================
# Pareto Analysis
# =============================

product_profit_full = (
    filtered_df.groupby("Product Name")["Gross Profit"]
    .sum()
    .sort_values(ascending=False)
)

pareto = product_profit_full.cumsum() / product_profit_full.sum() * 100

fig_pareto, ax4 = plt.subplots(figsize=(6,4))

product_profit_full.plot(kind="bar", ax=ax4)

ax5 = ax4.twinx()

pareto.plot(ax=ax5, color="red", marker="o")

ax4.set_title("Pareto Analysis – Profit Contribution")
ax5.set_ylabel("Cumulative Profit %")

# =============================
# Dashboard Layout (2x2 Grid)
# =============================

col1, col2 = st.columns(2)

with col1:
    st.pyplot(fig_product)

with col2:
    st.pyplot(fig_division)

col3, col4 = st.columns(2)

with col3:
    st.pyplot(fig_cost)

with col4:
    st.pyplot(fig_pareto)

# Footer
st.markdown("---")

st.markdown(
"""
**Project:** Product Line Profitability & Margin Performance Analysis – Nassau Candy Distributor  

Tools Used: Python, Pandas, Matplotlib, Seaborn, Streamlit
"""
)
