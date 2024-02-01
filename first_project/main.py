"""
Arquivo: app.py
Descrição: Um aplicativo Flask simples com uma rota inicial.
Autor: Marcos
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    """
    Rota inicial do aplicativo.

    Retorna:
        str: Uma mensagem de saudação.
    """
    return "Home"

if __name__ == "__main__":
    app.run(debug=True)
