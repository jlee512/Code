from flask import Flask, render_template

app = Flask(__name__)


# Route for Home/Index Page
@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")


# Route for adding a post to the system
@app.route('/add_post', methods=["GET", "POST"])
def add_post():
    return render_template("add_post.html")

# Route for the tutorial/about me page
@app.route('/about', methods=["GET"])
def about():
    return render_template("about.html")





if __name__ == '__main__':
    app.run()
