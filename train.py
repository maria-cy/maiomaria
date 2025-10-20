import random
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, precision_score, recall_score
import joblib
import math
import json

#  Version & seeds för reproducerbarhet
version = "v0.2"
np.random.seed(42)
random.seed(42)

# Ladda data
data = load_diabetes(as_frame=True)
X = data.frame.drop(columns=["target"])
y = data.frame["target"]

#  Dela upp data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Skala data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#  Träna modell (Ridge Regression)
model = Ridge(alpha=1.0, random_state=42)
model.fit(X_train_scaled, y_train)

#  Prediktion och utvärdering
y_pred = model.predict(X_test_scaled)
rmse = math.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE (v0.2 - Ridge): {rmse:.2f}")

#  Skapa high-risk flagg
threshold = np.percentile(y_train, 75)
y_test_highrisk = (y_test > threshold).astype(int)
y_pred_highrisk = (y_pred > threshold).astype(int)

precision = precision_score(y_test_highrisk, y_pred_highrisk)
recall = recall_score(y_test_highrisk, y_pred_highrisk)

print(f"Precision (high-risk flag): {precision:.2f}")
print(f"Recall (high-risk flag): {recall:.2f}")

#  Spara modell och scaler
model_artifact = {
    "model": model,
    "scaler": scaler,
    "threshold": threshold,
    "version": version
}
joblib.dump(model_artifact, "app/model.joblib")

#  Logga metrics till JSON
metrics = {
    "version": version,
    "rmse": round(rmse, 2),
    "precision": round(precision, 2),
    "recall": round(recall, 2),
    "threshold": round(threshold, 2)
}

with open("metrics.json", "w", encoding="utf-8") as f:
    json.dump(metrics, f, indent=2)
