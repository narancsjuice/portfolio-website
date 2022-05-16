from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """

    :return:
    """
    return render_template("home.html")


@app.route("/about/")
def about():
    """

    :return:
    """
    return render_template("about.html")


@app.route("/experience/")
def experience():
    """

    :return:
    """
    return render_template("experience.html")


@app.route("/contact/")
def contact():
    """

    :return:
    """
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)