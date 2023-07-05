from fastapi import APIRouter
from models.project import Project
from config.db import db_projects
from schemas.project import serializeDict,serializeList
from bson import ObjectId

project = APIRouter(prefix="/project",tags=['project'])

@project.get('/')
async def find_all_projects():
    return serializeList(db_projects.find())

@project.get('/{id}')
async def find_project(id):
    return serializeDict(db_projects.find_one({"_id":ObjectId(id)}))

@project.post('/')
async def create_project(project:Project):
    db_projects.insert_one(dict(project))
    return serializeDict(db_projects.find())

@project.put('/{id}')
async def update_project(id,project:Project):
    db_projects.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(project)})
    return serializeDict(db_projects.find_one({"_id":ObjectId(id)}))    

@project.delete('/{id}')
async def delete_project(id):
    return serializeDict(db_projects.find_one_and_delete({"_id":ObjectId(id)}))






