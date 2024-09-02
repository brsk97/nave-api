from flask import Flask, jsonify, Response
import random

app = Flask(__name__)

# Datos de los sistemas y sus códigos
damaged_systems = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05"
}

# Estado del sistema dañado (se actualizará aleatoriamente en la primera llamada)
current_damaged_system = None

@app.route('/status', methods=['GET'])
def status():
    global current_damaged_system
    if current_damaged_system is None:
        current_damaged_system = random.choice(list(damaged_systems.keys()))
    return jsonify({"damaged_system": current_damaged_system})

@app.route('/repair-bay', methods=['GET'])
def repair_bay():
    global current_damaged_system
    if current_damaged_system is None:
        return Response("No damaged system specified", status=400)
    
    code = damaged_systems.get(current_damaged_system, "UNKNOWN")
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Repair</title>
</head>
<body>
<div class="anchor-point">{code}</div>
</body>
</html>"""
    return Response(html_content, mimetype='text/html')

@app.route('/teapot', methods=['POST'])
def teapot():
    return Response("I'm a teapot", status=418)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
