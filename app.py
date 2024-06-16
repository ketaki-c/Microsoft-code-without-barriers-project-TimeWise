from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.to_dict()
    # Process the data and store it in a database
    return 'Data submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)

import pandas as pd

app = Flask(__name__)

# Sample data
class_data = [
    {"course": "Math 101", "time": "MWF 9:00-10:00"},
    {"course": "History 202", "time": "TR 11:00-12:30"}
]

def generate_schedule(data):
    # Basic scheduling logic (example)
    schedule = []
    for item in class_data:
        if is_available(item['time']):
            schedule.append(item)
    return schedule

def is_available(time):
    # Check if the time slot is available (dummy logic)
    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.to_dict()
    schedule = generate_schedule(data)
    return render_template('schedule.html', schedule=schedule)

if __name__ == '__main__':
    app.run(debug=True)
