from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

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
