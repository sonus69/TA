from flask import Flask, request, render_template
import pickle
import numpy as np


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predictFarhan")
def predict():
    return render_template("model_farhan.html")

@app.route("/predictAbid")
def prediction():
    return render_template("model_abid.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
