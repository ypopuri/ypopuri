from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import re

from sqlalchemy import true

app = Flask(__name__)
app.secret_key = 'Y@shu1234'
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yashu.db'

db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), unique=False, nullable=False)
    lastname = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(40), unique=False, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=False)
    confirmpassword = db.Column(db.String(20), unique=False, nullable=False)
  
@app.route('/')
@app.route('/LoginPage', methods =['GET', 'POST'])
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        user = Users.query.filter_by(email=email, password=password).first()
        if user:
            session['loggedin'] = True
            # session['name'] = user['name']
            # session['email'] = user['email']
            mesage = 'Logged in successfully !'
            return render_template('SecretPage.html', mesage = mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('LoginPage.html', mesage = mesage)
  
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('email', None)
    return redirect(url_for('login'))
  
  
def password_check(password):
    if(bool(re.match('((?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})',password))==True):
            return True
    elif(bool(re.match('(([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,30})',password))==True):
            return False
            
@app.route('/SignUpPage', methods =['GET', 'POST'])
def register():
    mesage = ''
    if request.method == 'POST' :
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        email = request.form["email"]
        password = request.form.get("password")
        confirmpassword = request.form.get("confirmpassword")
        print(firstname)
        print(lastname)
        print(email)
        print(password)
        print(confirmpassword)

        account = Users.query.filter_by(email=email).first()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mesage = 'Invalid email address !'
        elif not firstname or not password or not email:
            mesage = 'Please fill out the form !'
        if password_check(password):
            message = "invalid password"
        if not password == confirmpassword:
            mesage = 'password is not mached!'
        else:
            p = Users(firstname=firstname, lastname=lastname,email=email,password=password,confirmpassword=confirmpassword)
            db.session.add(p)
            db.session.commit()
            mesage = 'You have successfully registered !'
            return render_template('Thankyou.html', mesage = mesage)
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    return render_template('SignUpPage.html', mesage = mesage)
    
if __name__ == "__main__":
    app.run()