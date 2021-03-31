import requests 
from flask import Flask,request, jsonify
from tinydb import TinyDB, Query
import datetime as dt

app = Flask(__name__)
app.config['DEBUG'] = True

#Saving to DB
db=TinyDB('./db.json')
User = Query()
today_date = dt.date.today()

@app.route('/hello/<string:userName>', methods=['GET', 'PUT'])

def index(userName):
    if request.method == 'PUT':
        if request.headers['Content-Type'] == 'application/json':
            data = request.get_json()
            DOB = data['dateOfBirth'] 
            db.insert({'name': userName, "dob": DOB})
            return ('', 204)
        else:
            return ("Data MUST be in JSON Type")

            
    if request.method == 'GET':
        searchValue = db.search(User.name == userName)
        newValue = searchValue[0]
        final = newValue['dob']
        return jsonify({"message" : f"Hello, {userName}! Your birthday is on {today_date} days and you enered {final}"})


if __name__=="__main__":
    app.run(host='0.0.0.0', port=80, debug=True)