import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'student_performance_dataset_1000.csv')
MODEL_FOLDER = os.path.join(BASE_DIR, 'models')

if not os.path.exists(MODEL_FOLDER):
    os.makedirs(MODEL_FOLDER)

# Load dataset
df = pd.read_csv(DATA_PATH)

# Features & Target
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model (Better than Linear Regression 🔥)
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Save model
model_path = os.path.join(MODEL_FOLDER, 'student_model.pkl')
joblib.dump(model, model_path)

# Accuracy (R² Score)
score = model.score(X_test, y_test)

print("✅ Model trained successfully!")
print(f"📁 Saved at: {model_path}")
print(f"🎯 Accuracy (R2 Score): {score:.2f}")