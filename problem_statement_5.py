#Problem Statement 5: Product Category Insights
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df=pd.read_csv(r"C:\Users\ravij\OneDrive\Desktop\Python project\Diwali Sales Data 2.csv")

#Objective 5.1: Most Purchased Product Categories
df_clean = df.dropna(subset=['Product_Category'])
category_counts = df_clean['Product_Category'].value_counts().head(10)
plt.figure(figsize=(8,5))
category_counts.plot(kind='bar', color='crimson')
plt.title('Top 10 Product Categories by Purchase Count')
plt.xlabel('Product Category')
plt.ylabel('Count')
plt.tight_layout()
plt.show()
#Objective 5.2: Revenue by Product Category
df_clean = df.dropna(subset=['Amount'])
df_clean['Amount'] = df_clean['Amount'].astype(float)
revenue_by_category = df_clean.groupby('Product_Category')['Amount'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(8,5))
revenue_by_category.plot(kind='bar', color='darkorange')
plt.title('Top Product Categories by Revenue')
plt.xlabel('Category')
plt.ylabel('Revenue (₹)')
plt.tight_layout()
plt.show()
#Objective 5.3: Top Selling Products
top_products = df['Product_ID'].value_counts().head(5)
print("Top 5 Most Purchased Products by ID:")
print(top_products)
#Objective 5.4: Strategy Based on Product Trends
top_categories = df['Product_Category'].value_counts().head(3)
print("Focus Strategy for Top Categories:")
for category in top_categories.index:
    print(f"→ Run Diwali offers and campaigns on {category}.")


