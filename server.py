import json

from flask import Flask, render_template
from datetime import datetime
import requests

#year for copyright
now = datetime.now()
year = now.year









name_to_check = "dave"



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", current_year=year)

@app.route("/guess/<name_to_check>")
def guess(name_to_check):
    # work on name api
    data1 = requests.get(f"https://api.agify.io?name={name_to_check}").text
    data2 = requests.get(f"https://api.genderize.io?name={name_to_check}").text
    age_api = json.loads(data1)
    gender_api = json.loads(data2)
    gender = gender_api["gender"]
    age = age_api["age"]
    name = name_to_check.capitalize()

    return render_template("guess.html", nme=name, ag=age, gen=gender)


if __name__ == "__main__":
    app.run(debug=True)


