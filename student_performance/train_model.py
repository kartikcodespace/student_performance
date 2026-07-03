"""
=============================================================
  train_model.py — Student Performance Prediction System
  Author  : AI/ML Mini Project
  Purpose : Load data, train a Linear Regression model,
            evaluate accuracy, and save artefacts to disk.
=============================================================
"""

import os
import pickle
import warnings

import matplotlib
matplotlib.use("Agg")          # non-interactive backend (no display needed)
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────
# 1. PATHS
# ─────────────────────────────────────────────
BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "student_data.csv")
MODEL_DIR   = os.path.join(BASE_DIR, "model")
STATIC_DIR  = os.path.join(BASE_DIR, "static", "images")

os.makedirs(MODEL_DIR,  exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)

# ─────────────────────────────────────────────
# 2. LOAD DATASET
# ─────────────────────────────────────────────
print("📂  Loading dataset …")
df = pd.read_csv(DATASET_PATH)
print(f"    Shape : {df.shape}")
print(df.head())
print(df.info())

# ─────────────────────────────────────────────
# 3. HANDLE MISSING VALUES
# ─────────────────────────────────────────────
print("\n🔍  Checking for missing values …")
print(df.isnull().sum())

# Fill numeric columns with their median to stay robust to outliers
for col in df.select_dtypes(include=[np.number]).columns:
    df[col].fillna(df[col].median(), inplace=True)

print("    ✅  Missing values handled.")

# ─────────────────────────────────────────────
# 4. FEATURE / TARGET SPLIT
# ─────────────────────────────────────────────
FEATURES = [
    "study_hours",
    "attendance_percentage",
    "sleep_hours",
    "previous_marks",
    "assignments_completed",
    "screen_time",
]
TARGET = "final_marks"

X = df[FEATURES]
y = df[TARGET]

# ─────────────────────────────────────────────
# 5. TRAIN / TEST SPLIT
# ─────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\n📊  Train size : {len(X_train)}  |  Test size : {len(X_test)}")

# ─────────────────────────────────────────────
# 6. FEATURE SCALING
# ─────────────────────────────────────────────
scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc  = scaler.transform(X_test)

# ─────────────────────────────────────────────
# 7. TRAIN LINEAR REGRESSION
# ─────────────────────────────────────────────
print("\n🤖  Training Linear Regression model …")
model = LinearRegression()
model.fit(X_train_sc, y_train)
print("    ✅  Training complete.")

# ─────────────────────────────────────────────
# 8. EVALUATE MODEL
# ─────────────────────────────────────────────
y_pred = model.predict(X_test_sc)

r2  = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"\n📈  Model Performance")
print(f"    R² Score : {r2:.4f}  ({r2*100:.2f}%)")
print(f"    MAE      : {mae:.4f}")
print(f"    MSE      : {mse:.4f}")
print(f"    RMSE     : {rmse:.4f}")

# Save metrics for app.py to display
metrics = {"r2": round(r2, 4), "mae": round(mae, 4), "rmse": round(rmse, 4)}
with open(os.path.join(MODEL_DIR, "metrics.pkl"), "wb") as f:
    pickle.dump(metrics, f)

# ─────────────────────────────────────────────
# 9. SAVE MODEL & SCALER
# ─────────────────────────────────────────────
with open(os.path.join(MODEL_DIR, "model.pkl"),  "wb") as f:
    pickle.dump(model,  f)
with open(os.path.join(MODEL_DIR, "scaler.pkl"), "wb") as f:
    pickle.dump(scaler, f)
with open(os.path.join(MODEL_DIR, "features.pkl"), "wb") as f:
    pickle.dump(FEATURES, f)

print("\n💾  Model, scaler, and features saved to /model/")

# ─────────────────────────────────────────────
# 10. VISUALIZATIONS
# ─────────────────────────────────────────────
sns.set_theme(style="darkgrid", palette="muted")

# ── 10a. Study Hours vs Final Marks ──────────
fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(df["study_hours"], df["final_marks"],
           color="#4f46e5", alpha=0.7, edgecolors="white", linewidth=0.5, s=70)
m, b = np.polyfit(df["study_hours"], df["final_marks"], 1)
xs = np.linspace(df["study_hours"].min(), df["study_hours"].max(), 200)
ax.plot(xs, m * xs + b, color="#f59e0b", linewidth=2.5, label="Trend line")
ax.set_title("Study Hours vs Final Marks", fontsize=15, fontweight="bold", pad=12)
ax.set_xlabel("Study Hours / Day", fontsize=12)
ax.set_ylabel("Final Marks", fontsize=12)
ax.legend()
plt.tight_layout()
plt.savefig(os.path.join(STATIC_DIR, "study_vs_marks.png"), dpi=120)
plt.close()

# ── 10b. Attendance vs Performance ───────────
fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(df["attendance_percentage"], df["final_marks"],
           color="#10b981", alpha=0.7, edgecolors="white", linewidth=0.5, s=70)
m, b = np.polyfit(df["attendance_percentage"], df["final_marks"], 1)
xs = np.linspace(df["attendance_percentage"].min(), df["attendance_percentage"].max(), 200)
ax.plot(xs, m * xs + b, color="#ef4444", linewidth=2.5, label="Trend line")
ax.set_title("Attendance % vs Final Marks", fontsize=15, fontweight="bold", pad=12)
ax.set_xlabel("Attendance (%)", fontsize=12)
ax.set_ylabel("Final Marks", fontsize=12)
ax.legend()
plt.tight_layout()
plt.savefig(os.path.join(STATIC_DIR, "attendance_vs_marks.png"), dpi=120)
plt.close()

# ── 10c. Correlation Heatmap ─────────────────
fig, ax = plt.subplots(figsize=(9, 7))
corr = df.corr(numeric_only=True)
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(
    corr, mask=mask, annot=True, fmt=".2f",
    cmap="coolwarm", center=0, linewidths=0.5,
    annot_kws={"size": 10}, ax=ax
)
ax.set_title("Feature Correlation Heatmap", fontsize=15, fontweight="bold", pad=12)
plt.tight_layout()
plt.savefig(os.path.join(STATIC_DIR, "correlation_heatmap.png"), dpi=120)
plt.close()

print("📊  Visualisations saved to /static/images/")
print("\n✅  Training pipeline complete. Run  python app.py  to start the web app.")
