from flask import Flask, jsonify, request
import json

funciones = Flask(__name__)

with open('dispositivos_con_nombre.json', 'r') as file:
    dispositivos = json.load(file)


@funciones.route("/disp", methods = ['GET'])
def mostrarDispInfo():

    #CONSIDERA EN TODAS LAS LLAMDAS A API's UNA FORMA  DE PREVENIR ERRORES
    Dispositivo_name = request.args.get('name')
    if not Dispositivo_name:
        return jsonify({"error": "Debes proporcionar el parámetro 'name'"}), 400

    #CONSIDERA EN TODAS LAS LLAMDAS A API's UNA FORMA DE PREVENIR ERRORES x2
    Dispositivo = dispositivos.get(Dispositivo_name)
    if not Dispositivo:
        return jsonify({"error": f"Dispositivo '{Dispositivo_name}' no encontrado"}), 404
    
    #PUEDES VERIFICAR LOS DIFERENTES TIPOS DE ERROR 400 & 404

    return jsonify({dispositivos})


@funciones.route('/dispositivos', methods=['GET'])
def get_all_Dispositivos():
    return jsonify(dispositivos)




@funciones.route("/disp", methods = ['POST'])
def crear_Dispositivo():
    data = request.get_json()
    name = data.get("name")

    if not name or name in dispositivos:
        return jsonify({"Error": "Nombre invalido o ya existe"}), 400
    
    dispositivos[name] = {
        "ID": data.get("ID", dispositivos[name]["ID"]),
        "Ip": data.get("Ip", dispositivos[name]["Ip"]),
        "MAC": data.get("MAC", dispositivos[name]["MAC"]),
        "Lvl": data.get("Lvl", dispositivos[name]["Lvl"])
    }
    with open('dispositivos_con_nombre.json', 'w', encoding='utf-8') as file:
        json.dump(dispositivos, file)

    return jsonify({"message": f"Dispositivo '{name}' agregado correctamente"}), 201


@funciones.route('/disp/<name>', methods=['PUT'])
def update_device(name):
    if name not in dispositivos["Dispositivos"]:
        return jsonify({"error": f"Dispositivo '{name}' no encontrado"}), 404

    data = request.get_json()
    dispositivos["Dispositivos"][name].update({
        "ID": data.get("ID", dispositivos["Dispositivos"][name]["ID"]),
        "Ip": data.get("Ip", dispositivos["Dispositivos"][name]["Ip"]),
        "MAC": data.get("MAC", dispositivos["Dispositivos"][name]["MAC"]),
        "Lvl": data.get("Lvl", dispositivos["Dispositivos"][name]["Lvl"])
    })

    with open('dispositivos_con_nombre.json', 'w') as file:
        json.dump(dispositivos, file)

    return jsonify({"message": f"Dispositivo '{name}' actualizado correctamente"}), 200

@funciones.route('/disp/delete/<name>', methods=['DELETE'])
def delete_device(name):
    if name not in dispositivos["Dispositivos"]:
        return jsonify({"error": f"Dispositivo '{name}' no encontrado"}), 404
    
    
    del dispositivos["Dispositivos"][name]
    
    with open('dispositivos_con_nombre.json', 'w') as file:
        json.dump(dispositivos, file)

    return jsonify({"message": f"Dispositivo '{name}' eliminado correctamente"}), 200



if __name__ == '__main__':
    funciones.run(debug=True)