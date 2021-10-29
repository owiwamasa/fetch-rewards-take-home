import requests


transactions = [
    {"payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z"},
    {"payer": "UNILEVER", "points": 200, "timestamp": "2020-10-31T11:00:00Z"},
    {"payer": "DANNON", "points": -200, "timestamp": "2020-10-31T15:00:00Z"},
    {"payer": "MILLER COORS", "points": 10000,
        "timestamp": "2020-11-01T14:00:00Z"},
    {"payer": "DANNON", "points": 300, "timestamp": "2020-10-31T10:00:00Z"},
]

for transaction in transactions:
    response = requests.post(
        "http://127.0.0.1:5000/api/points/new-transaction", json=transaction)
    print(response.json())

response = requests.put(
    "http://127.0.0.1:5000/api/points/spend-points", json={"points": 5000})
print(response.json())

response = requests.get("http://127.0.0.1:5000/api/points/")
print(response.json())
