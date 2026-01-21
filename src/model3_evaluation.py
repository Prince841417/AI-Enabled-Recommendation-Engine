def calculate_metrics(actual_items, recommended_items):
    """
    Calculates Precision, Recall and F1-Score

    actual_items       : list of actual relevant items
    recommended_items  : list of items recommended by the model
    """

    actual_set = set(actual_items)
    recommended_set = set(recommended_items)

    # True Positives
    true_positive = len(actual_set & recommended_set)

    # Precision
    if len(recommended_set) == 0:
        precision = 0
    else:
        precision = true_positive / len(recommended_set)

    # Recall
    if len(actual_set) == 0:
        recall = 0
    else:
        recall = true_positive / len(actual_set)

    # F1 Score
    if precision + recall == 0:
        f1_score = 0
    else:
        f1_score = 2 * (precision * recall) / (precision + recall)

    return precision, recall, f1_score


# ----------------- TEST / DEMO -----------------
if __name__ == "__main__":
    actual_items = ["I1", "I2", "I3"]
    recommended_items = ["I1", "I3", "I5"]

    precision, recall, f1 = calculate_metrics(actual_items, recommended_items)

    print("Precision:", round(precision, 2))
    print("Recall   :", round(recall, 2))
    print("F1-Score :", round(f1, 2))