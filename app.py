from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# 🔥 Create metric
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')

@app.route("/")
def home():
    REQUEST_COUNT.inc()   # count requests
    return "Hello from DevOps + Kubernetes 🚀"

@app.route("/health")
def health():
    return "OK"

# 🔥 IMPORTANT: Prometheus endpoint
@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
