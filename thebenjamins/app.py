import os

import pandas as pd
import numpy as np

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

import pickle


app = Flask(__name__)


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/Issue")
def Issue():
    return render_template("Issue.html")

    
@app.route("/methoddddd")
def methoddddd():
    return render_template("methoddddd.html")

@app.route("/methodology")
def methodology():
    return render_template("methodology.html")

@app.route("/plots")
def plots():
    return render_template("plots.html")

@app.route("/send", methods=["GET","POST"]) 
def send():
    if request.method == "POST":
        amount = int(request.form["loanAmount"]) 
        term = int(request.form["termAmount"])
        income = int(request.form["incomeAmount"])
        fico = int(request.form["FICOamount"])
        home = request.form["housing"] 
        mortgage = 0
        own = 0
        rent = 0

        if home == 'own':
            own = 1
        elif home == 'rent':
            rent = 1
        elif home == 'mortgage':
            mortgage = 1
        # data = map(float,[amount, term, income, fico, mortgage, own, rent])
        data = np.array([[amount, term, income, fico, mortgage, own, rent]])
        # data = np.array([[10000, 36, 100000, 750, 0, 0, 1]])
    

        model = pickle.load(open('model.h5','rb'))
        predicted = model.predict(data)
        final = np.round_(predicted[0][0],decimals =2)
        
        print(data)
        print(np.round_(predicted[0][0],decimals =2))
    # return str(predicted)

        return render_template("click.html", predicted=final)
    
    return render_template("click.html")

    #look up flask jinja template





if __name__ == "__main__":
    app.run(debug=True)


        # scaler = pickle.load(open('transform.h5', 'rb'))
