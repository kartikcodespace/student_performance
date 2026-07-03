# 🎓 EduPredict — AI-Based Student Performance Prediction System

A complete AI/ML web application that predicts a student's final marks using
**Linear Regression** and six academic input features.

---

## 📁 Project Structure

```
student_performance/
├── app.py               # Flask web application (routes, prediction logic)
├── train_model.py       # ML pipeline: load → preprocess → train → save → visualise
├── requirements.txt     # Python dependencies
│
├── dataset/
│   └── student_data.csv # 100-row sample dataset
│
├── model/               # Created after training
│   ├── model.pkl        # Trained LinearRegression object
│   ├── scaler.pkl       # StandardScaler for feature normalisation
│   ├── features.pkl     # Ordered list of feature names
│   └── metrics.pkl      # R², MAE, RMSE dictionary
│
├── templates/           # Jinja2 HTML templates
│   ├── base.html        # Shared layout (navbar, footer)
│   ├── index.html       # Home / landing page
│   ├── predict.html     # Input form page
│   ├── result.html      # Prediction result page
│   ├── visualizations.html  # Charts page
│   └── error.html       # Error page
│
└── static/
    ├── css/
    │   └── style.css    # Custom styles (dark academic theme)
    ├── js/
    │   └── main.js      # Client-side form validation & UX
    └── images/          # Created after training
        ├── study_vs_marks.png
        ├── attendance_vs_marks.png
        └── correlation_heatmap.png
```

---

## ⚙️ Tech Stack

| Layer        | Technology                        |
|--------------|-----------------------------------|
| Backend      | Python 3.10+, Flask 3             |
| ML           | scikit-learn (LinearRegression)   |
| Data         | pandas, numpy                     |
| Charts       | matplotlib, seaborn               |
| Frontend     | HTML5, CSS3, Bootstrap 5, Jinja2  |
| Model save   | pickle                            |

---

## 🚀 Step-by-Step Setup & Run

### Step 1 — Clone / unzip the project

```bash
cd student_performance
```

### Step 2 — Create a virtual environment (recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Train the model

```bash
python train_model.py
```

This will:
- Load `dataset/student_data.csv`
- Handle missing values
- Split data 80/20 for training & testing
- Train a Linear Regression model
- Print R², MAE, RMSE to the console
- Save `model/model.pkl`, `scaler.pkl`, `features.pkl`, `metrics.pkl`
- Generate 3 PNG charts in `static/images/`

### Step 5 — Start the web server

```bash
python app.py
```

### Step 6 — Open in your browser

```
http://127.0.0.1:5000
```

---

## 🧠 Features

| Feature                  | Description                                             |
|--------------------------|---------------------------------------------------------|
| Dataset loading          | CSV → pandas DataFrame, missing values handled          |
| Linear Regression        | Trained with StandardScaler-normalised features         |
| Model persistence        | Saved/loaded with pickle                                |
| Performance grades       | Excellent / Good / Average / Poor classification        |
| Input validation         | Client-side JS + server-side Python (both layers)       |
| 3 Visualisations         | Study hours, attendance, correlation heatmap            |
| Responsive UI            | Bootstrap 5, custom dark-theme CSS, mobile-friendly     |

---

## 📊 Input Features Used for Prediction

| Feature                | Range     |
|------------------------|-----------|
| Study Hours / Day      | 0 – 24    |
| Attendance Percentage  | 0 – 100   |
| Sleep Hours / Night    | 0 – 24    |
| Previous Exam Marks    | 0 – 100   |
| Assignments Completed  | 0 – 20    |
| Screen / Internet Time | 0 – 24    |

---

## 🏅 Grade Classification

| Marks    | Grade     |
|----------|-----------|
| 90 – 100 | Excellent |
| 75 – 89  | Good      |
| 50 – 74  | Average   |
| 0 – 49   | Poor      |

---

## 🛠 Troubleshooting

**"Model not found" error**
→ Run `python train_model.py` before starting the server.

**Charts not showing**
→ Make sure `train_model.py` completed successfully and `static/images/` exists.

**Port already in use**
→ Change the port in `app.py`: `app.run(port=5001)`

---

## 📄 File Descriptions

| File               | Purpose                                                      |
|--------------------|--------------------------------------------------------------|
| `app.py`           | Flask app: routes, input validation, prediction, rendering   |
| `train_model.py`   | Full ML pipeline: data loading → training → saving → plots   |
| `dataset/student_data.csv` | 100-row synthetic student dataset                  |
| `templates/*.html` | Jinja2 page templates extending `base.html`                  |
| `static/css/style.css` | Dark academic CSS theme using CSS variables              |
| `static/js/main.js`    | Form UX: spinner on submit, live error removal           |
| `requirements.txt` | All Python package dependencies with pinned versions         |

---

Built with ❤️ as an AI/ML Mini Project using Flask & scikit-learn.
