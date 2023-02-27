from flask import Flask, request, url_for, redirect, flash,abort,render_template
import psycopg2 
import psycopg2.extras
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask import jsonify
from flask_cors import CORS,cross_origin





app=Flask(__name__)
app.secret_key="this is my secret key"
app.config['SQLALCHEMY_DATABASE_URI']= "postgresql://postgres:123@localhost/students"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db= SQLAlchemy(app)
CORS(app)





class Pet(db.Model):
    __tablename__= 'pets'
    id =db.Column(db.Integer, primary_key= True)
    pet_name= db.Column(db.String(100),nullable=False)
    pet_type= db.Column(db.String(100), nullable=False)
    pet_age= db.Column(db.Integer(), nullable= False)
    pet_price=db.Column(db.Integer(), nullable=False)


    def __init__(self,pet_name,pet_type,pet_age,pet_price):
        self.pet_name=pet_name
        self.pet_age=pet_age
        self.pet_type=pet_type
        self.pet_price=pet_price
        
    def __repr__(self):
        return f"{self.pet_name}:{self.pet_age}:{self.pet_type}:{self.pet_price}"
    


@app.route('/')
def index():
    return jsonify({"message":"Welcome to my site"})
    

@cross_origin()
@app.route('/pets', methods = ['POST'])
def create_pet():
    pet_data = request.json

    pet_name = pet_data['pet_name']
    pet_type = pet_data['pet_type']
    pet_age = pet_data['pet_age']
    pet_price = pet_data['pet_price']
    pet = Pet(pet_name =pet_name , pet_type = pet_type, pet_age = pet_age, pet_price=pet_price )
    db.session.add(pet)
    db.session.commit()
    

    return jsonify({"success": True,"response":"Pet added"})
        
        
             


@cross_origin()    
@app.route('/getpets', methods = ['GET'])
def getpets():
    all_pets = []
    pets = Pet.query.all()
    for pet in pets:
        results = {
                    "pet_id":pet.id,
                    "pet_name":pet.pet_name,
                    "pet_age":pet.pet_age,
                    "pet_type":pet.pet_type,
                    "pet_price":pet.pet_price, }
        all_pets.append(results)
        

    return jsonify(
            {
                "success": True,
                "pets": all_pets,
                "total_pets": len(pets),
            }
        )

@app.route("/pets/<int:pet_id>", methods = ["PATCH"])
def update_pet(pet_id):
    pet = Pet.query.get(pet_id)
    pet_age = request.json['pet_age']
    pet_price = request.json['pet_price']

    if pet is None:
        abort(404)
    else:
        pet.pet_age = pet_age
        pet.pet_price = pet_price
        db.session.add(pet)
        db.session.commit()
        return jsonify({"success": True, "response": "Pet Details updated"})    

@app.route("/pets/delete/<int:pet_id>", methods = ["PATCH"])
def delete_pet(pet_id):
    pet = Pet.query.get(pet_id)
    pet_name = request.json['pet_name']
    

    if pet is None:
        abort(404)
    else:
        db.session.delete(pet)
        
        db.session.commit()
        return jsonify({"success": True, "response": "Pet Details updated"})

db.create_all()
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
    """
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin

import datetime 

x=datetime.datetime.now()

app=Flask(__name__)

migrate = Migrate()



CORS(app)
@app.route('/data',methods = ['POST','GET'])
def get_time():
    return{
        'Name':"deepak",
        "City":"Dehradun",
        "Date": x,

        "programming":"python"
    }

if __name__=='__main__':
    app.run()"""