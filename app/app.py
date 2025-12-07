from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    hostname = socket.gethostname()
    return f"Hello from Malcolm's Kubernetes! Pod: {hostname}\n"

if __name__ == "__main__":
    # Gunicorn will be used in the container, this is just for local testing
    app.run(host="0.0.0.0", port=8000)
