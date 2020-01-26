from flask import Flask
from flask_restful import Api
from flask_jwt import JWT, jwt_required

from authintication import authenticate, identity
from resources.user_registry import UserRegister
from resources.item_registry import Item, ItemsList
from resources.store_registry import Store
from resources.store_registry import StoreList

app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jareer'
api = Api (app)

@app.before_first_request
def create_table():
    db.create_all()

jwt = JWT (app, authenticate, identity)

api.add_resource (Item, '/item/<string:name>')
api.add_resource (Store, '/store/<string:name>')
api.add_resource (StoreList, '/storeslist')
api.add_resource (ItemsList, '/itemslist')
api.add_resource (UserRegister, '/register')

if __name__ == "__main__":
    from db import db

    db.init_app (app)
    app.run (port=5000, debug=True)
