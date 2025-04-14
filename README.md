# Load Balancer Simulation

A fun, interactive simulation of different load balancing strategies using Python Flask and HTML/JS.

## Features

- Round Robin
- Random Selection
- Least Connections
- Weighted Round Robin

## Setup
1. Clone the repository:

bash
git clone https://github.com/losing-blip/load-balancer-simulation.git
cd load-balancer-simulation
2. Install dependencies:

bash
pip install -r requirements.txt
3. Run the backend server:

bash
python backend/load_balancer.py
4. Open the frontend:

Open frontend/index.html in your browser.

## API Endpoints
POST /request
Simulates a load balancing request.

POST /reset
Resets server loads to 0.


