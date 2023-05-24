from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/a0984180b53d79ed4e90")
    if response.status_code == 200:
        json_data = response.json()
    return render_template("index.html", blogs_data=json_data)


@app.route('/post/<id>')
def get_post(id):
    response = requests.get("https://api.npoint.io/a0984180b53d79ed4e90")
    if response.status_code == 200:
        json_data = response.json()
    return render_template("post.html", blogs_data=json_data, blog_id=int(id))


if __name__ == "__main__":
    app.run(debug=True)
