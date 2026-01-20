# AI-Enabled Recommendation Engine

## Project Overview
This project is an AI-based recommendation system that suggests items to users based on their past interactions.  
The system uses collaborative filtering techniques and is developed milestone-wise.

---

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn (basic usage)
- Git & GitHub

---

## Dataset
The dataset contains user-item interaction data:
- user_id
- item_id
- rating (implicit feedback)

---

# ✅ Milestone 1: Data Preparation & Preprocessing

### Objective
To prepare clean and structured data for building a recommendation system.

### Tasks Completed
- Loaded raw dataset into Python using Pandas
- Removed duplicate user-item interactions
- Converted implicit feedback into ratings
- Created a **User–Item Interaction Matrix**
- Handled missing values by filling zeros
- Saved processed data as CSV files

### Files Created
- `model1_data_preparation.py`
- `user_item_matrix.csv`
- `user_personalized_features.csv`

### Output
A clean and structured user-item matrix ready for recommendation modeling.

---

# Milestone 2: Model Building (AI-Enabled Recommendation Engine)

## Objective
The objective of Milestone 2 is to develop and train the core recommendation model using the processed data from Milestone 1. This milestone focuses on selecting a recommendation algorithm, training the model, and generating initial recommendations.

---

## Selected Recommendation Model
**Item-Based Collaborative Filtering**

### Why this model?
- Simple and effective for beginners
- Uses user-item interaction data
- Recommended for initial recommendation systems
- Matches mentor instruction to compute similarity and train on interaction matrix

---

## Approach Used

1. Loaded the **user-item interaction matrix** generated in Milestone 1.
2. Applied **Cosine Similarity** to compute similarity between items.
3. Created an **item similarity matrix**.
4. Developed a recommendation function that:
   - Takes a selected item
   - Finds similar items
   - Returns top-N recommended items
5. Tested the model with sample inputs.

---

## Technologies Used
- Python
- Pandas
- Scikit-learn (Cosine Similarity)

---

## Files Involved
- `model2_recommendation.py` – Model building and recommendation logic
- `user_item_matrix.csv` – Interaction matrix from Milestone 1

---

## Sample Output

```text
User-Item Matrix Loaded Successfully
Item Similarity Matrix Created
Selected Item: Apparel
Recommended Items: ['Books', 'Electronics', 'Health & Beauty', 'Home & Kitchen']
=== Milestone 2 Completed Successfully ===
----

---

## Milestone 3: Evaluation and Refinement

**Completion Date:** 28 January

### Objective
Evaluate the performance of the recommendation model and refine it to improve accuracy.

### Tasks Performed
- Calculated evaluation metrics: Precision, Recall, and F1-score
- Analyzed recommendation results
- Fine-tuned the model based on evaluation outcomes
- Tested different recommendation scenarios

### Evaluation Metrics
- **Precision:** 0.33
- **Recall:** 0.50
- **F1-Score:** 0.40

### Outcome
The model performance was validated using standard evaluation metrics.
Based on the results, the recommendation algorithm was refined to improve accuracy.
Multiple recommendation scenarios were tested to ensure robustness.
