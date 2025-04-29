from flask import Flask
from flask_cors import CORS
from application.routes.routes import chatView

# Rodar o backEnd

app = Flask(__name__)
# CORS com rota para o frontend Angular
CORS(app, resources={r"/chat": {"origins": "http://localhost:4200"}})
app.register_blueprint(chatView)


if __name__ == "__main__":
    app.run(debug=True)