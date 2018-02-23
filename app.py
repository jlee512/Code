from flask import Flask, render_template, request, redirect, url_for
import os, json

app = Flask(__name__)

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

# Route for Home/Index Page
@app.route('/', methods=["GET"])
def index():
    json_url = os.path.join(SITE_ROOT, "static/json", "posts.json")
    data = json.load(open(json_url))
    return render_template("index.html", data=data)

# Route for the tutorial/about me page
@app.route('/about', methods=["GET"])
def about():
    return render_template("about.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    return render_template("register.html")


# Route for adding a post to the system
@app.route('/post', methods=["POST"])
def post():
    return render_template("add_post.html")


@app.route('/like/<int:post_id>', methods=["GET"])
def like(post_id):

    json_url = os.path.join(SITE_ROOT, "static/json", "posts.json")
    data = json.load(open(json_url))

    data[post_id]["like_count"] = data[post_id]["like_count"] + 1

    with open(json_url, "w") as file:
        json.dump(data, file)



    return redirect("/")


if __name__ == '__main__':
    app.run()
