from flask import Blueprint, request


points_routes = Blueprint("points_routes", __name__)

transactions = []


@points_routes.route("/")
def all_payer_balances():
    payerInfo = {}
    for transaction in transactions:
        payer = transaction["payer"]
        if payer not in payerInfo:
            payerInfo[payer] = transaction["points"]
        else:
            payerInfo[payer] += transaction["points"]
    return payerInfo


@points_routes.route("/new-transaction", methods=["POST"])
def new_transaction():
    transaction = {
        "payer": request.json["payer"],
        "payee": request.json["payee"],
        "points": request.json["points"],
    }
    transactions.append(transaction)
    return transaction
