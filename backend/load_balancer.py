import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Enable frontend-backend communication

# Simulated backend servers
servers = ["Server-A", "Server-B", "Server-C", "Server-D"]

# Round Robin setup
rr_index = 0

# Server loads for Least Connections
server_loads = {s: 0 for s in servers}

# Weighted Round Robin setup
weights = {
    "Server-A": 3,
    "Server-B": 2,
    "Server-C": 1,
    "Server-D": 4
}
weighted_list = [s for s in servers for _ in range(weights[s])]
wr_index = 0

# --- Algorithms ---
def round_robin():
    global rr_index
    server = servers[rr_index]
    rr_index = (rr_index + 1) % len(servers)
    return server

def random_selection():
    return random.choice(servers)

def least_connections():
    return min(server_loads, key=server_loads.get)

def weighted_round_robin():
    global wr_index
    server = weighted_list[wr_index]
    wr_index = (wr_index + 1) % len(weighted_list)
    return server

# --- Request handler ---
@app.route("/request", methods=["POST"])
def handle_request():
    data = request.get_json()
    algorithm = data.get("algorithm", "round_robin")

    if algorithm == "round_robin":
        server = round_robin()
    elif algorithm == "random":
        server = random_selection()
    elif algorithm == "least_connections":
        server = least_connections()
        server_loads[server] += 1
    elif algorithm == "weighted_round_robin":
        server = weighted_round_robin()
    else:
        return jsonify({"error": "Unknown algorithm"}), 400

    return jsonify({
        "server": server,
        "algorithm_used": algorithm
    })

# --- Reset loads (for testing) ---
@app.route("/reset", methods=["POST"])
def reset():
    for s in server_loads:
        server_loads[s] = 0
    return jsonify({"message": "Server loads reset."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
