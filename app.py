from flask import Flask,render_template,request
# import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from form import Form,Login
# from sqlite3
# from models import db

import os 
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.sqlite3'
app.config['SECRET_KEY']='mysecret' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
# db.init_app(app)
db=SQLAlchemy(app)

@app.route('/')
def index():
    form=Form()
    return render_template('index.html',form=form)


@app.route("/payment", methods = ['POST'])
def makepayment():
    form=Form()

    if request.method == "POST":
       if form.is_submitted():
            print("Form successfully submitted")
       if form.validate_on_submit():
        reg = form.Registration_No.data
        name = form.Name.data
        level = form.level.data
        email = form.Email.data
        momo =form.MobileMoney.data
        Amount = form.Amount.data
        Contact = form.Contact.data
        name = request.form.data("Name", default_value)
       
        # return 'success' 
        return render_template('index.html',form=form)
    # print(Contact)
    #     return(momo_send(Contact,Amount))
    return render_template('success.html')

#list all your transactions
@app.route("/transactions")
def transactions ():
   
    return 'transactions'

@app.route("/login")
def log():
    login=Login()
    return render_template('sign.html',login=login)



if __name__=='__main__':
   app.run(debug=True)

