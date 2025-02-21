from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Datos de ejemplo de productos
productos = [
    {"id": 1, "nombre": "Producto A", "precio": 10.99},
    {"id": 2, "nombre": "Producto B", "precio": 15.50},
    {"id": 3, "nombre": "Producto C", "precio": 7.25}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/productos')
def api_productos():
    return jsonify(productos)

if __name__ == '__main__':
    app.run(debug=True)

    
