#Problem Statement 3: Gender-Based Sales Analysis
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df=pd.read_csv(r"C:\Users\ravij\OneDrive\Desktop\Python project\Diwali Sales Data 2.csv")

df_clean = df.dropna(subset=['Amount'])
df_clean['Amount'] = df_clean['Amount'].astype(float)

#Objective 3.1: Total Sales by Gender
plt.figure(figsize=(6,4))
sns.barplot(data=df_clean.groupby('Gender', as_index=False)['Amount'].sum(), x='Gender', y='Amount', palette='Set2')
plt.title('Total Sales Amount by Gender')
plt.ylabel('Total Amount (₹)')
plt.tight_layout()
plt.show()
#Objective 3.2: Order Quantity by Gender
plt.figure(figsize=(6,4))
sns.barplot(data=df_clean.groupby('Gender', as_index=False)['Orders'].sum(), x='Gender', y='Orders', palette='Set1')
plt.title('Total Orders by Gender')
plt.ylabel('Order Count')
plt.tight_layout()
plt.show()
#Objective 3.3: Average Order Value by Gender
avg_order_val_gender = df_clean.groupby('Gender')['Amount'].mean().reset_index()
plt.figure(figsize=(6,4))
sns.barplot(data=avg_order_val_gender, x='Gender', y='Amount', palette='Set3')
plt.title('Average Order Value by Gender')
plt.ylabel('Average Amount (₹)')
plt.tight_layout()
plt.show()
# Objective 3.4: Suggested Strategy Based on Gender
avg_order_val_gender = df_clean.groupby('Gender')['Amount'].mean().reset_index()
top_gender = avg_order_val_gender.sort_values(by='Amount', ascending=False).iloc[0]
print(f"Suggested Strategy: Focus more on '{top_gender['Gender']}' segment with higher average spending: ₹{round(top_gender['Amount'], 2)}")

