# import the Flask class from the flask module
import flask
from flask import Flask, render_template, redirect, url_for, request ,session
from flask_wtf import Form
from wtforms import StringField,PasswordField
import os

# create the application object
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/welcome')
def welcome():
    print ("yo")
    return render_template('welcome.html')  # render a template

class LoginForm(Form):
    username=StringField('username')
    password=PasswordField('password')

@app.route('/login',methods=['GET','POST'])
def login():
    form1=LoginForm()
    # print(request.form["Login"])
    error = None
    if form1.username.data!= 'admin' or form1.password.data!= 'admin':
        error = 'Invalid Credentials. Please try again.'
    else:
        session['logged_in']=True
        flash('You were just logged_in')
        return redirect(url_for('home'))
    return render_template('login.html', form1=form1)

@app.route('/register',methods=['GET','POST'])
def register():
    return "Say yo"
@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    return render_template(url_for('welcome'))

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4444)))
  



