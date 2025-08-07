import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset (adjust path as needed)
@st.cache_data
def load_data():
    return pd.read_csv('data/ai_based_service_reminder.csv')

df = load_data()

st.title("Service Reminder Dashboard")

# Summary statistics
total_customers = len(df)
critical_customers = df[df['customer_segment'] == 'Critical'].shape[0]
high_priority_customers = df[df['customer_segment'] == 'High Priority'].shape[0]
medium_priority_customers = df[df['customer_segment'] == 'Medium Priority'].shape[0]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Customers", total_customers)
col2.metric("Critical Customers", critical_customers)
col3.metric("High Priority Customers", high_priority_customers)
col4.metric("Medium Priority Customers", medium_priority_customers)

# Visualization: Distribution of customers by Customer Segment
st.subheader("Customer Segment Distribution")
segment_counts = df['customer_segment'].value_counts()
fig1, ax1 = plt.subplots()
sns.barplot(x=segment_counts.index, y=segment_counts.values, palette='viridis', ax=ax1)
ax1.set_xlabel("Customer Segment")
ax1.set_ylabel("Count")
st.pyplot(fig1)

# Visualization: Service due days histogram
st.subheader("Distribution of Days Until Next Service Due")
fig2, ax2 = plt.subplots()
sns.histplot(df['next_service_due_days'], bins=30, kde=True, color='skyblue', ax=ax2)
ax2.set_xlabel("Days Until Next Service Due")
ax2.set_ylabel("Frequency")
st.pyplot(fig2)

# Filter by Customer Type and visualize count
st.subheader("Customer Count by Type")
customer_type_counts = df['customer_type'].value_counts()
fig3, ax3 = plt.subplots()
sns.barplot(x=customer_type_counts.index, y=customer_type_counts.values, palette='magma', ax=ax3)
ax3.set_xlabel("Customer Type")
ax3.set_ylabel("Count")
st.pyplot(fig3)

# Table preview of data with filters
st.subheader("Sample Customer Service Data")
filter_segment = st.multiselect("Filter by Customer Segment", options=df['customer_segment'].unique(), default=df['customer_segment'].unique())
filter_customer_type = st.multiselect("Filter by Customer Type", options=df['customer_type'].unique(), default=df['customer_type'].unique())

filtered_df = df[df['customer_segment'].isin(filter_segment) & df['customer_type'].isin(filter_customer_type)]

st.dataframe(filtered_df[['location', 'customer_type', 'make', 'model', 'year_of_purchase',
                          'feedback_score', 'next_service_due_days', 'customer_segment', 'personalized_message']].head(20))
