from flask import Flask
import random

app = Flask(__name__)

random_num = random.randint(0, 9)


@app.route("/")
def splash():
    return ('<h1 style="text-align: center"><b>Guess a number between 0 and 9</b></h1>'
            '<center><img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnEzNzU3dnF5enE2YXZ3Z2gwMG'
            'JjYTBoM2hkMHVodXY2Nzd2dmNweCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JdFEeta1hLNnO/giphy.gif"></center>')


@app.route("/<int:number>")
def guess(number):
    if number == random_num:
        return ('<h1 style="text-align: center"><b>You Guessed Correctly!</b></h1>'
                '<center><img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWRpa245MnJyaGNqYXc2dHdrYnRre'
                'WU4cWlzcGJ1bzYzMXVwd3ltciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OfkGZ5H2H3f8Y/giphy.gif"></center>')
    elif number < random_num:
        return ('<h1 style="text-align: center"><b>You Guessed Too Low!</b></h1>'
                '<center><img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnYybHdtM2dqang0OXh5Njhsa2hwa'
                'XY0dGRmbWpsaXRqajVtb2Z2YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IevhwxTcTgNlaaim73/giphy.gif">'
                '</center>')
    else:
        return ('<h1 style="text-align: center"><b>You Guessed Too Low!</b></h1>'
                '<center><img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXBqNnJkcWM5b3B3d2E3NW82YXo5M'
                'mpkbHgwcGVsaG5xbGVzaGJ1ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VWwS82FgMKRm8/giphy.gif">'
                '</center>')


if __name__ == "__main__":
    app.run(debug=True)

