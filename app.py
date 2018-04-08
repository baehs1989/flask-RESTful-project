from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity as identify_function

import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'alexhyungsoobae'
api = Api(app)

#DB tables created in first call
@app.before_first_request
def create_tables():
    db.create_all()

app.config['JWT_AUTH_URL_RULE'] = '/get_token' #if you want to use /login instead of /auth(Default)
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=1800)
# app.config['JWT_AUTH_USERNAME_KEY'] = 'id'
jwt = JWT(app, authenticate, identify_function) #jwt implementation



if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
