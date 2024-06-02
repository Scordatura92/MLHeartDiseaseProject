import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('models/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features = [np.array(input_features)]
    prediction = model.predict(features)

    print(input_features)
    print(prediction)

    if prediction >= 1:
        output = "High risk of heart disease detected, please seek medical attention immediately"
    else:
        output= "Low risk of heart disease detected"

    print(output)

    return render_template('index.html', prediction_text='Results: {}'.format(output))

if __name__ == "__main__":
    app.run()