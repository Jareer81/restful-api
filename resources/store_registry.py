from flask_restful import Resource
from models.store import StoreModel

class Store (Resource):

    def get(self, name):
        store= StoreModel.find_by_name(name)
        if store:
            return store.json(), 202

        return {"message":f"The store '{name}' does not exist in the database"}, 404

    def post( self, name ):
        if StoreModel.find_by_name(name):
            return {"message": f"The store '{name}' already exists"}, 400

        store = StoreModel(name)
        store.save_to_db()
        return store.json(), 201

    def delete( self, name ):
        store= StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

            return {"message": "The store has been deleted"}, 202

        return {"message": "The store does not exist in the database"}, 404

class StoreList(Resource):

    def get( self ):
        storelist= StoreModel.query.all()

        return {"Stores": [store.json() for store in storelist]},202








