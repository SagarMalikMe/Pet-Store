from crypt import methods
import email
import app
from flask import Flask, request, url_for, redirect, flash,abort,render_template
import psycopg2 
import psycopg2.extras
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask import jsonify
from flask_cors import CORS,cross_origin
from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
 
app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"
app.config['SQLALCHEMY_DATABASE_URI']= "postgresql://postgres:123@localhost/students"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db= SQLAlchemy(app)
 
DB_HOST = "localhost"
DB_NAME = "students"
DB_USER = "postgres"
DB_PASS = "123"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
class User(db.Model):
    __tablename__= 'user'
    email =db.Column(db.String(100), primary_key= True)
    name= db.Column(db.String(100),nullable=False)
    password= db.Column(db.String(100), nullable=False)



    def __init__(self,email,name,password):
        self.email=email
        self.name=name
        self.password=password
        
        
    def __repr__(self):
        return f"{self.email}-{self.name}-{self.email}"

@app.route('/users', methods=['GET'])
def Index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM user"
    cur.execute(s) # Execute the SQL
    list_users = cur.fetchall()
    
     
@app.route('/add_student', methods=['POST'])
def add_student():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']
        cur.execute("INSERT INTO user (email, name, password) VALUES (%s,%s,%s)", (email, name, password))
        conn.commit()
        flash('User Added successfully')
        
 
@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_employee(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('SELECT * FROM user WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    
 
@app.route('/update/<id>', methods=['POST'])
def update_student(id):
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
         
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE user
            SET fname = %s,
                lname = %s,
                email = %s
            WHERE id = %s
        """, (fname, lname, email, id))
        flash('user Updated Successfully')
        conn.commit()
        
 
@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_student(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM user WHERE id = {0}'.format(id))
    conn.commit()
    flash('user Removed Successfully')

   
"""
@app.route('/users')
def get_users():
    users=User.query.all()

    output=[]
    for user in users:
        user_data={'email':user.email ,'name':user.name }
        output.append(user_data)
    return {"users":output}"""

if __name__ == "__main__":
    app.run(debug=True)
    
