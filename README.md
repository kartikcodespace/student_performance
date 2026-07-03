# AI-Based Student Performance Prediction System

## Overview

The AI-Based Student Performance Prediction System is a machine learning web application that predicts a student’s final marks using academic and behavioral factors. The system uses a Linear Regression model to analyze student data and provide an estimated final score along with a performance category.

The project helps students and educators understand how factors such as study hours, attendance, sleep, previous marks, assignments, and screen time may affect academic performance.

---

## Features

* Predicts final student marks
* Uses Linear Regression machine learning model
* Accepts six student input features
* Classifies performance into four categories
* Includes input validation
* Displays model evaluation metrics
* Generates data visualization charts
* Provides a responsive Flask web interface
* Saves the trained model using Pickle

---

## Input Features

The system uses the following features for prediction:

* Study Hours
* Attendance Percentage
* Sleep Hours
* Previous Marks
* Assignments Completed
* Screen Time

---

## Performance Classification

| Predicted Marks | Performance Level |
| --------------- | ----------------- |
| 90–100          | Excellent         |
| 75–89           | Good              |
| 50–74           | Average           |
| Below 50        | Poor              |

---

## Technologies Used

* Python
* Flask
* scikit-learn
* Pandas
* NumPy
* Matplotlib
* Seaborn
* HTML
* CSS
* Bootstrap
* JavaScript

---

## Machine Learning Model

The project uses the Linear Regression algorithm to predict final marks.

The dataset is divided into training and testing data. The model is evaluated using:

* R² Score
* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)

---

## Project Structure

```text
student_performance/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
│
├── dataset/
│   └── student_data.csv
│
├── model/
│   ├── model.pkl
│   ├── scaler.pkl
│   ├── features.pkl
│   └── metrics.pkl
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── predict.html
│   ├── result.html
│   ├── visualizations.html
│   └── error.html
│
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── main.js
    └── images/
        ├── study_vs_marks.png
        ├── attendance_vs_marks.png
        └── correlation_heatmap.png
```

---

## Installation Steps

### 1. Clone or Download the Project

Download the project folder and open it in Visual Studio Code.

```bash
cd student_performance
```

### 2. Create a Virtual Environment

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Train the Machine Learning Model

Run the following command:

```bash
python train_model.py
```

This command will:

* Load the student dataset
* Handle missing values
* Train the Linear Regression model
* Evaluate model performance
* Save model files in the `model` folder
* Generate visualization charts in the `static/images` folder

### 5. Run the Flask Application

```bash
python app.py
```

### 6. Open the Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Output

The system displays:

* Predicted final marks
* Performance category
* Student input details
* Model evaluation metrics
* Academic performance visualizations

---

## Future Improvements

* Add user login and registration
* Store prediction history in MySQL
* Use Random Forest and compare results
* Add more student-related features
* Generate downloadable PDF performance reports
* Deploy the application online

---

## Learning Outcomes

Through this project, the following skills were developed:

* Data preprocessing
* Regression analysis
* Machine learning model training
* Model evaluation
* Flask web development
* Data visualization
* Input validation
* Model deployment using Pickle

---

## Author

AI/ML Mini Project
Student Performance Prediction System
