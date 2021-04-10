from flask import Flask,request, jsonify
from flask_restplus import Api, Resource, fields
from tinydb import TinyDB, Query
import datetime as dt

app = Flask(__name__)
api = Api(app,version="1.0", title="DevOpsR", description="A simple Birthday Count API", default="Revolut", license="Revolut")
#Saving to DB
db=TinyDB('./db.json')
User = Query()

#Current Date
today = dt.date.today()

#model
sampleModel = api.model('Date Of Birth', { 'dateOfBirth' : fields.String(description='The object type', enum=['1988-12-01']) })

@api.route('/hello/<userName>')
class Language(Resource):
    def get(self, userName):
        try:
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
                    return {"message" : f"Hello, {userName}! Happy Birthday"}
                else:
                    return {"message" : f"Hello, {userName}! Your birthday is in {diff.days} days."}
        except IndexError:
            return '''<strong><em>SORRY Page Not Found</em>:</strong>\n
                    <h1><strong>NOTE:</strong> Username must contain only letters and make sure before GET request use PUT request to add dateOfBirth for username<h1>'''     
    
    @api.expect(sampleModel)
    def put(self, userName):
        try:
            if request.headers['Content-Type'] == 'application/json':
                data = request.get_json()
                db.upsert({'name': userName, "dob": data['dateOfBirth']}, User.name == userName)
                return {}, 204
        except IndexError:
            return {"message": "Data MUST be in JSON Type"}

@app.errorhandler(404)
def page_not_found(e):
    return ('''<strong><em>SORRY Page Not Found</em>:</strong>\n
            <strong><em>Hint</em>:</strong> This is a RESTful web service! Append a username to the URL after hello (for example: <code>/hello/mayank -d { "dateOfBirth" : "1988-12-01" }</code>) with data.</p1>\n''')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=True)