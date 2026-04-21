🎯 Student Performance Prediction System

A Machine Learning based web application that predicts a student's exam score based on study habits and performance metrics.

🚀 Features
📊 Predict student exam score using ML model
🤖 Uses Random Forest for better accuracy
📈 Feature Importance Visualization
📉 Graph: Study Hours vs Final Score
🌐 Flask-based web application
📱 Easily extendable to mobile apps (Flutter integration ready)
🧠 Machine Learning Model
Algorithm: Random Forest Regressor
Features Used:
Study Hours
Attendance
Previous Score
Practice Papers
Distraction Time
Target:
Final Exam Score
📂 Project Structure
exam_predictor/
│
├── app.py
├── train_model.py
│
├── data/
│   └── student_performance_dataset_1000.csv
│
├── models/
│   └── student_model.pkl
│
├── templates/
│   └── home.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   ├── graph.png
│   └── feature.png
│
└── requirements.txt
⚙️ Installation
1. Clone Repository
git clone https://github.com/your-username/student-performance-predictor.git
cd student-performance-predictor
2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
▶️ Usage
Step 1: Train Model
python train_model.py
Step 2: Run Flask App
python app.py
Step 3: Open in Browser
http://127.0.0.1:5000
📊 Output
Predicted Score displayed on UI
Graph: Study Hours vs Score
Feature Importance Chart
