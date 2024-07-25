from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__)

@app.route('/fotos/<filename>')
def get_foto(filename):
    return send_from_directory('fotos', filename)

@app.route('/fotos')
def list_fotos():
    fotos = [f for f in os.listdir('fotos') if os.path.isfile(os.path.join('fotos', f))]
    return jsonify(fotos)

if __name__ == '__main__':
    app.run(debug=True)
