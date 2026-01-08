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

# ✅ Milestone 2: Basic Recommendation Model

### Objective
To build a basic recommendation engine using collaborative filtering.

### Tasks Completed
- Used user-item matrix from Milestone 1
- Implemented basic collaborative filtering logic
- Generated item recommendations for users
- Tested recommendations on sample users
- Prepared model output for future enhancements

### Files Created
- `model2_recommendation.py`

### Output
A working basic recommendation system that suggests items based on user similarity.

---

## Project Status
- ✔ Milestone 1 completed
- ✔ Milestone 2 completed
- ⏳ Advanced modeling and optimization planned in next milestones

---

## How to Run the Project
```bash
pip install pandas numpy scikit-learn
python model1_data_preparation.py
python model2_recommendation.py
