# import requests 
from flask import Flask,request, jsonify
from tinydb import TinyDB, Query
from datetime import timedelta as td
from datetime import datetime as dt
import time
app = Flask(__name__)
app.config['DEBUG'] = True

#Saving to DB
db=TinyDB('./db.json')
User = Query()
current_date = dt.now().date()

@app.route('/hello/<string:userName>', methods=['GET', 'PUT'])
def index(userName):
    if request.method == 'PUT':
        if request.headers['Content-Type'] == 'application/json':
            data = request.get_json()
            DOB = data['dateOfBirth'] 
            db.upsert({'name': userName, "dob": DOB}, User.name == userName)
            return ('', 204)
        else:
            return ("Data MUST be in JSON Type")
    if request.method == 'GET':
        searchValue = db.search(User.name == userName)
        newValue = searchValue[0]
        final = newValue['dob']
        myDate = dt.strptime(final, '%Y-%m-%d')
        myDob = myDate.date()
        # delta = final2 - current_date
        delta = current_date - myDob
        return jsonify({"message" : f"Hello, {userName}! Your birthday is in {delta.days} days"})


if __name__=="__main__":
    app.run(host='0.0.0.0', port=80, debug=True)