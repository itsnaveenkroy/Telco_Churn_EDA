# 📞 Telco Customer Churn – Exploratory Data Analysis (EDA)

## 📘 Project Overview
This project explores the **Telco Customer Churn dataset**, which contains detailed information about telecom customers, their demographics, subscribed services, and billing details.  
The primary objective is to analyze customer churn and extract insights that can help the business improve **customer retention** and reduce **churn rate**.

---

## 🧩 Problem Statement
The business objective is to analyze **customer churn** in a telecommunications dataset and provide actionable insights that can help **retain customers**.

Each row in the dataset represents a customer with information on:
- **Demographics:** gender, senior citizen, partner, dependents  
- **Services Subscribed:** phone, internet, streaming, online security, backups, device protection, tech support, etc.  
- **Account Details:** tenure, contract type, payment method, billing, and charges  
- **Target Column:** `Churn` → Yes (customer left) / No (customer stayed)

---

## 🎯 EDA Goals
The goal of this EDA is to answer key business questions such as:
1. What is the **overall churn rate**, and how does it vary across demographics, services, and contracts?  
2. How do **billing patterns** (monthly charges, total charges, payment methods) relate to churn?  
3. Is there a **critical tenure period** where churn is highest?  
4. Which **service combinations or customer segments** show the highest and lowest churn?  
5. Are there any **missing values or outliers** that could affect the analysis?

---

## 📊 Steps Performed

### 1. **Data Understanding**
- Loaded and explored the Telco dataset  
- Checked data types, shape, and column summaries  
- Identified categorical and numerical features  
- Verified presence of missing or inconsistent values  

### 2. **Data Cleaning**
- Handled missing values (e.g., `TotalCharges` column)  
- Converted data types where necessary  
- Removed duplicates and corrected inconsistent categories  

### 3. **Exploratory Data Analysis (EDA)**
- **Univariate Analysis:** Distributions of demographics and services  
- **Bivariate Analysis:** Relationship between churn and categorical variables  
- **Correlation Analysis:** Using heatmaps for numerical variables  
- **Outlier Detection:** Boxplots for monthly and total charges  
- **Visualizations:** Bar charts, pie charts, scatter plots, and heatmaps  

### 4. **Insights and Observations**
- Higher churn observed among **month-to-month** contract customers  
- Customers with **electronic check payments** showed higher churn tendency  
- **Senior citizens** and **single customers** churn more frequently  
- Customers with **multiple services and longer tenure** have higher retention  
- Higher **monthly charges** are linked to higher churn risk  

---

## 📈 Visualizations
Key visualization types used:
- Bar charts and count plots (for categorical analysis)  
- Boxplots and scatter plots (for numerical patterns)  
- Heatmaps (for correlation)  
- Distribution plots (for charge-based insights)

---

## ⚙️ Tools and Libraries
- **Python 3.x**
- **Pandas**, **NumPy**
- **Matplotlib**, **Seaborn**
- **Google Colab / Jupyter Notebook**

---

## 🚀 How to Run
1. Open the notebook: [Insert your Colab link here]  
2. Upload or link the dataset (`Telco-Customer-Churn.csv`)  
3. Run the cells sequentially to reproduce the EDA and visualizations.

---

## 📁 File Description
| File Name | Description |
|------------|--------------|
| `Telco_Churn_EDA.ipynb` | Colab notebook containing the full EDA |
| `Telco-Customer-Churn.csv` | Dataset containing customer details |
| `README.md` | Project overview and documentation |

---

