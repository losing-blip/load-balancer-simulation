# Load Balancer Simulation

A fun, interactive simulation of different load balancing strategies using Python Flask and HTML/JS.

## Features

- Round Robin
- Random Selection
- Least Connections
- Weighted Round Robin

## Setup
1. Clone the repository:
 ```bash
git clone https://github.com/losing-blip/load-balancer-simulation.git
cd load-balancer-simulation
```

2. Install dependencies:
 ```bash
pip install -r requirements.txt
 ```

3. Run the backend server:
 ```bash
python backend/load_balancer.py
 ```

5. Open the frontend:
Open frontend/index.html in your browser.

## API Endpoints
### `POST /request`
Simulates a load balancing request using a specified algorithm.

**Request Payload:**
```json
{
  "algorithm": "round_robin"
}
```

Available algorithms:
- `round_robin`
- `random`
- `least_connections`
- `weighted_round_robin`

**Response Example:**
```json
{
  "server": "Server-A",
  "algorithm_used": "round_robin"
}
```

---

### `POST /reset`
Resets all server loads to `0`.

**Response Example:**
```json
{
  "message": "Server loads reset."
}
```


