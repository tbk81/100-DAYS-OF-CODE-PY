from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index3.html')


if __name__ == "__main__":
    app.run(debug=True)

# If you go to the dev tools of the website and go to 'console' you can make the page editable
# add this line 'document.body.contentEditable=true'
# Then save the webpage and out that in the 'templates' file
