from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from datetime import datetime
import json

with open('templates/config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)

app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = params['mail-username']
app.config['MAIL_PASSWORD'] = params['mail-password']
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)


if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]


db = SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), nullable=False)
    phone_no = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(120), nullable=False)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post")
def post():
    return render_template("post.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Extract form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        
        # Check if all form fields are received
        print(f"Received: {name}, {email}, {phone}, {message}")
        
        # Create a new entry
        entry = Contacts(
            Name=name,
            phone_no=phone,
            msg=message,
            email=email,
            date=datetime.now()  # Format date
        )
        
        # Add and commit to the database
        try:
            db.session.add(entry)
            db.session.commit()
            print("Entry added successfully!")

            recepient = email  # List of recepients email.
            subject = "Thank you for contacting us."
            message_body = message

            msg = Message(subject=subject, sender="xred7698@gmail.com", recipients=[recepient])
            msg.body = message_body

            try:
                mail.send(msg)
                print("Email sent sucessfully")
            except Exception as e:
                print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
            db.session.rollback()  # Rollback if there's an error
        
    return render_template("contact.html", params = params)


app.run(debug = True)