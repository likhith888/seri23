from fastapi import APIRouter
from models.project import Project
from config.db import db_projects
from schemas.project import serializeDict,serializeList
from bson import ObjectId
import json

project = APIRouter(prefix="/project",tags=['project'])

@project.get('/')
async def find_all_projects():
    return serializeList(db_projects.find())
    
@project.get('/{id}')
async def find_project(id):
    return serializeDict(db_projects.find_one({"_id":ObjectId(id)}))

@project.get('/{id}/sensors')
async def find_sensors(id):
    record = db_projects.find_one({"_id":ObjectId(id)})
    if(record):
        return {"internal_temp":record['internal_temp'],"external_temp":record['external_temp'],"internal_humidity":record['internal_humidity'],"external_humidity":record['external_humidity'],"roof_temp":record['roof_temp'],"roof_humidity":record['roof_humidity']}

@project.get('/{id}/actuators')
async def find_actuators(id):
    record = db_projects.find_one({"_id":ObjectId(id)})
    if(record):
        return {"exhaust_state":record['exhaust_state'],"sprinkeler_state":record['sprinkeler_state'],"override":record['override'],"reset":record['reset']}

@project.post('/')
async def create_project(project:Project):
    db_projects.insert_one(dict(project))
    return serializeDict(db_projects.find())

# @project.put('/{id}')
# async def update_project(id,body:str):
#     db_projects.find_one_and_update({"_id":ObjectId(id)},{"$set":json.loads(body)})
#     return serializeDict(db_projects.find_one({"_id":ObjectId(id)}))    

@project.put('/{id}')
async def update_project(id: str, body):
    # Log the received request information

    # print(body)

    print("Received PUT request for project with ID:", id)
    print("Request Body:", body)

    # Your existing code to update the project and retrieve the response
    db_projects.find_one_and_update({"_id": ObjectId(id)}, {"$set": json.loads(body)})
    response = serializeDict(db_projects.find_one({"_id": ObjectId(id)}))
    
    # Log the response information
    print("Response:", response)

    return response

project_router = APIRouter(prefix="/project", tags=['project'])
project_router.include_router(project_router)

@project.delete('/{id}')
async def delete_project(id):
    return serializeDict(db_projects.find_one_and_delete({"_id":ObjectId(id)}))

@project.get('/{id}/override')
async def override(id):
    record = db_projects.find_one({"_id":ObjectId(id)})
    if(record):
        return record['override']

@project.get('/{id}/reset_device')
async def resetDevice(id):
    record = db_projects.find_one({"_id":ObjectId(id)})
    if(record):
        return record['reset']




