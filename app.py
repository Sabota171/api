from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Função para registrar logs
def log_request():
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent', 'Desconhecido')
    now = datetime.utcnow().isoformat() + "Z"
    print(f"[LOG] Requisição recebida: IP={ip_address}, Agente={user_agent}, Hora={now}")

# Rota que retorna o timestamp atual
@app.route('/timestamp', methods=['GET'])
def timestamp():
    log_request()  # Registra as informações do usuário

    now = datetime.utcnow()
    response = {
        "timestamp": int(now.timestamp()),
        "datetime": now.isoformat() + "Z"
    }
    return jsonify(response)

# Inicia a aplicação na porta 3000 (usada pelo Koyeb)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
