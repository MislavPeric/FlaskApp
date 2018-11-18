from flask import Flask, render_template
from data import articles

app = Flask(__name__)

articles = articles()

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/articles")
def articles():
    return render_template("articles.html", articles = articles)
if __name__ == "__main__":
    app.run(debug=True)
