from db import db
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister (Resource):
    parser = reqparse.RequestParser ()

    parser.add_argument ('username',
                         type=str,
                         required=True,
                         help='Field is manadatory')
    parser.add_argument ('password',
                         type=str,
                         required=True,
                         help='Field is manadatory')

    def post (self):
        data = UserRegister.parser.parse_args ()

        if UserModel.find_by_username(data['username']):
            return {"message": f"The username '{data['username']}' already exists in the database"}

        user= UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message": f"User '{data['username']}' has been successfully created"}, 201