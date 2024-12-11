from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
from datetime import datetime
import json
import os
import math

with open('templates/config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)

app.secret_key = params['SECRET_KEY']
app.config['UPLOAD_FOLDER'] = params['upload_location']

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

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    tag_line = db.Column(db.String, nullable=False)
    slug = db.Column(db.String(25), nullable=False)
    content = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String(150), nullable=False)
    date = db.Column(db.String, nullable=False)

@app.route("/")
def home():
    posts = Posts.query.filter_by().all()
    total_posts = len(posts)
    last = math.ceil(total_posts / int(params['no_of_posts']))

    page = request.args.get('page')
    if(not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page - 1)*int(params['no_of_posts']):(page - 1)*int(params['no_of_posts'])+ int(params['no_of_posts'])]
    if(page == 1):
        prev = "#"
        next = "/?page=" + str(page + 1)
    elif(page == last):
        prev = "/?page=" + str(page - 1)
        next = "#"
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)


    return render_template("index.html", params=params, posts=posts, prev = prev, next = next)

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    if('user' in session and session['user'] == params['login_email']):
        posts = Posts.query.all()
        return render_template("dashboard.html", posts = posts)
    if request.method == 'POST':
        email = request.form.get('uname')
        password = request.form.get('pass')
        if email == params['login_email'] and password == params['login_pass']:
            session['user'] = email
            posts = Posts.query.all()
            return render_template("dashboard.html", posts = posts)
        
    return render_template("login.html", params = params)

@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit(sno):
    if('user' in session and session['user'] == params['login_email']):
        if request.method == 'POST':
            title = request.form.get('title')
            tline = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            if sno == '0':
                post = Posts(
                    title = title,
                    tag_line = tline,
                    slug = slug,
                    content = content,
                    img_url = img_file,
                    date=datetime.now()
                )
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(sno = sno).first()
                post.title = title
                post.tag_line = tline
                post.slug = slug
                post.content = content
                post.img_url = img_file
                post.date = datetime.now()
                db.session.commit()

        post = Posts.query.filter_by(sno = sno).first()
        return render_template("edit.html", params = params, post = post, sno = sno)

@app.route("/uploader", methods=['GET', 'POST'])
def uploader():
    if('user' in session and session['user'] == params['login_email']):
        if(request.method == 'POST'):
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return "File uploaded successfully!"  # Add this response
        return "Upload page for POST method."  # Add a fallback for GET method
    else:
        return "Unauthorized access", 403 

@app.route("/logout")    
def logout():
    session.pop('user')
    return redirect("/dashboard")


@app.route("/delete/<string:sno>", methods=['GET', 'POST'])
def delete(sno):
    if('user' in session and session['user'] == params['login_email']):
        post = Posts.query.filter_by(sno = sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect("/dashboard")


@app.route("/about")
def about():
    return render_template("about.html", params = params)

@app.route("/post", methods=['GET'])
def post_redirect():
    latest_post = Posts.query.order_by(Posts.date.desc()).first() # This will redirect to latest post.
    if latest_post:
        return redirect(url_for('post_route', post_slug=latest_post.slug))
    else:
        return "No posts available", 404


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template("post.html", params = params, post= post)

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
            db.session.rollback() 


    return render_template("contact.html", params = params)


app.run(debug = True)