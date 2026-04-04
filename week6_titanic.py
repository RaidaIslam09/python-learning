# ========================================
# Week 6 : Titanic Dataset Analysis
# Author : Raida Tasnim Islam
# ========================================

# --- Business Question ---
# 1. How does fare correlation with passenger class and embarkation port?
# 2. Which demographics predict survival?
# 3. How did cabin class impact survival rates 
# ===========================================

import pandas as pd
import numpy as np

# --- Load the dataset ---
df = pd.read_csv (r"C:\Users\Raida\Documents\python-learning\titanic.csv")

# --- First look ---
print("Shape:", df.shape)
print()
print("First 5 rows:")
print(df.head())
print()
print("Column Information:")
print()
print("Missing Values:")
print(df.isnull().sum())
print()

