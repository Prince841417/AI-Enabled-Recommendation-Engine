# ==============================
# Milestone 2: Recommendation Model
# Item-Based Collaborative Filtering
# ==============================

import os
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

print("=== Milestone 2: Model Building Started ===")

# --------------------------------
# Step 1: Resolve correct file path
# --------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "user_item_matrix.csv")

# --------------------------------
# Step 2: Load user-item matrix
# --------------------------------
user_item_matrix = pd.read_csv(DATA_PATH, index_col=0)
print("User-item matrix loaded successfully")
print("Matrix shape:", user_item_matrix.shape)

# --------------------------------
# Step 3: Calculate item-item similarity
# --------------------------------
item_similarity = cosine_similarity(user_item_matrix.T)

item_similarity_df = pd.DataFrame(
    item_similarity,
    index=user_item_matrix.columns,
    columns=user_item_matrix.columns
)

print("Item similarity matrix created")
print("Similarity matrix shape:", item_similarity_df.shape)

# --------------------------------
# Step 4: Recommendation function
# --------------------------------
def recommend_items(user_id, top_n=5):
    if user_id not in user_item_matrix.index:
        return "User not found"

    user_ratings = user_item_matrix.loc[user_id]
    scores = item_similarity_df.dot(user_ratings)
    scores = scores.sort_values(ascending=False)

    return scores.head(top_n)

# --------------------------------
# Step 5: Sample test
# --------------------------------
sample_user = user_item_matrix.index[0]
recommendations = recommend_items(sample_user)

print("\nRecommendations for user:", sample_user)
print(recommendations)

print("=== Milestone 2 Completed Successfully ===")