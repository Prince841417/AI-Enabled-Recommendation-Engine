import pandas as pd

# Load CSV files
users = pd.read_csv("users.csv")
products = pd.read_csv("products.csv")
interactions = pd.read_csv("interactions.csv")

# Clean data
interactions.drop_duplicates(inplace=True)
interactions["interaction"] = interactions["interaction"].fillna(0)

# Create User-Item Interaction Matrix
user_item_matrix = interactions.pivot_table(
    index="user_id",
    columns="product_id",
    values="interaction",
    aggfunc="mean",
    fill_value=0
)

# Save output
user_item_matrix.to_csv("user_item_matrix.csv")

# Print output
print("✅ Milestone 1 completed successfully\n")
print(user_item_matrix)