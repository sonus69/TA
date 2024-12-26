from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:30Fariz05@localhost/TA_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model Database
class TA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    HbA1c = db.Column(db.Float, nullable=False)
    BMI = db.Column(db.Float, nullable=False)
    Age = db.Column(db.Integer, nullable=False)
    Triglycerides = db.Column(db.Float, nullable=False)
    Cholesterol = db.Column(db.Float, nullable=False)
    Gender = db.Column(db.String(10), nullable=False)
    Prediction = db.Column(db.String(50), nullable=False)

# Load Model Machine Learning
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict1")
def predict():
    return render_template("model_farhan.html")

@app.route("/predictFarhan",methods=['GET','POST'])
def predictfarhan():
    if request.method == 'POST':
        # Ambil data dari form
        HbA1c = float(request.form['HbA1c'])
        BMI = float(request.form['BMI'])
        Age = int(request.form['Age'])
        Triglycerides = float(request.form['Triglycerides'])
        Cholesterol = float(request.form['Cholesterol'])
        Gender = request.form['Gender']

        # Proses prediksi dengan model
        input_data = pd.DataFrame([[HbA1c, BMI, Age, Triglycerides, Cholesterol, Gender]], 
                                  columns=['HbA1c', 'BMI', 'Age', 'Triglycerides', 'Cholesterol', 'Gender'])
        prediction = model.predict(input_data)[0]

        # Simpan data ke database
        new_data = TA(
            HbA1c=HbA1c,
            BMI=BMI,
            Age=Age,
            Triglycerides=Triglycerides,
            Cholesterol=Cholesterol,
            Gender=Gender,
            Prediction=prediction
        )
        db.session.add(new_data)
        db.session.commit()

    return render_template("model_farhan.html",prediction=prediction)

@app.route("/predictAbid")
def prediction():
    return render_template("model_abid.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True)
