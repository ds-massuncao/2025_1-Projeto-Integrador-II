from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Função para checar credenciais
def check_login(email, senha):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email=? AND senha=?", (email, senha))
    user = cursor.fetchone()
    conn.close()
    return user

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        if check_login(email, senha):
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('painel'))
        else:
            flash('Usuário ou senha incorretos.', 'danger')
    
    return render_template('login.html')

@app.route('/painel')
def painel():
    return "<h1>Bem-vindo ao sistema!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
