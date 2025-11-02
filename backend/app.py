from flask import Flask, jsonify
from flask_cors import CORS
from models import db, init_db
from routes import register_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///financial.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db.init_app(app)
register_routes(app)

@app.before_first_request
def setup():
    init_db(app)

@app.route('/')
def index():
    return jsonify({"message": "Financial Dashboard API is running"})

if __name__ == '__main__':
    app.run(debug=True)