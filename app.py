import os
from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    )

load_dotenv()

# Instancia a aplicação Flask no escopo global
app = Flask(__name__)

# Chave criptográfica usada pelo Flask para assinar os cookies de sessão
app.secret_key = 'FLASK_SECRET_KEY'

@app.route('/exemplo', methods=[GET, POST])
def exemplo():

    if request.method == 'POST':
        # Captura o valor digitado no input HTML
        campo = request.form['']

        flash('Operação realizada com sucesso!', 'success')

        return redirect('/exemplo')

    return render_template('arq.hmtl')

if __name__ == '__main__':
    # Roda o servidor em modo debug (recarrega automático ao salvar)
    app.run(debug=True)