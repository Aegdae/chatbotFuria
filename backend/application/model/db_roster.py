from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv("C:/Users/Jonna/Documentos/Projetos/chatbotFuria/backend/env/dbconfig.env")

# Banco de dados para atualizar o elenco

class RosterDatabase:
    def __init__(self, db_name='furia_db', uri=None):
        if uri is None:
            uri = os.getenv("URI")
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def insert_roster(self, roster):
        self.db.roster.delete_many({})

        documents = [{"jogador": player} for player in roster]
        self.db.roster.insert_many(documents)

    def get_roster(self):
        roster = self.db.roster.find()
        players = [player['jogador'] for player in roster]
        return players
    
    def update_roster(self, roster):
        self.db.roster.delete_many({})
        documents = [{"jogador": player} for player in roster]
        self.db.roster.insert_many(documents)
    
    def check_roster_exists(self):
        return self.db.roster.count_documents({}) > 0