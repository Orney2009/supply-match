from flask import Flask, jsonify, make_response
import os
from dotenv import load_dotenv
from flask_restful import Resource, Api
from database import *

import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud
from nltk import pos_tag
import pickle
import string
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

engine = get_engine(os.getenv('DBMS'), os.getenv('DB_USER'), os.getenv('DB_PASSWORD'), os.getenv('DB_HOST'), os.getenv('DB_PORT'), os.getenv('DB_NAME'))
Base.metadata.create_all(bind=engine)
current_session = get_session(engine)

db = current_session()


class Entreprises(Resource):
    def get(self):

        try:
            entreprises = db.query(objects.Entreprise).all()
            categories = db.query(objects.Category).all()
            ent_result = []
            cat_result = []
            for entreprise in entreprises:                
                ent_result.append({
                    'entreprise_id': entreprise.id,
                    'category_id': entreprise.category_id,
                    'name': entreprise.name,
                    'address': entreprise.address,
                    'phone': entreprise.phone,
                    'description': entreprise.description

                })

            for category in categories:                
                cat_result.append({
                    'id': category.id,
                    'name': category.name
                })

            result = {
                'entreprises' : ent_result,
                'categories' : cat_result
            }

            return make_response(jsonify(result), 200)

        except Exception as e:
            return jsonify({'error': str(e)}), 500

class Recommandations(Resource):
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
 


class Model:
    def __init__(self):
        try:
            # lsa model import
            with open('../artificial_intelligence/pickles/lsa_model.pkl', 'rb') as lsa_model:    
                self.lsa = pickle.load(lsa_model)                    


            # vector import
            with open('../artificial_intelligence/pickles/vector.pkl', 'rb') as vector_pkl:    
                self.vector = pickle.load(vector_pkl)

            # topic_df import
            with open('../artificial_intelligence/pickles/topic_df.pkl', 'rb') as topic_df_pkl:    
                self.topic_df = pickle.load(topic_df_pkl)

        except Exception as e:
            print(f"\nError during instanciation of sentiment analysis model: {e}\n")
  

    def tokenizer(self,df):
        try:
            tokenized_book = df
            tokenized_book["summary"] = df["summary"].map(lambda x: word_tokenize(x.lower() if isinstance(x, str) else str(x) ))
        except Exception as e:
            print(f"An error occurs when tokenizing: {e}")
        return tokenized_book

    def stopwords_remover(self, df):        
        try:   
            stop_words = set(stopwords.words('french'))    
            without_stopwords = df
            without_stopwords["summary"] = df["summary"].map(lambda x: [word for word in x if (word not in stop_words)]) 
        except Exception as e:
            print(f"An error occurs when removing stopwords: {e}")
        return without_stopwords

    def punctuation_remover(self, df):
        try:
            punctuation = string.punctuation + "``" + "''" + "--" + "_" + "(" + ")" + '""' + "|" + "“" + "”" + "’" + "‘" + "___"
            without_punc = df
            without_punc["summary"] = df["summary"].map(lambda x: [word for word in x if word not in punctuation])
        except Exception as e:
            print(f"An error occurs when removing punctuations: {e}")
        return without_punc

    def pos_tagger(self, df):
        try:
            pos_tagged = df
            pos_tagged["summary"] = df["summary"].map(lambda x: [tagged for tagged in pos_tag(x,tagset='universal') if tagged[1] not in ["NUM"] ])
        except Exception as e:
            print(f"An error occurs when tagging: {e}")
        return pos_tagged

    def lemmatizer(self, df):
        try:
            lem = WordNetLemmatizer()
            lemmans = df
            lemmans["summary"] = df["summary"].map(lambda row: [ lem.lemmatize(word[0], pos = get_pos_tag(word[1])) for word in row ])
        except Exception as e:
            print(f"An error occurs when lemmatizing: {e}")
        return lemmans    

    def get_pos_tag(self, pos):    
        match pos:
            case "NOUN":
                result = "n"
            case "VERB":
                result = "v"
            case "ADJ":
                result = "a"
            case "ADV":
                result = "r"
            case _:
                result = "s"
        return result

    def search_processing(self, search):
        try:
            search_df = pd.DataFrame(data=[search], columns=["summary"])
            tokenized_book = self.tokenizer(search_df)
            without_stopwords = self.stopwords_remover(tokenized_book)
            without_punctuation = self.punctuation_remover(without_stopwords)
            tagged_words = self.pos_tagger(without_punctuation)
            lemmatized_words = self.lemmatizer(tagged_words)
            lemmatized_words = lemmatized_words.summary.tolist()
            search = [" ".join(str(elm) for elm in row) for row in lemmatized_words]        
            vec = self.vector.transform(search)            
            return self.lsa.transform(vec)

        except Exception as e:
            print(f"An error occurs when processing the search:{e}")
        
    def best_recommended_pme(self, search, nb_recommandations):
        try:
            
            # Récupération du vecteur du livre cible
            search_vector = self.search_processing(search).reshape(1, -1)

            # Calcul des similarités cosinus
            similarities = self.topic_df.apply(
                lambda x: cosine_similarity(search_vector, x.to_numpy().reshape(1, -1))[0][0], axis=1
            )

            # Conversion en DataFrame
            recommandations = similarities.to_frame(name="Similarity")

            # Tri décroissant des similarités
            recommandations.sort_values(by="Similarity", ascending=False, inplace=True)

            # Sélection des meilleurs résultats
            result = recommandations.head(min(nb_recommandations, len(recommandations)))

            if result.empty:
                print("Aucune recommandation disponible.")
                return []

            print(f"Recommandations générées avec succès pour la recherche '{search}'.\n")
            formatted_result = []
            for recom in result.itertuples(index=True, name=None):
                formatted_result.append({
                    "name" : recom[0],
                    "score" : recom[1]
                })            
            return formatted_result
        
        except Exception as e:
            print(f"Une erreur est survenue lors de la génération des recommandations : {e}")
            return []

    
    