from fastapi import APIRouter
from models.user import User
from config.db import db_users
from schemas.user import serializeDict,serializeList
from bson import ObjectId

user = APIRouter(prefix="/user",tags=['user'])

@user.get('/')
async def find_all_users():
    return serializeList(db_users.find())

@user.get('/{id}')
async def find_user(id):
    return serializeDict(db_users.find_one({"_id":ObjectId(id)}))

@user.post('/')
async def create_user(user:User):
    db_users.insert_one(dict(user))
    return serializeDict(db_users.find())

@user.put('/{id}')
async def update_user(id,user:User):
    db_users.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(user)})
    return serializeDict(db_users.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id):
    return serializeDict(db_users.find_one_and_delete({"_id":ObjectId(id)}))