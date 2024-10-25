from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# Rota que retorna o timestamp atual
@app.route('/timestamp', methods=['GET'])
def timestamp():
    now = datetime.utcnow()
    response = {
        "timestamp": int(now.timestamp()),
        "datetime": now.isoformat() + "Z"
    }
    return jsonify(response)

# Inicia a aplicação na porta 3000 (usada pelo Koyeb)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
