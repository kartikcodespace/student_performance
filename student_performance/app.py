"""
=============================================================
  app.py — Student Performance Prediction System
  Author  : AI/ML Mini Project
  Purpose : Flask web application – serves the UI, handles
            prediction requests, and renders results.
=============================================================
"""

import os
import pickle

import numpy as np
from flask import Flask, redirect, render_template, request, url_for

# ─────────────────────────────────────────────
# 1. FLASK APP SETUP
# ─────────────────────────────────────────────
app = Flask(__name__)

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR  = os.path.join(BASE_DIR, "model")


# ─────────────────────────────────────────────
# 2. LOAD MODEL ARTEFACTS  (loaded once at startup)
# ─────────────────────────────────────────────
def load_artefacts():
    """Load the trained model, scaler, feature list, and metrics from disk."""
    try:
        with open(os.path.join(MODEL_DIR, "model.pkl"),   "rb") as f:
            model = pickle.load(f)
        with open(os.path.join(MODEL_DIR, "scaler.pkl"),  "rb") as f:
            scaler = pickle.load(f)
        with open(os.path.join(MODEL_DIR, "features.pkl"), "rb") as f:
            features = pickle.load(f)
        with open(os.path.join(MODEL_DIR, "metrics.pkl"), "rb") as f:
            metrics = pickle.load(f)
        return model, scaler, features, metrics
    except FileNotFoundError:
        return None, None, None, None


model, scaler, FEATURES, metrics = load_artefacts()


# ─────────────────────────────────────────────
# 3. HELPER — PERFORMANCE CLASSIFICATION
# ─────────────────────────────────────────────
def classify_performance(marks: float) -> dict:
    """Return grade label, colour, and an emoji for a given mark."""
    if marks >= 90:
        return {"label": "Excellent 🏆", "color": "#10b981", "badge": "success"}
    elif marks >= 75:
        return {"label": "Good 👍",       "color": "#4f46e5", "badge": "primary"}
    elif marks >= 50:
        return {"label": "Average 📘",    "color": "#f59e0b", "badge": "warning"}
    else:
        return {"label": "Poor ⚠️",       "color": "#ef4444", "badge": "danger"}


# ─────────────────────────────────────────────
# 4. ROUTES
# ─────────────────────────────────────────────

@app.route("/")
def home():
    """Home / landing page."""
    model_ready = model is not None
    return render_template("index.html", model_ready=model_ready, metrics=metrics)


@app.route("/predict", methods=["GET"])
def predict_form():
    """Render the prediction input form."""
    if model is None:
        return render_template("error.html",
                               message="Model not found. Please run train_model.py first.")
    return render_template("predict.html")


@app.route("/predict", methods=["POST"])
def predict_result():
    """
    Handle form submission:
      1. Validate & parse inputs
      2. Scale features
      3. Run prediction
      4. Classify result
      5. Render result page
    """
    if model is None:
        return render_template("error.html",
                               message="Model not found. Please run train_model.py first.")

    errors = {}

    # ── Validate each input field ──────────────
    def get_float(field, min_val, max_val, label):
        raw = request.form.get(field, "").strip()
        if not raw:
            errors[field] = f"{label} is required."
            return None
        try:
            val = float(raw)
        except ValueError:
            errors[field] = f"{label} must be a number."
            return None
        if not (min_val <= val <= max_val):
            errors[field] = f"{label} must be between {min_val} and {max_val}."
            return None
        return val

    study_hours            = get_float("study_hours",            0, 24,  "Study Hours")
    attendance_percentage  = get_float("attendance_percentage",  0, 100, "Attendance %")
    sleep_hours            = get_float("sleep_hours",            0, 24,  "Sleep Hours")
    previous_marks         = get_float("previous_marks",         0, 100, "Previous Marks")
    assignments_completed  = get_float("assignments_completed",  0, 20,  "Assignments Completed")
    screen_time            = get_float("screen_time",            0, 24,  "Screen Time")

    # If any validation failed, re-render form with errors
    if errors:
        form_values = {k: request.form.get(k, "") for k in [
            "study_hours", "attendance_percentage", "sleep_hours",
            "previous_marks", "assignments_completed", "screen_time"
        ]}
        return render_template("predict.html", errors=errors, form_values=form_values)

    # ── Build feature array & predict ──────────
    input_data = np.array([[
        study_hours, attendance_percentage, sleep_hours,
        previous_marks, assignments_completed, screen_time
    ]])

    input_scaled  = scaler.transform(input_data)
    predicted_raw = model.predict(input_scaled)[0]

    # Clamp to [0, 100]
    predicted_marks = round(float(np.clip(predicted_raw, 0, 100)), 2)

    performance = classify_performance(predicted_marks)

    # Collect student data for display on result page
    student_data = {
        "Study Hours":           study_hours,
        "Attendance (%)":        attendance_percentage,
        "Sleep Hours":           sleep_hours,
        "Previous Marks":        previous_marks,
        "Assignments Completed": assignments_completed,
        "Screen Time (hrs)":     screen_time,
    }

    return render_template(
        "result.html",
        predicted_marks = predicted_marks,
        performance     = performance,
        student_data    = student_data,
        metrics         = metrics,
    )


@app.route("/visualizations")
def visualizations():
    """Page that displays the generated charts."""
    return render_template("visualizations.html")


# ─────────────────────────────────────────────
# 5. RUN
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("🚀  Starting Student Performance Prediction System …")
    if model is None:
        print("⚠️   WARNING: Model artefacts not found.")
        print("    Run  python train_model.py  first, then restart the server.")
    else:
        print(f"✅  Model loaded | R² = {metrics['r2']}")
    app.run(debug=True, host="0.0.0.0", port=5000)
