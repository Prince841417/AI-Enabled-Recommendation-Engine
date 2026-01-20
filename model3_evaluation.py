import numpy as np

def precision_recall_f1(recommended, relevant):
    recommended = set(recommended)
    relevant = set(relevant)

    tp = len(recommended & relevant)
    fp = len(recommended - relevant)
    fn = len(relevant - recommended)

    precision = tp / (tp + fp) if tp + fp > 0 else 0
    recall = tp / (tp + fn) if tp + fn > 0 else 0
    f1 = (2 * precision * recall / (precision + recall)) if precision + recall > 0 else 0

    return precision, recall, f1


# Example (demo purpose)
recommended_items = ["Books", "Electronics", "Home & Kitchen"]
actual_items = ["Books", "Health & Beauty"]

p, r, f = precision_recall_f1(recommended_items, actual_items)

print("Precision:", round(p, 2))
print("Recall:", round(r, 2))
print("F1-Score:", round(f, 2))hpo