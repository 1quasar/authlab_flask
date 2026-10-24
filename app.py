import os
from dotenv import load_dotenv
from flask import Flask
from controllers.auth_controller import AuthController

load_dotenv()

# Instancia a aplicação Flask no escopo global
app = Flask(__name__)

# Chave criptográfica usada pelo Flask para assinar os cookies de sessão
app.secret_key = os.getenv('FLASK_SECRET_KEY')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return AuthController.login()

if __name__ == '__main__':
    # Roda o servidor em modo debug (recarrega automático ao salvar)
    app.run(debug=True)