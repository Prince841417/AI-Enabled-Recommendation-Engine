# ==============================
# Milestone 1: Data Preparation
# ==============================

import os
import pandas as pd

print("=== Milestone 1: Data Preparation Started ===")

# ------------------------------
# 1. Load dataset
# ------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "user_personalized_features.csv")

df = pd.read_csv(DATA_PATH)
print("Dataset loaded successfully")

# ------------------------------
# 2. Clean column names
# ------------------------------
df.columns = df.columns.str.strip().str.lower()
print("Columns:", list(df.columns))

# ------------------------------
# 3. Detect user column
# ------------------------------
user_col = None
for col in df.columns:
    if "user" in col and "id" in col:
        user_col = col
        break

if user_col is None:
    raise ValueError("User ID column not found")

print(f"Using user column: {user_col}")

# ------------------------------
# 4. Detect item/interest column
# ------------------------------
possible_items = ["interest", "category", "product", "preferences"]
item_col = None

for col in df.columns:
    for p in possible_items:
        if p in col:
            item_col = col
            break
    if item_col:
        break

if item_col is None:
    raise ValueError("Item/Interest column not found")

print(f"Using item column: {item_col}")

# ------------------------------
# 5. Create interaction data
# ------------------------------
interactions = df[[user_col, item_col]].copy()
interactions["rating"] = 1  # implicit feedback

# Remove duplicates
interactions.drop_duplicates(inplace=True)

# ------------------------------
# 6. Create user-item matrix
# ------------------------------
user_item_matrix = interactions.pivot_table(
    index=user_col,
    columns=item_col,
    values="rating",
    fill_value=0
)

# ------------------------------
# 7. Save matrix
# ------------------------------
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "user_item_matrix.csv")
user_item_matrix.to_csv(OUTPUT_PATH)

print("User-item matrix saved successfully")
print("Matrix shape:", user_item_matrix.shape)
print("=== Milestone 1 Completed ===")