# 🏦 Home Credit Dashboard

An interactive data analytics dashboard built using **Python and Streamlit** to analyze customer loan applications, credit behavior, income, demographics, employment, education, external credit scores, regional risk, and customer-level loan default risk.

---

## 📌 Project Overview

The **Home Credit Dashboard** is an interactive data analytics project developed using the Home Credit application dataset.

The main purpose of this project is to analyze customer loan application data and identify patterns related to loan defaults.

The dashboard provides **20 analytical pages** covering customer demographics, income, credit amount, education, employment, family characteristics, housing and assets, contract information, external credit scores, regional risk, missing values, correlation between risk factors, and customer-level risk.

---

## 🎯 Project Objectives

- Analyze customer loan applications
- Understand patterns associated with loan defaults
- Compare default and non-default customers
- Analyze customer income and credit behavior
- Study demographic characteristics of customers
- Analyze education and employment patterns
- Analyze family and housing characteristics
- Analyze contract types
- Analyze external credit scores
- Identify regional risk patterns
- Analyze missing values in the dataset
- Identify correlations between risk factors
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

### 11. Education Analysis

Provides detailed analysis of customer education characteristics and their relationship with loan default risk.

Includes:

- Education levels
- Education distribution
- Education vs default
- Default rate by education level
- Customer distribution by education

---

### 12. Employment Analysis

Analyzes employment-related characteristics of customers.

Includes:

- Employment duration
- Employment categories
- Income type
- Employment vs default
- Customer distribution by employment characteristics

---

### 13. Family Analysis

Analyzes customer family-related characteristics.

Includes:

- Family status
- Number of family members
- Number of children
- Family characteristics vs default
- Customer distribution by family characteristics

---

### 14. Housing & Assets Analysis

Analyzes customer housing and asset-related characteristics.

Includes:

- Housing type
- Property characteristics
- Asset ownership
- Housing and assets vs default
- Customer distribution by housing characteristics

---

### 15. Contract Analysis

Analyzes loan contract-related information.

Includes:

- Contract types
- Contract distribution
- Contract type vs default
- Customer distribution by contract characteristics

---

### 16. External Score Analysis

Analyzes external credit score characteristics and their relationship with loan default risk.

Includes:

- External score distributions
- Score categories
- External score vs default
- Risk patterns based on external scores

---

### 17. Regional Risk Analysis

Analyzes customer and loan risk across different regions.

Includes:

- Regional distribution
- Regional default patterns
- Regional risk comparison
- Default rate by region
- Customer distribution across regions

---

### 18. Missing Value Analysis

Analyzes missing and incomplete data within the dataset.

Includes:

- Missing value counts
- Missing value percentages
- Columns with missing values
- Missing value patterns
- Data quality analysis

---

### 19. Correlation & Risk Factors Analysis

Analyzes relationships between numerical variables and customer default risk.

Includes:

- Correlation analysis
- Risk factor relationships
- Correlation matrix
- Relationship between financial variables
- Identification of important risk-related variables

---

### 20. Customer Risk Explorer

Provides detailed customer-level risk analysis.

Includes:

- Customer information
- Credit information
- Income information
- External scores
- Employment information
- Family information
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
│   ├── 11_Education_Analysis.py
│   ├── 12_Employment_Analysis.py
│   ├── 13_Family_Analysis.py
│   ├── 14_Housing_Assets.py
│   ├── 15_Contract_Analysis.py
│   ├── 16_External_Score_Analysis.py
│   ├── 17_Regional_Risk.py
│   ├── 18_Missing_Value_Analysis.py
│   ├── 19_Correlation_Risk_Factors.py
│   └── 20_Customer_Risk_Explorer.py
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