# =====================================
# Week 4 : Pandas
# Author: Raida Tasnim Islam
# =====================================

import pandas as pd

# --- Creating a DataFrame from a dictionary ---
data = {
    "name" : ["Raida", "Sarah", "Ahmed", "John", "Maria"],
    "city" : ["Dallas", "Austin", "Raleigh", "Dallas", "Austin"],
    "sales" : [15000, 8000, 23000, 5000, 19000],
    "active" : [True, False, True, False, True]
}

df = pd.DataFrame(data)

# --- View the Dataframe ---
print(df)

# --- The 5 essential pandas commands ---
# 1. Shape - how many rows and columns
print(df.shape)

# 2. Head - see first 5 rows
print(df.head())


# 4. Describe - basic statistics on number columns
print(df.describe())

# 5. Filtering - show only active customers
active_customers = df[df["active"] == True ]
print(active_customers)

# --- Reading a real CSV file ---
df2 = pd.read_csv(r"C:\Users\Raida\Documents\python-learning\customers.csv")

print ("Shape:", df2.shape)
print()
print(df2.head())
print()
print(df2.info())

