from flask import Flask, jsonify, request, abort
import uuid

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

"""
Base de datos temporal en memoria mediante una lista
de diccionarios
"""
series = [
  {
    "id": uuid.uuid4(),
    "nombre": "Gotham",
    "temporada": 1,
    "liga": "http://sample.com",
    "total_capitulos": 12,
    "capitulo_actual": 2
  },
  {
    "id": uuid.uuid4(),
    "nombre": "Better call Saul",
    "temporada": 2,
    "liga": "http://sample.com",
    "total_capitulos": 12,
    "capitulo_actual": 5
  }
]

@app.route("/")
def index():
  return "Nada que ver aqui por favor dirigete a los endpoints"

@app.route("/tracker/api/v0.01/serie/agregar", methods=["POST"])
def add_serie():
  if not request.json or not "nombre" in request.json or not "temporada" in request.json or not "total_capitulos" in request.json or not "capitulo_actual" in request.json:
    abort(404)
  serie = {
    "id": uuid.uuid4(),
    "nombre": request.json["nombre"],
    "temporada": request.json["temporada"],
    "liga": request.json.get("liga", ""),
    "total_capitulos": request.json["total_capitulos"],
    "capitulo_actual": request.json["capitulo_actual"]
  }
  series.append(serie)
  return jsonify({"serie": serie}), 201

@app.route("/tracker/api/v0.01/serie/get", methods=["GET"])
def get_serie():
  return jsonify({"series": series})

@app.route("/tracker/api/v0.01/serie/<uuid:id_serie>", methods=["PUT"])
def update_serie(id_serie):
  serie = [serie for serie in series if serie["id"] == id_serie]
  if len(serie) == 0:
    abort(404)
  if not request.json:
    abort(400)
  if "nombre" in request.json and str(request.json["nombre"]) != str:
    abort(400)
  if "temporada" in request.json and type(request.json["temporada"]) != str:
    abort(400)
  if "liga" in request.json and type(request.json["liga"]) != str:
    abort(400)
  if "total_capitulos" in request.json and type(request.json["total_capitulos"]) != int:
    abort(400)
  if "capitulo_actual" in request.json and type(request.json["capitulo_actual"]) != int:
    abort(400)
  
  serie[0]["nombre"] = request.json.get("nombre", serie[0]["nombre"])
  serie[0]["temporada"] = request.json.get("temporada", serie[0]["temporada"])
  serie[0]["liga"] = request.json.get("liga", serie[0]["liga"])
  serie[0]["total_capitulos"] = request.json.get("litotal_capitulosga", serie[0]["total_capitulos"])
  serie[0]["capitulo_actual"] = request.json.get("capitulo_actual", serie[0]["capitulo_actual"])
  return jsonify({"serie": serie[0]})

@app.route("/tracker/api/v0.01/serie/<uuid:id_serie>", methods=["DELETE"])
def delete_serie(id_serie):
  serie = [serie for serie in series if serie["id"] == id_serie]
  if len(serie) == 0:
    abort(404)
  series.remove(serie[0])
  return jsonify({"result": True})

if __name__ == "__main__":
  app.run(debug=True, host= "0.0.0.0")