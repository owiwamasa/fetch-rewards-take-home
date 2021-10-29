from flask import Blueprint, request
from datetime import datetime
import json

points_routes = Blueprint("points_routes", __name__)

transactions = []
payerBalances = {}


@points_routes.route("/")
def all_payer_balances():
    return payerBalances


@points_routes.route("/new-transaction", methods=["POST"])
def new_transaction():
    payer = request.json["payer"]
    points = request.json["points"]
    transaction = {
        "payer": payer,
        "points": points,
        "timestamp": datetime.strptime(request.json["timestamp"], "%Y-%m-%dT%H:%M:%SZ"),
    }
    transactions.append(transaction)
    transactions.sort(key=lambda x: x["timestamp"])
    if payer not in payerBalances:
        payerBalances[payer] = points
    else:
        payerBalances[payer] += points
    return transaction


@points_routes.route("/spend-points", methods=["PUT"])
def spend_points():
    points = request.json['points']
    payer_difference = {}
    spent_points = []

    for transaction in transactions:
        if points == 0:
            break
        if points - transaction["points"] < 0:
            difference = transaction["points"] - points
            if (transaction["payer"] in payer_difference):
                payer_difference[transaction["payer"]] += points
            else:
                payer_difference[transaction["payer"]] = points
            points = 0
            break
        else:
            if transaction["points"] < 0:
                payer_difference[transaction["payer"]] += transaction["points"]
            elif (transaction["payer"] in payer_difference):
                payer_difference[transaction["payer"]] += transaction["points"]
            else:
                payer_difference[transaction["payer"]] = transaction["points"]
            points -= transaction["points"]

    if points > 0:
        return "Error: Not enough points to process this request"

    for payer in payer_difference:
        spent_points.append(
            {"payer": payer, "points": -1 * payer_difference[payer]})
        payerBalances[payer] -= payer_difference[payer]

    json_reponse = json.dumps(spent_points)
    return json_reponse
