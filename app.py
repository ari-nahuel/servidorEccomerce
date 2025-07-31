from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

# Cargar productos desde un archivo JSON
def cargar_productos():
    with open('productos.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/api/productos', methods=['GET'])
def obtener_productos():
    productos = cargar_productos()
    return jsonify(productos)

@app.route('/api/productos/<int:id>', methods=['GET'])
def obtener_producto(id):
    productos = cargar_productos()
    producto = next((p for p in productos if p['id'] == id), None)
    if producto:
        return jsonify(producto)
    else:
        return jsonify({'error': 'Producto no encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
