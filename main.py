from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return {'key': 'value'}

api.add_resource(Home, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
