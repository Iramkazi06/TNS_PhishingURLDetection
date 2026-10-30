# run this ONCE first: python train_model.py
import json

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, confusion_matrix)
from sklearn.model_selection import train_test_split

from backend.dataset import make_data
from backend.features import get_features, columns

df = make_data()
X = pd.DataFrame([get_features(u) for u in df["url"]], columns=columns)
y = df["label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "Logistic Regression (baseline)": LogisticRegression(max_iter=5000),
    "Random Forest": RandomForestClassifier(random_state=42),
}

results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    results[name] = {
        "accuracy": round(accuracy_score(y_test, pred), 3),
        "precision": round(precision_score(y_test, pred), 3),
        "recall": round(recall_score(y_test, pred), 3),
        "f1": round(f1_score(y_test, pred), 3),
    }
    print(name, results[name])
    if name == "Random Forest":
        cm = confusion_matrix(y_test, pred)
        print("Confusion matrix:")
        print(cm)

# save the model and the results so the app can use them
joblib.dump(models["Random Forest"], "artifacts/model.pkl")
with open("artifacts/metrics.json", "w") as f:
    json.dump({"results": results, "confusion_matrix": cm.tolist()}, f)
print("Saved to artifacts/")
