from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__)


FOTOS_DIR = "Fotos"
if not os.path.exists(FOTOS_DIR):
    os.makedirs(FOTOS_DIR)

@app.route('/fotos', methods=['GET'])
def fotos():
    """Devuelve la lista de fotos en el directorio."""
    fotos = os.listdir(FOTOS_DIR)
    return jsonify(fotos)

@app.route('/fotos/<filename>')
def fotos_filename(filename):
    """Devuelve una foto específica."""
    return send_from_directory(FOTOS_DIR, filename)

@app.route('/')
def index():
    """Devuelve la página principal."""
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
