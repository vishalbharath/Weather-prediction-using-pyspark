import pandas as pd
from flask import Flask, request, render_template
import pickle

# Load the trained model from 'model.pkl'
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    # Define the exact features used in training, in the same order (excluding RainTomorrow)
    required_columns = [
        'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine', 
        'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm', 
        'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm', 
        'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am', 
        'Temp3pm', 'RainToday', 'RISK_MM'
    ]
    
    # Map form inputs to match model's expected feature names
    input_data = {
        'MinTemp': float(request.form['MinTemp']),
        'MaxTemp': float(request.form['MaxTemp']),
        'Rainfall': float(request.form['Rainfall']),
        'Evaporation': float(request.form['Evaporation']),
        'Sunshine': float(request.form['Sunshine']),
        'WindGustDir': request.form['WindGustDir'],  # Assuming categorical
        'WindGustSpeed': float(request.form['WindGustSpeed']),
        'WindDir9am': request.form['WindDir9am'],  # Assuming categorical
        'WindDir3pm': request.form['WindDir3pm'],  # Assuming categorical
        'WindSpeed9am': float(request.form['WindSpeed9am']),
        'WindSpeed3pm': float(request.form['WindSpeed3pm']),
        'Humidity9am': float(request.form['Humidity9am']),
        'Humidity3pm': float(request.form['Humidity3pm']),
        'Pressure9am': float(request.form['Pressure9am']),
        'Pressure3pm': float(request.form['Pressure3pm']),
        'Cloud9am': float(request.form['Cloud9am']),
        'Cloud3pm': float(request.form['Cloud3pm']),
        'Temp9am': float(request.form['Temp9am']),
        'Temp3pm': float(request.form['Temp3pm']),
        'RainToday': int(request.form['RainToday']),
        'RISK_MM': float(request.form['RISK_MM']),  # Assuming RISK_MM is numerical
    }

    # Create a DataFrame with the exact same columns as the training data
    input_df = pd.DataFrame([input_data])

    # Predict (ensure to pass only the columns that the model expects)
    prediction = model.predict(input_df[required_columns])
    prediction_text = "Yes" if prediction[0] == 1 else "No"

    # Render the result
    return render_template('index.html', prediction_text=f'Prediction: {prediction_text}')

  

    

if __name__ == "__main__":
    app.run(debug=True)
