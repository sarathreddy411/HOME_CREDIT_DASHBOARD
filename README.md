# HOME_CREDIT_DASHBOARD
Home Credit Dashboard using Python and Streamlit
# 🏦 Home Credit Dashboard

An interactive data analytics dashboard built using **Python and Streamlit** to analyze customer loan applications, credit behavior, income, demographics, employment, education, external credit scores, and loan default risk.

---

## 📌 Project Overview

The **Home Credit Dashboard** is an interactive data analytics project developed using the Home Credit application dataset.

The main purpose of this project is to analyze customer loan application data and identify patterns related to loan defaults.

The dashboard provides multiple analytical views covering customer demographics, income, credit amount, education, employment, external credit scores, and customer-level risk.

---

## 🎯 Project Objectives

- Analyze customer loan applications
- Understand patterns associated with loan defaults
- Compare default and non-default customers
- Analyze customer income and credit behavior
- Study demographic characteristics of customers
- Analyze education and employment patterns
- Analyze external credit scores
- Explore customer-level risk characteristics
- Present analytical insights through interactive dashboards

---

## 📊 Dashboard Features

### 1. Executive Overview

Provides an overall summary of the dataset using key performance indicators and visualizations.

Key metrics include:

- Total Applications
- Default Customers
- Non-Default Customers
- Default Rate
- Total Credit Amount
- Average Credit Amount
- Average Income
- Average Annuity

---

### 2. Default Analysis

Analyzes customer default behavior.

Includes:

- Default vs Non-Default Customers
- Default Rate
- Customer distribution
- Gender analysis
- Contract type analysis
- Income type analysis

---

### 3. Age Analysis

Analyzes customer age and its relationship with loan default behavior.

Includes:

- Age distribution
- Age groups
- Default rate by age group
- Customer distribution across age groups

---

### 4. Income Analysis

Analyzes customer income patterns.

Includes:

- Income distribution
- Income categories
- Average income
- Income vs default
- Income patterns across customer groups

---

### 5. Credit Analysis

Analyzes customer credit and loan information.

Includes:

- Credit amount distribution
- Average credit amount
- Annuity analysis
- Credit vs income
- Credit behavior across customer groups

---

### 6. Income vs Credit Analysis

Analyzes the relationship between customer income and credit amount.

Includes:

- Income vs credit relationship
- Customer segmentation
- Credit patterns across income groups
- Default behavior across income and credit levels

---

### 7. Education Analysis

Analyzes customer education levels.

Includes:

- Education distribution
- Education vs default
- Default rate by education level
- Customer distribution by education

---

### 8. Employment Analysis

Analyzes customer employment characteristics.

Includes:

- Employment duration
- Employment categories
- Income type
- Employment vs default
- Customer distribution by employment characteristics

---

### 9. External Score Analysis

Analyzes external credit score information.

Includes:

- External score distributions
- Score categories
- External score vs default
- Risk patterns based on external scores

---

### 10. Customer Risk Explorer

Provides customer-level risk analysis.

Includes:

- Customer information
- Credit information
- Income information
- External scores
- Default status
- Customer risk characteristics

---

## 📈 Key Performance Indicators

| KPI | Value |
|---|---:|
| Total Applications | 307,511 |
| Default Customers | 24,825 |
| Non-Default Customers | 282,686 |
| Default Rate | 8.07% |
| Total Credit Amount | 184,207,084,195.50 |
| Average Credit Amount | 599,026.00 |
| Average Income | 168,797.92 |
| Average Annuity | 27,108.57 |

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Plotly

### Dashboard

- Streamlit

### Version Control

- Git
- GitHub

### Development Environment

- Visual Studio Code

---

## 📁 Project Structure

```text
home_credit_dashboard/
│
├── app.py
│
├── pages/
│   ├── 01_Executive_Overview.py
│   ├── 02_Default_Analysis.py
│   ├── 03_Age_Analysis.py
│   ├── 04_Income_Analysis.py
│   ├── 05_Credit_Analysis.py
│   ├── 06_Income_vs_Credit.py
│   ├── 07_Education_Analysis.py
│   ├── 08_Employment_Analysis.py
│   ├── 09_External_Score_Analysis.py
│   ├── 10_Customer_Risk_Explorer.py
│   └── ...
│
├── data/
│   └── application_train.csv
│
├── screenshots/
│   ├── executive_overview.png
│   ├── default_analysis.png
│   ├── age_analysis.png
│   ├── income_analysis.png
│   ├── credit_analysis.png
│   ├── external_score_analysis.png
│   └── customer_risk.png
│
├── .gitignore
├── README.md
└── requirements.txt