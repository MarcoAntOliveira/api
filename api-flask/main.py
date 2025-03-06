from flask import Flask, jsonify
from articles  import Event1, Event2, Event3
import json
ev1 = Event1()
ev2 = Event2()
ev3 = Event3()

eventos = [ev1, ev2, ev3]

app = Flask(__name__)

@app.route("/")
def index():
      return "<h1> O Flask está  configurado com sucesso </h1>"


@app.route("/api/eventos/")
def listar_eventos():
    eventos_dict = []
    for ev in eventos:
      eventos_dict.append({
        "id": ev.id,
        "nome": ev.nome,
      })

    return jsonify(eventos_dict)

