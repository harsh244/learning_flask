# import the Flask class from the flask module
import flask
from flask import Flask, render_template, redirect, url_for, request ,session,flash
from flask_wtf import Form
from wtforms import StringField,PasswordField
import os

# create the application object
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# use decorators to link the function to a url
@app.route('/jo')
def home():
    return render_template('index.html')  # return a string

@app.route('/')
def welcome():
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
        flash('You were just logged in')
        return redirect(url_for('home'))
    return render_template('login.html', form1=form1)

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('You just logged out')
    return redirect(url_for('welcome'))

# # start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
  



