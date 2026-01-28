from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "API Gateway - Pedidos Veloz"

@app.route("/pedidos")
def pedidos():
    return requests.get("http://pedidos:5000").text

@app.route("/pagamentos")
def pagamentos():
    return requests.get("http://pagamentos:5000").text

@app.route("/estoque")
def estoque():
    return requests.get("http://estoque:5000").text

app.run(host="0.0.0.0", port=5000)
