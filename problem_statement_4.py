#Problem Statement 4: State-wise Performance Analysis
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df=pd.read_csv(r"C:\Users\ravij\OneDrive\Desktop\Python project\Diwali Sales Data 2.csv")

df_clean = df.dropna(subset=['Amount'])
df_clean['Amount'] = df_clean['Amount'].astype(float)
#Objective 4.1: Top 10 States by Total Sales
top_states = df_clean.groupby('State')['Amount'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
top_states.plot(kind='bar', color='teal')
plt.title('Top 10 States by Total Sales')
plt.ylabel('Total Sales (₹)')
plt.xlabel('State')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Objective 4.2: Top 10 States by Orders
top_states_orders = df_clean.groupby('State')['Orders'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
top_states_orders.plot(kind='bar', color='purple')
plt.title('Top 10 States by Orders')
plt.ylabel('Number of Orders')
plt.xlabel('State')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#Objective 4.3: Least Performing States
bottom_states = df_clean.groupby('State')['Amount'].sum().sort_values().head(5)
print("Least Performing States (by Revenue):")
print(bottom_states)
#Objective 4.4: Strategy for Low Performing States
bottom_states = df_clean.groupby('State')['Amount'].sum().sort_values().head(3)
print("Strategy Suggestion:")
for state in bottom_states.index:
    print(f"→ Improve visibility and promotions in {state} to boost sales.")



