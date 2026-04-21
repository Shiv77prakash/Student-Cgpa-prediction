from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import os
import joblib
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'student_performance_dataset_1000.csv')

GRAPH_PATH = os.path.join(BASE_DIR, 'static', 'graph.png')
FEATURE_PATH = os.path.join(BASE_DIR, 'static', 'feature.png')

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None

    if request.method == 'POST':
        # Load dataset
        df = pd.read_csv(DATA_PATH)

        X = df.iloc[:, :-1]
        y = df.iloc[:, -1]

        # Train better model
        MODEL_PATH = os.path.join(BASE_DIR, 'models', 'student_model.pkl')
        model = joblib.load(MODEL_PATH)
        model.fit(X, y)

        # Get user input
        study = float(request.form['study'])
        attendance = float(request.form['attendance'])
        previous = float(request.form['previous'])
        practice = float(request.form['practice'])
        distraction = float(request.form['distraction'])

        features = np.array([[study, attendance, previous, practice, distraction]])

        prediction = model.predict(features)[0]

        # 📊 Graph: StudyHours vs Score
        plt.figure()
        plt.scatter(df['StudyHours'], df['FinalScore'])
        plt.xlabel("Study Hours")
        plt.ylabel("Final Score")
        plt.title("Study Hours vs Score")
        plt.savefig(GRAPH_PATH)
        plt.close()

        # 📈 Feature Importance
        importance = model.feature_importances_
        cols = X.columns

        plt.figure()
        plt.bar(cols, importance)
        plt.title("Feature Importance")
        plt.xticks(rotation=30)
        plt.savefig(FEATURE_PATH)
        plt.close()

    return render_template('home.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)