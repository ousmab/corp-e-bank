from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/database_for_test.db"
db = SQLAlchemy(app)

#---------------MODELS-------------------------------
class Client(db.Model):
	id 				= db.Column(db.Integer,primary_key=True)
	nom				= db.Column(db.String(80),nullable=False )   #required , 
	prenom			= db.Column(db.String(80),nullable=False) #required , 
	sexe			= db.Column(db.Integer,nullable=False) # masculin = 1 feminin =0 et autres  > 1 #required , 
	date_naissance 	= db.Column(db.DateTime,nullable=False) #required , 
	telephone		= db.Column(db.String(13),nullable=False ) #required , 
	email			= db.Column(db.String(250),nullable=False ) #required , 
	adresse			= db.Column(db.String(25),nullable=False)
	numero_compte   = db.Column(db.String(22))
	solde_compte	= db.Column(db.Float,default=0.0)
	login			= db.Column(db.String(255) )
	mot_de_passe	= db.Column(db.Text )
	date_creation	= db.Column(db.DateTime)


	


#--------------ROUTES--------------------------------


@app.route('/')
def home():
    return render_template("pages/home.html")

@app.route('/connection')
def connection_client():
	return	render_template("pages/connection.html")

@app.route('/myaccount')
def account():
	return render_template("pages/account/dashboard.html")


if __name__ == "__main__":
	db.create_all()
	app.run(debug=True,port=8000,host="0.0.0.0")