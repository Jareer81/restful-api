from flask_restful import reqparse, Resource
from flask_jwt import jwt_required
from models.item import ItemModel


class ItemsList(Resource):
    def get (self):
        return {"items":[item.json() for item in ItemModel.query.all()]}



class Item (Resource):

    parser = reqparse.RequestParser ()
    parser.add_argument ("price",
                         type=float,
                         required=True)
    parser.add_argument("store id",
                        type= int,
                        required= True)

    @jwt_required()
    def get (self, name):

        item= ItemModel.find_by_name(name)

        if item:
            return item.json(), 200
        return {"message": f"item '{name}' is not available"}, 404



    def post (self, name):
        if ItemModel.find_by_name(name):
            return {"message": "The item already exists in the database"},400

        data= self.parser.parse_args()
        item= ItemModel(name, data["price"], data["store id"])

        item.save_to_db()

        return {"message": f"The item '{name}' has been added to the items list"}, 201



    def put (self, name):
        data = self.parser.parse_args ()
        item = ItemModel.find_by_name(name)

        if item:
            item.price= data['price']
            item.store_id= data['store id']
            item.save_to_db()
            return {"message": f"The item '{name}' has been updated"}, 202

        item = ItemModel(name, data['price'], data['store id'])
        item.save_to_db()
        return {"message": f"The item '{name}' has been added to the items list"}, 201

    def delete (self,name):

        item= ItemModel.find_by_name(name)
        if item is None:
            return {"message": f"The item '{name}' does not exist in the database"}, 404

        item.delete_from_db()
        return {"message": f"The item '{name}' has been deleted"}, 202
