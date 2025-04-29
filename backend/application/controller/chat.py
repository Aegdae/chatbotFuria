import os
import requests
from dotenv import load_dotenv
from app.model.db_roster import RosterDatabase
from app.model.db_matches import MatchesDatabase

load_dotenv("C:/Users/Jonna/OneDrive/Documentos/Projeto-Furia/backend/env/config.env")

db_roster = RosterDatabase()
db_matches = MatchesDatabase()

# IA

def chat_response(user_input, history=None):
    url = "https://api.cohere.ai/v1/chat"
    headers = {
        "Authorization": f"Bearer {os.getenv('COHERE_API_KEY')}",
        "Content-Type": "application/json"
    }

    # Historico da conversa
    
    if history is None:
        history = []

    players = db_roster.get_roster()
    elenco_texto = f"O elenco atual da FURIA é: {', '.join(players)}."


    history.insert(0, {"role": "system", "message": elenco_texto})


    if 'elenco' in user_input.lower() or 'jogadores' in user_input.lower():
        return elenco_texto
    
    if 'proxima partida' in user_input.lower() or 'proximo jogo' in user_input.lower() or 'proximas partidas' in user_input.lower() or 'proximos jogos' in user_input.lower():
        upcoming_matches = db_matches.get_upcoming_matches()
        if upcoming_matches:
            upcoming_response = "A próxima partida da FURIA é:\n"
            upcoming_response += '\n'.join([f"{match['date']} - {match['team1']} vs {match['team2']} (Evento: {match['event']})" for match in upcoming_matches])
        else:
            upcoming_response = "Não há partidas futuras agendadas para a FURIA."
        return upcoming_response

    if 'ultimas partidas' in user_input.lower() or 'ultimos jogos' in user_input.lower() or 'ultimos resultados' in user_input.lower():
        recent_matches = db_matches.get_recent_matches()
        if recent_matches:
            recent_response = "As últimas partidas da FURIA foram:\n\n"
            recent_response += '\n\n'.join(
                [f"{match['date']} - {match['team1']} vs {match['team2']}\nResultado: {match['score']}" for match in recent_matches]
            )
        else:
            recent_response = "Não há partidas passadas registradas para a FURIA."
        return recent_response

    # Prompt para responder sobre a Furia CS2
    
    data = {
        "message":  f"Você é um assistente da FURIA especializado em Counter-Strike 2 (CS2). Sempre responda somente sobre CS2 da FURIA. Pergunta: {user_input}",
        "model": "command-r-plus",
        "chat_history": [
            { "role": msg["role"].lower(), "message": msg["message"]}
            for msg in history
        ]
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return response.json()['text']
    else:
        return f"Erro na IA: {response.status_code} - {response.text}"
