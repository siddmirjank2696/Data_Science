# Importing the required libraries
import numpy as np
import pandas as pd
import pickle
from flask import Flask, request, app, render_template


# Creating a Flask application
app = Flask(__name__)

# Loading the linear regression model
linear_model = pickle.load(open("linear_model.pkl", "rb"))

# Loading the scaler standardizer
scaler = pickle.load(open("scaler.pkl", "rb"))


# Creating a decorator to direct to the home page
@app.route("/")
def home():

    # Returning thr home page
    return render_template("home.html")


# Creating a decorator to direct to the prediction page
@app.route("/predict", methods=["POST"])
def predict():

    # Retrieving the data from an HTML form
    data = [float(x) for x in request.form.values()]
    
    # Standardizing the data
    final_input =  scaler.transform(np.array(data).reshape(1, -1))

    # Displaying the final input
    print(final_input)

    # Predicting the output using the linar model
    output = linear_model.predict(final_input)[0]

    # Returning the output
    return render_template("home.html", prediction_text="The Prediction Of The House Price Is : {}".format(output))


# Creating a main function
if __name__ == "__main__":

    # Allowing debugging of the app
    app.run(debug=True)