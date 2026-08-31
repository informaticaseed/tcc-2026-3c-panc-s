"""
Arquivo principal do servidor Flask e das rotas do site.
"""

import os

from dotenv import load_dotenv
from flask import Flask, abort, flash, redirect, render_template, request, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)

from models import Usuario, db
from pancs_data import buscar_panc, listar_pancs

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "chave-teste")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "sqlite:///panc.db"
)

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "Faça login para acessar essa página."


@login_manager.user_loader
def carregar_usuario(usuario_id):
    return db.session.get(Usuario, int(usuario_id))


@app.route("/")
def index():
    """Página inicial: lista todas as PANCs cadastradas."""
    return render_template("index.html", pancs=listar_pancs())


@app.route("/panc/<panc_id>")
def detalhe(panc_id):
    """Página com os detalhes de uma PANC específica."""
    panc = buscar_panc(panc_id)
    if panc is None:
        abort(404)
    return render_template("detalhe.html", panc=panc)


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form["nome"].strip()
        email = request.form["email"].strip().lower()
        senha = request.form["senha"]

        if Usuario.query.filter_by(email=email).first():
            flash("Já existe uma conta com esse email.")
            return redirect(url_for("cadastro"))

        usuario = Usuario(nome=nome, email=email)
        usuario.set_senha(senha)
        db.session.add(usuario)
        db.session.commit()

        login_user(usuario)
        return redirect(url_for("index"))

    return render_template("cadastro.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"].strip().lower()
        senha = request.form["senha"]

        usuario = Usuario.query.filter_by(email=email).first()
        if usuario is None or not usuario.checar_senha(senha):
            flash("Email ou senha inválidos.")
            return redirect(url_for("login"))

        login_user(usuario)
        return redirect(url_for("index"))

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
