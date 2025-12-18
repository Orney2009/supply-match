from flask import Flask
from flask_restful import Resource, Api
from backend import *



app = Flask(__name__)
api = Api(app)


        
api.add_resource(Entreprises, '/')
api.add_resource(Recommandations, '/search')

if __name__ == '__main__':
    app.run(debug=True)