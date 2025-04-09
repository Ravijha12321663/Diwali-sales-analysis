 #Problem Statement 2: Sales Performance Overview
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df=pd.read_csv(r"C:\Users\ravij\OneDrive\Desktop\Python project\Diwali Sales Data 2.csv")

df_clean = df.dropna(subset=['Amount'])
df_clean['Amount'] = df_clean['Amount'].astype(float)
#Objective 2.1: Total Orders
total_orders = df_clean['Orders'].sum()
print("Total Orders:", total_orders)
#Objective 2.2: Total Revenue
total_revenue = df_clean['Amount'].sum()
print("Total Revenue: ₹", total_revenue)
#Objective 2.3: Average Order Value
average_order_value = df_clean['Amount'].mean()
print("Average Order Value: ₹", round(average_order_value, 2))
# Objective 2.4: Top Product Categories by Revenue
plt.figure(figsize=(8,5))
df_clean.groupby('Product_Category')['Amount'].sum().sort_values(ascending=False).head(5).plot(kind='bar', color='salmon')
plt.title('Top 5 Product Categories by Revenue')
plt.xlabel('Product Category')
plt.ylabel('Revenue (₹)')
plt.tight_layout()
plt.show()
