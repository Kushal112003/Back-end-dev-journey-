flask ml pass predictor Web App

A simple machine learning-powered web application that predicts whether a student will pass or fail based on the number of study hours.

🔍 Project Overview

This project demonstrates the use of a linear regression model trained on student study data. The goal is to predict whether a student is likely to pass based on the number of hours they have studied.

 📌 Features

1. Input study hours through a simple web form.
2. Backend powered by Flask (Python).
3. Trained ML model (linear regression) saved and used for inference.
4. Outputs prediction: **"Pass"** or **"Fail"**.
5. HTML frontend built with Jinja2 templating.
6. Lightweight and easy to deploy.

🧠 Tech Stack

- Python
- Flask
- HTML/CSS (Jinja2 templating)
- Scikit-learn
- Pickle (for model serialization)

## 📁 Project Structure

project1/
├── app.py # Flask app to serve the model 
├── train_model.py # Script to train and save the ML model 
├── model.pkl # Trained ML model 
├── requirements.txt # Python dependencies 
├── Procfile # For deployment (e.g. on Heroku/Railway)
└── templates/
└── index.html # Frontend form for user input

📌 Use Case
Ideal for demonstrating how a basic machine learning model can be turned into a web application using Flask. This project shows the full pipeline from training to deployment.

✍️ Author
Kushal Jhirmiria
