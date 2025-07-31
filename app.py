from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

def cargar_productos():
    with open('productos.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/api/productos', methods=['GET'])
def obtener_productos():
    productos = cargar_productos()
    
    # Leer parámetros query limit y offset (con valores por defecto)
    try:
        limit = int(request.args.get('limit', 10))
        offset = int(request.args.get('offset', 0))
    except ValueError:
        return jsonify({'error': 'Parámetros inválidos'}), 400
    
    # Slice la lista de productos según limit y offset
    productos_pag = productos[offset:offset + limit]

    return jsonify(productos_pag)

@app.route('/api/productos/<int:id>', methods=['GET'])
def obtener_producto(id):
    productos = cargar_productos()
    producto = next((p for p in productos if p['id'] == id), None)
    if producto:
        return jsonify(producto)
    else:
        return jsonify({'error': 'Producto no encontrado'}), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
