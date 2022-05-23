from flask import Flask, render_template, request
from flask_wtf import FlaskForm, CSRFProtect
from flask_mail import Message, Mail
from wtforms.validators import DataRequired, Email
from wtforms import StringField, TextAreaField, SubmitField
import configparser

# Create Flask instance
app = Flask(__name__)

# Create Mail instance
mail = Mail()

# Enable CSRF protection
csrf = CSRFProtect(app)

# Read config.env for sensitive information
config = configparser.ConfigParser(interpolation=None)
config.read("config.env")


# App configuration for Contact Form email feature for encrypted google
# mail server
app.config["SECRET_KEY"] = config["SENS_INFO"]["SECRET_KEY"]
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = config["SENS_INFO"]["MAIL_USERNAME"]
app.config["MAIL_PASSWORD"] = config["SENS_INFO"]["MAIL_PASSWORD"]
mail.init_app(app)


@app.route("/")
def home():
    """
    Renders home page
    :return: home.html
    """
    return render_template("home.html")


@app.route("/about/")
def about():
    """
    Renders about page
    :return: about.html
    """
    return render_template("about.html")


@app.route("/experience/")
def experience():
    """
    Renders work experience page
    :return: experience.html
    """
    return render_template("experience.html")


@app.route("/skills/")
def skills():
    """
    Renders skills page
    :return: skills.html
    """
    return render_template("skills.html")


# Create contact form
class ContactForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    email = StringField(label="Email", validators=[DataRequired(),
                                                   Email(granular_message=True)])
    subject = StringField(label="Subject", validators=[DataRequired()])
    message = TextAreaField(label="Message", validators=[DataRequired()])
    submit = SubmitField(label="Send Message")


@app.route("/contact/", methods=["GET", "POST"])
def contact():
    """
    Renders contact page
    :return: contact.html
    """
    # Instance of contact form class
    cform = ContactForm()

    # If user send a POST request with Send button on form, send email with
    # template that gets form values
    if request.method == "POST":
        msg = Message(cform.subject.data, sender=config["SENS_INFO"]["SENDER"],
                      recipients=[config["SENS_INFO"]["RECIPIENT"]])
        msg.body = """
              New contact request from the website.
              
              From: %s <%s>
              
              Message: %s
              """ % (cform.name.data, cform.email.data, cform.message.data)
        mail.send(msg)

        # Render contact page without form, with success message
        return render_template("contact.html", form=cform, success=True)

    # Render contact page
    elif request.method == "GET":
        return render_template("contact.html", form=cform)


@app.errorhandler(404)
def page_not_found(e):
    """
    Renders when user types in non-existent hypertext reference
    :return: 404.html
    """
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
    csrf.init_app(app)
