"""
Arquivo principal do servidor Flask e das rotas do site.
"""

from flask import Flask, abort, render_template

from pancs_data import buscar_panc, listar_pancs

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)
