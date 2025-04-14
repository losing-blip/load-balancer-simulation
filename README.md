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
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the backend server:

bash

python load_balancer.py
Open index.html in your browser to access the frontend.

API Endpoints
POST /request: Simulates a load balancing request.

Payload: { "algorithm": "round_robin" }

POST /reset: Resets server loads to 0.

## Tech Stack

- Python Flask
- Flask-CORS
- HTML + JavaScript
