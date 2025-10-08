from flask import Flask, jsonify, request
import json

dispositivos_con_nombre = Flask(__name__)

with open('dispositivos_con_nombre.json', 'r') as file:
    dispositivos_con_nombre = json.load(file)


@dispositivos_con_nombre.route("/disp", methods = ['GET'])
def mostrarDispInfo():

    #CONSIDERA EN TODAS LAS LLAMDAS A API's UNA FORMA DE PREVENIR ERRORES
    Dispositivo_name = request.args.get('name')
    if not Dispositivo_name:
        return jsonify({"error": "Debes proporcionar el parámetro 'name'"}), 400

    #CONSIDERA EN TODAS LAS LLAMDAS A API's UNA FORMA DE PREVENIR ERRORES x2
    Dispositivo = dispositivos_con_nombre.get(Dispositivo_name)
    if not Dispositivo:
        return jsonify({"error": f"Dispositivo '{Dispositivo_name}' no encontrado"}), 404
    
    #PUEDES VERIFICAR LOS DIFERENTES TIPOS DE ERROR 400 & 404

    return jsonify({dispositivos_con_nombre})


@dispositivos_con_nombre.route('/dispositivos', methods=['GET'])
def get_all_Dispositivos():
    return jsonify(dispositivos_con_nombre)



if __name__ == '__main__':
    dispositivos_con_nombre.run(debug=True)



@dispositivos_con_nombre.route("/disp", methods = ['POST'])
def crear_Dispositivo():
    data = request.get_json()
    name = data.get("name")

    if not name or name in dispositivos_con_nombre:
        return jsonify({"Error": "Nombre invalido o ya existe"}), 400
    
    dispositivos_con_nombre[name] = {
        ""
    }