"""
Arquivo: app.py
Descrição: Um aplicativo Flask simples com rotas para obter e criar usuários.
Autor: Marcos
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    """
    Rota para obter dados de um usuário.

    Parâmetros:
        user_id (str): O ID do usuário a ser recuperado.

    Argumentos de Consulta:
        extra (str, opcional): Informação extra opcional.

    Retorna:
        json: Dados do usuário no formato JSON.
        Código de status HTTP: 200 se bem-sucedido.
    """
    user_data = {
        "user_id": user_id,
        "name": "Jonh Doe",
        "email": "marcoolivear096@gmail.com"
    }
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST", "GET"])
def create_user():
    """
    Rota para criar um novo usuário.

    Métodos HTTP Suportados:
        POST: Cria um novo usuário com base nos dados fornecidos no corpo da solicitação.

    Retorna:
        json: Dados do usuário recém-criado no formato JSON.
        Código de status HTTP: 201 se bem-sucedido.
    """
    if request.method == "POST":
        data = request.get_json()

        return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)
