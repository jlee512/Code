from flask import Flask, render_template, request, redirect

app = Flask(__name__)


# Route for Home/Index Page
@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")


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

    print(post_id)

    return redirect("/")




if __name__ == '__main__':
    app.run()
