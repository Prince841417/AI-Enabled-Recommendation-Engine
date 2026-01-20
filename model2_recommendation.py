import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

print("=== Milestone 2: Model Building Started ===")

# -----------------------------
# Step 1: Load User-Item Matrix
# -----------------------------
user_item_matrix = pd.read_csv("user_item_matrix.csv", index_col=0)
print("User-Item Matrix Loaded Successfully")
print(user_item_matrix.head())

# -------------------------------------
# Step 2: Calculate Item-Item Similarity
# -------------------------------------
item_similarity = cosine_similarity(user_item_matrix.T)

item_similarity_df = pd.DataFrame(
    item_similarity,
    index=user_item_matrix.columns,
    columns=user_item_matrix.columns
)

print("Item similarity matrix created")

# -------------------------------------
# Step 3: Recommendation Function
# -------------------------------------
def recommend_items(item_id, top_n=5):
    if item_id not in item_similarity_df.columns:
        return "Item not found" 
    

    similarity_scores = item_similarity_df[item_id]
    similar_items = similarity_scores.sort_values(ascending=False)[1:top_n+1]

    return list(similar_items.index)

# -------------------------------------
# Step 4: Test the Model
# -------------------------------------
sample_item = user_item_matrix.columns[0]

recommended_items = recommend_items(sample_item, top_n=5)

print("\nSelected Item:", sample_item)
print("Recommended Items:", recommended_items)

print("\n=== Milestone 2 Completed Successfully ===")