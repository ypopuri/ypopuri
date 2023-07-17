import re
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def assignBase():
    return render_template('base.html')

@app.route('/signup_form')
def signup_form():
    return render_template('index.html')

@app.route('/thank_you',methods = ['POST'])
def thank_you():
    bar1 = request.form['PW_Checker']
    m=0
    rep = {"length":"","Upper":"","lower":"","Dig":""}

    if len(bar1) < 8:
        m=1
        rep["length"] = "Your length should be greater than 8"
    
    if not re.match("[A-Z]",bar1):
        m=1
        rep["Upper"] = "You didnt use an upper case letter"
    
    if not re.match("[a-z]",bar1):
        m=1
        rep["lower"] = "You didnt use a lower case letter"
    
    if not bar1[-1].isdigit():
        m=1
        rep["Dig"] = "You didnt use a number at end"
    
    if m!=1:
        rep={}
        
    return render_template('report.html',d=rep)


if __name__ == '__main__':
    app.run(debug=True)