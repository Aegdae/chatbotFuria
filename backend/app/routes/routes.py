from flask import Blueprint, request, jsonify
from app.controller.chat import chat_response
from app.services.update import update_past_matches, update_roster, update_upcoming_matches

chatView = Blueprint('chat', __name__)

# Rotas para a API

@chatView.route("/chat", methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    history = request.json.get('history', [])
    if not user_input:
        return jsonify({"error": "Mensagem não recebida"}), 400

    response = chat_response(user_input, history)

    return jsonify({'response': response})

# Rota para Atualizar o elenco e partidas

@chatView.route('/updateData', methods=['POST'])
def update_dados_secreto():
    update_roster()
    update_upcoming_matches()
    update_past_matches()