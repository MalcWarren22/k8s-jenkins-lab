from flask import Flask
import socket

app = Flask(__name__)

@app.get("/")
def hello():
    hostname = socket.gethostname()
    return f"Hello from Malcolm's Kubernetes! Pod: {hostname}\n"

@app.get("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
