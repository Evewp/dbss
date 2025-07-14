from flask import Flask, render_template, request
import joblib
<<<<<<< HEAD
=======
from groq import Groq

# Comment off due to API key for security
# import os
# os.environ['GROQ_API_KEY'] = "" 
# for cloud ..........
>>>>>>> 9f9d54f (update app.py)

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    q = request.form.get("q")
    # DB
    return(render_template("main.html"))

@app.route("/dbs",methods=["GET","POST"])
def dbs():
    return(render_template("dbs.html"))

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    q = float(request.form.get("q"))

    # Load Model
    model = joblib.load("dbs.jl")

    # Make Prediction
    pred = model.predict([[q]])

    return(render_template("prediction.html",r=(-50.6*q)+90.2))

# This is for local testing
if __name__ == "__main__":
    app.run()
