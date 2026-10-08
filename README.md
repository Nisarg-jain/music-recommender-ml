# Music Genre Recommender (Decision Tree Classifier)

An end-to-end supervised machine learning pipeline using Python, Pandas, and Scikit-Learn that predicts music preferences based on demographic attributes (age and gender).

## Workflow Highlights
1. **Data Ingestion & Preprocessing:** Loaded structured demographic data using `pandas` and separated feature matrix ($X$) from target vector ($y$).
2. **Model Training:** Fitted a `DecisionTreeClassifier` from `sklearn.tree`.
3. **Performance Evaluation:** Evaluated accuracy using `train_test_split` and `accuracy_score`.
4. **Model Persistence:** Serialized and deserialized the trained model artifact using `joblib`.

## Tech Stack
- Python
- Pandas
- Scikit-Learn
- Joblib
- Jupyter Notebook