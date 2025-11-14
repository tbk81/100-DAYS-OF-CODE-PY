from flask import Flask, render_template
from datetime import datetime
import random
import requests

app = Flask(__name__)


@app.route("/")
def home():
    rando_num = random.randint(0, 100)
    current_year = datetime.now().year
    return render_template('index.html',
                           num=rando_num,
                           year=current_year)


@app.route("/guess/<name>")
def gender_age(name):
    gender_endpoint = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_endpoint).json()
    gender = gender_response['gender']
    age_endpoint = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_endpoint).json()
    age = age_response['age']
    return render_template('index.html', name=name.title(), gender=gender, age=age)







if __name__ == "__main__":
    app.run(debug=True)


