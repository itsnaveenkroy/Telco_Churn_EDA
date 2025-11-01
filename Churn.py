import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(page_title="Telco Churn Dashboard", layout="wide")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("/Users/itsnaveenkroy/Documents/Codes/Churn/group2_dataset.csv")
    # Clean TotalCharges
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'] = df['TotalCharges'].fillna(0)
    # Encode churn
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
    return df

df = load_data()

# Sidebar Filters
st.sidebar.title("Filters")

gender = st.sidebar.multiselect("Gender", options=df['gender'].unique(), default=df['gender'].unique())
senior = st.sidebar.multiselect("Senior Citizen", options=df['SeniorCitizen'].unique(), default=df['SeniorCitizen'].unique())
contract = st.sidebar.multiselect("Contract Type", options=df['Contract'].unique(), default=df['Contract'].unique())
internet = st.sidebar.multiselect("Internet Service", options=df['InternetService'].unique(), default=df['InternetService'].unique())

# Applying filters
df_filtered = df[
    (df['gender'].isin(gender)) &
    (df['SeniorCitizen'].isin(senior)) &
    (df['Contract'].isin(contract)) &
    (df['InternetService'].isin(internet))
]

# Sidebar Navigation 
page = st.sidebar.radio("Go to", ["Overview", "Demographics", "Tenure Analysis", "Segments"])

# Overview
if page == "Overview":
    st.title("Telco Churn Dashboard")
    st.write("Interactive dashboard for churn analysis with custom filters.")

    st.subheader("Dataset Preview")
    st.dataframe(df_filtered.head())

    churn_rate = df_filtered['Churn'].mean() * 100
    st.metric("Overall Churn Rate (Filtered)", f"{churn_rate:.2f}%")

    # Pie chart: Churn vs Non-churn
    st.subheader("Churn Distribution")
    churn_counts = df_filtered['Churn'].value_counts()
    labels = ["Stayed", "Churned"]
    sizes = [churn_counts.get(0, 0), churn_counts.get(1, 0)]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=["#66c2a5", "#fc8d62"], startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

# Demographics
elif page == "Demographics":
    st.title("Churn by Demographics")
    demo_cols = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines']

    # Pie chart: Gender distribution
    if 'gender' in df_filtered.columns:
        st.subheader("Gender Distribution (Filtered)")
        gender_counts = df_filtered['gender'].value_counts()
        fig, ax = plt.subplots()
        ax.pie(gender_counts.values, labels=gender_counts.index, autopct='%1.1f%%', colors=sns.color_palette("pastel"))
        ax.axis('equal')
        st.pyplot(fig)

    for col in demo_cols:
        if col in df_filtered.columns:
            st.subheader(f"Churn by {col}")
            churn_by_col = df_filtered.groupby(col)['Churn'].mean().reset_index()

            fig, ax = plt.subplots(figsize=(6, 3))
            sns.barplot(x=col, y="Churn", data=churn_by_col, palette="viridis", ax=ax)
            ax.set_ylabel("Churn Rate")
            ax.set_title(f"Churn by {col}")
            st.pyplot(fig)

#  Tenure Analysis
elif page == "Tenure Analysis":
    st.title("Tenure & Churn")
    max_t = int(df_filtered['tenure'].max())
    bins = list(range(0, max_t + 12, 12))
    labels = [f"{i+1}-{i+12}" for i in bins[:-1]]
    df_filtered['tenure_bucket'] = pd.cut(df_filtered['tenure'], bins=bins, labels=labels, right=True)

    churn_by_bucket = df_filtered.groupby('tenure_bucket')['Churn'].mean().reset_index()
    st.subheader("Churn Rate by Tenure Bucket")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x='tenure_bucket', y='Churn', data=churn_by_bucket, palette="mako", ax=ax)
    plt.xticks(rotation=45)
    ax.set_ylabel("Churn Rate")
    ax.set_title("Churn by Tenure Buckets")
    st.pyplot(fig)

    st.subheader("Critical Threshold")
    churn_by_month = df_filtered.groupby('tenure')['Churn'].mean()
    overall = df_filtered['Churn'].mean()
    threshold = churn_by_month[churn_by_month < overall].index.min()
    if threshold:
        st.write(f"Churn drops below average after about **{threshold} months**.")
    else:
        st.write("No clear threshold found in filtered data.")

# Segments 
elif page == "Segments":
    st.title("Customer Segments")
    seg_cols = ['Contract', 'InternetService', 'SeniorCitizen']
    seg = df_filtered.groupby(seg_cols)['Churn'].mean().reset_index()

    st.subheader("Lowest Churn Segments")
    st.dataframe(seg.sort_values('Churn').head())

    st.subheader("Highest Churn Segments")
    st.dataframe(seg.sort_values('Churn', ascending=False).head())
