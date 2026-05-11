# PHP + Nginx + ngrok (Docker)

## Run

docker compose up

Local: http://localhost:8080

---

## ngrok token

https://dashboard.ngrok.com/get-started/your-authtoken

Set in docker-compose.yml:

NGROK_AUTHTOKEN: <your_token_here>

---

## Public URL

curl http://localhost:4040/api/tunnels

---

## Structure

.
├── docker-compose.yml
├── php/index.php
└── nginx/default.conf