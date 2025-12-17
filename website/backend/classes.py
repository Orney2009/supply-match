from flask import Flask, jsonify, make_response
import os
from dotenv import load_dotenv
from flask_restful import Resource, Api
from database import *

load_dotenv()

engine = get_engine(os.getenv('DBMS'), os.getenv('DB_USER'), os.getenv('DB_PASSWORD'), os.getenv('DB_HOST'), os.getenv('DB_PORT'), os.getenv('DB_NAME'))
Base.metadata.create_all(bind=engine)
current_session = get_session(engine)

db = current_session()


class Entreprises(Resource):
    def get(self):

        try:
            entreprises = db.query(objects.Entreprise).all()
        
            result = []
            for entreprise in entreprises:                
                result.append({
                    'entreprise_id': entreprise.id,
                    'category_id': entreprise.category_id,
                    'name': entreprise.name,
                    'address': entreprise.address,
                    'phone': entreprise.phone,
                    'description': entreprise.description

                })

            return make_response(jsonify(result), 200)

        except Exception as e:
            return jsonify({'error': str(e)}), 500

class Recommandations(Resource):
    def get(self):
        return 