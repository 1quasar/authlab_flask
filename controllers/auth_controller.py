from flask import(
    request,
    render_template,
    redirect,
    url_for,
    flash,
)

class AuthController:

    @staticmethod
    def login():
        if request.method == 'POST':
            username = request.form.get('username').strip()
            password = request.form.get('password')
            # Verifica de os campos foram preenchidos.
            if not username or not password:
                flash('Por favor, preencha os campos.', 'error')
                return redirect(url_for('login'))
            # Valida os campos

            # Busca o usuário no Model

            # Verifica a senha

            # Cria a Sessão

            pass

        return render_template('login.html')