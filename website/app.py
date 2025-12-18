from flask import Flask
from flask_restful import Resource, Api
from backend import *
from flask_cors import CORS


# Enable CORS for all routes and origins
app = Flask(__name__)
api = Api(app)
CORS(app)


        
api.add_resource(Entreprises, '/')
api.add_resource(Recommandations, '/search')

if __name__ == '__main__':
    app.run(debug=True)