# ============================================
# Week 4 - Sales Data Analysis
# Author - Raida Tasnim Islam
# ============================================

import pandas as pd

# --- Look the CSV file ---
df =pd.read_csv (r"C:\Users\Raida\Documents\python-learning\sales_data.csv")

# --- First look at the Data ---
print("Shape:", df.shape)
print()
print("First 5 rows:")
print(df.head())
print()
print("Data types:")
print(df.info())
print()

# --- Basic Statistics ---
print("Sales Statistics:")
print(df.describe())
print()

# --- Filter: employee who hit their target ---
hit_target = df[df["sales"]>=df["target"]]
print("Employee who hit their target:")
print(hit_target[["employee", "department", "sales", "target"]])
print()

# --- Filter: Analytics department only ---
analytics = df[df["department"] =="Analytics"]
print("Analytics Department")
print(analytics[["employee", "region", "sales"]])
print()

# --- Average sales by department ---
print("Average sales by department:")
print(df.groupby("department")["sales"].mean())

# --- Average months employed by department ---
print("Average tenure by department(months):")
print(df.groupby("department")["months_employed"].mean())
print()

# --- sales performance gap by department ---
df["gap"] = df["sales"] - df["target"]
print("Average performance gap by department")
print(df.groupby("department")["gap"].mean())
print()

