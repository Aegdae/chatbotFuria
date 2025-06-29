from pymongo import MongoClient
from dotenv import load_dotenv
import os

path = load_dotenv("C:/Users/Jonna/Documentos/Projetos/chatbotFuria/backend/env/dbconfig.env")

#Banco de dados com atualização das partidas

class MatchesDatabase:
    def __init__(self, db_name='furia_db', uri=None):
        if uri is None:
            uri = os.getenv("URI")
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.upcoming_matches_collection = self.db['upcoming_matches']
        self.recent_matches_collection = self.db['recent_matches']

    def insert_upcoming_matches(self, upcoming_matches):
        if upcoming_matches:
            if all(isinstance(match, dict) for match in upcoming_matches):
                self.upcoming_matches_collection.insert_many(upcoming_matches)
            else:
                print("Erro: As partidas futuras devem ser instâncias de dicionários.")
        else:
            print("Nenhuma partida futura para inserir.")

    def insert_recent_matches(self, recent_matches):
        if recent_matches:
            if all(isinstance(match, dict) for match in recent_matches):
                self.recent_matches_collection.insert_many(recent_matches)
            else:
                print("Erro: As partidas passadas devem ser instâncias de dicionários.")
        else:
            print("Nenhuma partida passada para inserir.")

    def get_upcoming_matches(self):
        return list(self.upcoming_matches_collection.find())

    def get_recent_matches(self):
        return list(self.recent_matches_collection.find())