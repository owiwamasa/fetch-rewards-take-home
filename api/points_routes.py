from flask import Blueprint, request, jsonify
from datetime import datetime

points_routes = Blueprint("points_routes", __name__)

transactions = []
payerBalances = {}


@points_routes.route("/")
def all_payer_balances():
    for transaction in transactions:
        payer = transaction["payer"]
        if payer not in payerBalances:
            payerBalances[payer] = transaction["points"]
        else:
            payerBalances[payer] += transaction["points"]
    return jsonify(payerBalances)


@points_routes.route("/new-transaction", methods=["POST"])
def new_transaction():
    transaction = {
        "payer": request.json["payer"],
        "points": request.json["points"],
        "timestamp": datetime.strptime(request.json["timestamp"], "%Y-%m-%dT%H:%M:%SZ"),
    }
    transactions.append(transaction)
    transactions.sort(key=lambda x: x["timestamp"])
    return jsonify(transaction)


@points_routes.route("/spend-points", methods=["PUT"])
def spend_points():
    points = request.json["points"]
