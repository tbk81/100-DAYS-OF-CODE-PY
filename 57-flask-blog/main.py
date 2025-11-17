from flask import Flask, render_template
import requests

app = Flask(__name__)


headers = {
    "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
    }

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url, headers=headers, timeout=10)
    all_posts = response.json()
    return render_template("index2.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
