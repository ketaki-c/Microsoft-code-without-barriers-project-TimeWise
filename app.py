
from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle
import os

app = Flask(__name__)

# Example class data
class_data = [
    {"course": "Math 101", "time": "MWF 9:00-10:00"},
    {"course": "History 202", "time": "TR 11:00-12:30"}
]

# Dummy initial feedback data
feedback_data = []

# Function to generate a schedule
def generate_schedule(data):
    schedule = []
    for item in class_data:
        if is_available(item['time']):
            schedule.append(item)
    return schedule

# Function to check if a time slot is available
def is_available(time):
    # Dummy logic to check if the time slot is available
    return True

# Function to train the model on feedback data
def train_model(feedback_data):
    if feedback_data:
        df = pd.DataFrame(feedback_data)
        X = df.drop(columns='label')
        y = df['label']
        model = RandomForestRegressor()
        model.fit(X, y)
        with open('model.pkl', 'wb') as f:
            pickle.dump(model, f)
        return model
    return None

# Function to load the model
def load_model():
    if os.path.exists('model.pkl'):
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        return model
    return None

# Load the model
model = load_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.to_dict()
    schedule = generate_schedule(data)
    return render_template('schedule.html', schedule=schedule)

@app.route('/feedback', methods=['POST'])
def feedback():
    feedback_data.append(request.form.to_dict())
    # Process feedback and update the schedule
    global model
    model = train_model(feedback_data)
    return 'Feedback received!'

if __name__ == '__main__':
    app.run(debug=True)
