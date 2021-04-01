from flask import Flask,request, jsonify
from tinydb import TinyDB, Query
import datetime as dt
app = Flask(__name__)
app.config['DEBUG'] = True

#Saving to DB
db=TinyDB('./db.json')
User = Query()

#Current Date
today = dt.date.today()

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello World Application</h1><h2>DevOps Engineer Test</h2><p1>A Simple Hello World application that exposes GET and PUT api call.</p1>"

@app.route('/hello/<string:userName>', methods=['GET', 'PUT'])
def index(userName):
    try:
        if request.method == 'PUT':
            if request.headers['Content-Type'] == 'application/json':
                data = request.get_json()
                db.upsert({'name': userName, "dob": data['dateOfBirth']}, User.name == userName)
                return ('', 204)
            else:
                return ("Data MUST be in JSON Type")
        if request.method == 'GET':
            searchValue = db.search(User.name == userName)
            newValue = searchValue[0]
            birth = dt.datetime.strptime(newValue['dob'], '%Y-%m-%d')
            if ( today.month == birth.month and today.day >= birth.day or today.month > birth.month ):
                nextBirthYear = today.year + 1
            else: 
                nextBirthYear = today.year
            nextBirthday = dt.date(nextBirthYear, birth.month, birth.day)
            diff = nextBirthday - today
            if ( today == birth.date() ):
                return jsonify({"message" : f"Hello, {userName}! Happy Birthday"})
            else:
                # diff = nextBirthday - today
                return jsonify({"message" : f"Hello, {userName}! Your birthday is in {diff.days} days."})
    except IndexError:
        return "<h1>NOTE: Username must contain only letters and make sure before GET request use PUT request to add dateOfBirth for username<h1>"            

if __name__=="__main__":
    app.run(host='0.0.0.0', port=80, debug=True)