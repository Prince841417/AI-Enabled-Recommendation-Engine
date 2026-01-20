"""
Milestone 3 – Model Improvement
Objective:
- Improve recommendation quality
- Compare metrics BEFORE and AFTER improvement
"""

from model3_evaluation import calculate_metrics


def generate_recommendations(user, all_items, top_k=3):
    """
    Dummy recommendation logic
    (simulate improvement by changing top_k)
    """
    return all_items[:top_k]


def improve_model():
    # -----------------------------
    # Sample data (demo purpose)
    # -----------------------------
    user = "U1"

    actual_items = ["I1", "I2", "I3", "I4", "I5"]
    all_items = ["I1", "I2", "I3", "I4", "I5", "I6", "I7"]

    # -----------------------------
    # BEFORE Improvement (Top-3)
    # -----------------------------
    recommended_before = generate_recommendations(user, all_items, top_k=3)
    p1, r1, f1_1 = calculate_metrics(actual_items, recommended_before)

    print("----- BEFORE IMPROVEMENT -----")
    print("Recommendations:", recommended_before)
    print("Precision:", round(p1, 2))
    print("Recall:", round(r1, 2))
    print("F1-Score:", round(f1_1, 2))

    # -----------------------------
    # AFTER Improvement (Top-5)
    # -----------------------------
    recommended_after = generate_recommendations(user, all_items, top_k=5)
    p2, r2, f1_2 = calculate_metrics(actual_items, recommended_after)

    print("\n----- AFTER IMPROVEMENT -----")
    print("Recommendations:", recommended_after)
    print("Precision:", round(p2, 2))
    print("Recall:", round(r2, 2))
    print("F1-Score:", round(f1_2, 2))


# -----------------------------
# Run Improvement
# -----------------------------
if __name__ == "__main__":
    improve_model()
