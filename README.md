# Product-Line-Profitability-Margin-Performance-Analysis
### Nassau Candy Distributor

This project analyzes product-level profitability, cost efficiency, and division performance for Nassau Candy Distributor. The goal is to identify high-performing products, detect margin risks, and provide actionable insights for pricing, sourcing, and product strategy.

# Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- VS Code

# Problem Statement

For distributors like Nassau Candy, high sales volume does not always translate into strong profitability. Some products:

- Generate large revenue but have low margins
- Consume disproportionate production costs
- Appear successful but weaken overall profitability

Without detailed profitability insights, strategic decisions on pricing, promotions, and product portfolio management become reactive rather than data-driven.

This project addresses these challenges by performing a comprehensive profitability analysis across products, divisions, and geographic markets.

# Dataset Overview

The dataset contains transaction-level sales information including:

- Order Date
- Ship Date
- Product Name
- Division
- Sales
- Units Sold
- Cost
- Gross Profit
- Region
- State
- City

The dataset contains over **10,000 records** covering multiple product categories and geographic markets.

# Analytical Methodology

The analysis was conducted in multiple stages.

## Data Cleaning

- Converted date columns to proper datetime format
- Checked for missing values and duplicates
- Standardized product and division labels
- Created a cleaned dataset for analysis

## Feature Engineering

KPI metrics were created:

- **Gross Margin (%)** = Gross Profit / Sales
- **Profit per Unit**
- **Revenue Contribution**
- **Profit Contribution**

# Key Analysis Sections

## Product Profitability Analysis

Evaluated product performance based on:

- Total revenue
- Gross profit
- Profit margins

Identified:

- Top profit generating products
- High margin products
- Low margin risk products

## Division Performance Analysis

Compared divisions based on:

- Revenue
- Profit
- Margin efficiency

This helps identify which product categories contribute most to overall profitability.

## Pareto Analysis (Profit Concentration)

Applied the **Pareto principle (80/20 rule)** to identify the most important profit drivers.

Result:

> Approximately **4 products generate around 77% of total profit**, indicating strong profit concentration.

## Cost Structure Diagnostics

Analyzed the relationship between **production cost and revenue**.

This helped identify:

- Cost-heavy products
- Pricing inefficiencies
- Products with strong cost efficiency

## Geographic Profitability Analysis

Analyzed sales performance across regions, states, and cities.

Key findings:

- The **Pacific region** generates the highest revenue and profit.
- **California** is the top-performing state.
- Major cities such as **New York City, Los Angeles, and Philadelphia** contribute significantly to profitability.

# Key Business Insights

- Chocolate products dominate profitability and revenue generation.
- A small number of products contribute the majority of total profit.
- Certain products (e.g., Kazookles) show significantly lower margin efficiency.
- High-performing geographic markets are concentrated in major metropolitan regions.

These insights can support better decision-making for:

- Pricing strategies
- Marketing focus
- Inventory management
- Product portfolio optimization.

---

# Interactive Dashboard

A Streamlit dashboard was developed to make the analysis interactive.

The dashboard includes:

- KPI metrics (Revenue, Profit, Margin)
- Product profitability charts
- Division performance comparison
- Cost vs Sales diagnostics
- Pareto profit analysis

# Dashboard Preview

### Overview

![Dashboard Overview](images/dashboard_overview.png)

### Profit Diagnostics

![Dashboard Diagnostics](images/dashboard_diagnostics.png)

### Interactive Filters

![Dashboard Filters](images/dashboard_filter.png)



