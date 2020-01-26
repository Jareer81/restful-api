from models.user import UserModel

def authenticate (username, password):
    user = UserModel.find_by_username(username)
    if ((user is not None) and (user.password == password)):
        return user
    else:
        return {"message":"username or password is incorrect"}


def identity (payload):
    user_id = payload['identity']
    if user_id:
        return UserModel.find_by_userid(user_id)
    else:
        return {"message": "username or password is incorrect"}