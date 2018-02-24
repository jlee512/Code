from flask import Flask, render_template, request, redirect, url_for
import os, json
from urllib.parse import urlparse, parse_qs

app = Flask(__name__)

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))


# Route for Home/Index Page
@app.route('/', methods=["GET"])
def index():
    json_url = os.path.join(SITE_ROOT, "static/json", "posts.json")
    data = json.load(open(json_url))
    data = list(reversed(data))
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


@app.route('/add_post', methods=["GET", "POST"])
def add_post():
    if request.method == "POST":

        link = request.form.get("link")
        title = request.form.get("title")
        description = request.form.get("description")
        moderated = request.form.get("moderated")

        print(link)
        print(title)
        print(description)
        print(moderated)

        json_url = os.path.join(SITE_ROOT, "static/json", "posts.json")
        data = json.load(open(json_url))
        id = len(data)


        if link:

            post = {}
            post['id'] = id
            o = urlparse(link)
            post['content'] = "https://www.youtube.com/embed/" + o[4][2:]

            if title:
                post['title'] = title
            else:
                post['title'] = "Untitled"

            if title:
                post['description'] = description
            else:
                post['description'] = "Mysteriously there is no description"

            if moderated:
                post['moderated'] = True
            else:
                print("test")
                post['moderated'] = False

            post['like_count'] = 0
            data.append(post)


            print("test1")
            with open(json_url, "w") as file:
                print("test")
                json.dump(data, file)

            return redirect("/")


        else:
            return "No link attached"

        data.append(post)

        return redirect("/")

    if request.method == "GET":


        return render_template("add_post.html")


if __name__ == '__main__':
    app.run()
