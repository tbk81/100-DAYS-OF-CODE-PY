from flask import Flask, render_template
from datetime import datetime
import random

app = Flask(__name__)


@app.route("/")
def home():
    rando_num = random.randint(0, 100)
    current_year = datetime.now().year
    return render_template('index.html',
                           num=rando_num,
                           year=current_year)


@app.route("/guess/<name>")
def gender_age():


if __name__ == "__main__":
    app.run(debug=True)


