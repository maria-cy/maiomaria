from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib
import math
import json  # Flyttad hit för att undvika E402-fel


# Ladda datasetet
data = load_diabetes(as_frame=True)

X = data.frame.drop(columns=["target"])  # de 10 features
y = data.frame["target"]                 # sjukdomsprogression

# Dela upp i train och test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Skala data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Träna modell
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Utvärdera modell
y_pred = model.predict(X_test_scaled)
rmse = math.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE: {rmse:.2f}")

# Spara modellen
joblib.dump({"model": model, "scaler": scaler}, "app/model.joblib")

# Spara metrics (för CI artefakt)
metrics = {"rmse": rmse}
with open("metrics.json", "w") as f:
    json.dump(metrics, f)
