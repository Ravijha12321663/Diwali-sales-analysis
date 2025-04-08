#Problem Statement 1: Customer Demographics Analysis
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df=pd.read_csv(r"C:\Users\ravij\OneDrive\Desktop\Python project\Diwali Sales Data 2.csv")
#Objective 1.1: Gender Distribution of Customers
df_clean = df.dropna(subset=['Amount'])
df_clean['Amount'] = df_clean['Amount'].astype(float)
plt.figure(figsize=(5,4))
df_clean['Gender'].value_counts().plot(kind='bar', title='Gender Distribution', color=['skyblue', 'lightgreen'])
plt.xlabel('Gender')
plt.ylabel('Count')
plt.tight_layout()
plt.show()
#Objective 1.2: Age Group Distribution
df_clean = df.dropna(subset=['Amount'])
df_clean['Amount'] = df_clean['Amount'].astype(float)
plt.figure(figsize=(6,6))
df_clean['Age Group'].value_counts().plot(kind='pie', autopct='%1.1f%%', title='Age Group Distribution')
plt.ylabel('')
plt.tight_layout()
plt.show()
#Objective 1.3: Marital Status Breakdown
df_clean = df.dropna(subset=['Amount'])
df_clean['Amount'] = df_clean['Amount'].astype(float)
plt.figure(figsize=(5,4))
df_clean['Marital_Status'].value_counts().plot(kind='bar', title='Marital Status Count', color=['orange', 'cyan'])
plt.xlabel('Marital Status (0 = Single, 1 = Married)')
plt.ylabel('Count')
plt.tight_layout()
plt.show()
#Objective 1.4: State-wise Customer Count
df_clean = df.dropna(subset=['Amount'])
df_clean['Amount'] = df_clean['Amount'].astype(float)
plt.figure(figsize=(10,5))
df_clean['State'].value_counts().head(10).plot(kind='bar', title='Top 10 States by Customer Count', color='orchid')
plt.xlabel('State')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


