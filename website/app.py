from flask import Flask
from flask_restful import Resource, Api
from backend import *
from flask_cors import CORS
from flask_jwt_extended import JWTManager


# Enable CORS for all routes and origins
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this to a random secret key
api = Api(app)
CORS(app)
jwt = JWTManager(app)


        
api.add_resource(Entreprises, '/')
api.add_resource(UserLogin, '/login')
api.add_resource(User, '/entreprise')
api.add_resource(UserRegistration, '/register')
api.add_resource(Recommandations, '/search')

if __name__ == '__main__':
    app.run(debug=True)