import requests 
from flask import Flask,request, jsonify
from tinydb import TinyDB, Query

app = Flask(__name__)
app.config['DEBUG'] = True

#Saving to DB
db=TinyDB('db.json')
User = Query()

@app.route('/hello/<userName>', methods=['GET', 'PUT'])
def index(userName):
    if request.method == 'PUT':
        content = request.get_json()
        db.insert({'name': userName})
        return ('', 204)
    if request.method == 'GET':
        searchValue = db.search(User.name == userName)
        return jsonify(f"message: Hello, {searchValue}! Your birthday is on {content['dateOfBirth']}")


if __name__=="__main__":
    app.run(host='0.0.0.0', port=80, debug=True)