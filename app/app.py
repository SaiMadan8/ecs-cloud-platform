from flask import Flask, jsonify
import os
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

@app.route("/version")
def version():
    return jsonify(
        version=os.getenv("APP_VERSION", "unknown"),
        environment=os.getenv("APP_ENV", "unknown")
    ), 200

@app.route("/metadata")
def metadata():
    return jsonify(
        hostname=socket.gethostname(),
        timestamp=datetime.utcnow().isoformat()
    ), 200

if __name__ == "__main__":
    port = int(os.getenv("APP_PORT", 5000))
    app.run(host="0.0.0.0", port=port)
