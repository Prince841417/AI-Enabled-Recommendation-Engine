import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

print("=== Milestone 2: Model Building Started ===")

# Load user-item matrix
user_item_matrix = pd.read_csv("user_item_matrix.csv", index_col=0)
print("User-item matrix loaded")

# Compute user-user similarity
user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(
    user_similarity,
    index=user_item_matrix.index,
    columns=user_item_matrix.index
)
print("User similarity matrix created")

# Recommendation function
def recommend(user_id, top_n=3):

    if user_id not in user_item_matrix.index:
        print("User not found")
        return

    # Similarity scores
    sim_scores = user_similarity_df.loc[user_id]

    # Remove self user
    sim_scores = sim_scores.drop(user_id)

    # Align user-item matrix (VERY IMPORTANT)
    matrix_wo_user = user_item_matrix.drop(user_id)

    # Weighted sum
    weighted_scores = sim_scores.values @ matrix_wo_user.values

    scores = pd.Series(
        weighted_scores,
        index=user_item_matrix.columns
    )

    # Remove already interacted items
    already_used = user_item_matrix.loc[user_id]
    scores = scores[already_used == 0]

    return scores.sort_values(ascending=False).head(top_n)

# Test
test_user = user_item_matrix.index[0]
print(f"\nRecommendations for user {test_user}:")
print(recommend(test_user))

print("\n=== Milestone 2 Completed Successfully ===")