from model3_evaluation import calculate_metrics

def improve_model():
    # BEFORE improvement
    actual_items = ["I1", "I2", "I3"]
    old_recommendations = ["I1", "I4", "I5"]

    p1, r1, f1_1 = calculate_metrics(actual_items, old_recommendations)

    print("---- BEFORE IMPROVEMENT ----")
    print("Precision:", round(p1, 2))
    print("Recall:", round(r1, 2))
    print("F1-Score:", round(f1_1, 2))

    # AFTER improvement
    new_recommendations = ["I1", "I2", "I3"]

    p2, r2, f1_2 = calculate_metrics(actual_items, new_recommendations)

    print("\n---- AFTER IMPROVEMENT ----")
    print("Precision:", round(p2, 2))
    print("Recall:", round(r2, 2))
    print("F1-Score:", round(f1_2, 2))


if __name__ == "__main__":
    improve_model()