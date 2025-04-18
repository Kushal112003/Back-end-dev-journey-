from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template('index.html', prediction="")

@app.route('/predict', methods=['POST'])
def predict():
    input_value = request.form['input_value']
    prediction = model.predict([[float(input_value)]])
    return render_template('index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
