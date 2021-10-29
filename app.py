from flask import Flask
from api.points_routes import points_routes


app = Flask(__name__)

app.register_blueprint(points_routes, url_prefix='/api/points')


@app.route('/')
def home():
    return '<h1>Owen\'s Fetch Rewards Take Home Project</h1>'
