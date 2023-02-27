from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
import datetime 

x=datetime.datetime.now()

app=Flask(__name__)

migrate = Migrate()
cors = CORS()
@app.route('/data',methods = ['POST','GET'])
def get_time():

    return{
        'Name':"deepak",
        "City":"Dehradun",
        "Date":x,
        "programming":"python"
    }

if __name__=='__main__':
    app.run()
