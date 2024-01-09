from  fastapi import APIRouter
from config.database import collection
from models.todo_models import ToDoMOdel
from schemas.todo_schemas import todo_serializer,todo_serializer_list
from bson import ObjectId



todo_apis_router = APIRouter()


#retrieve

@todo_apis_router.get('/')
async def get_todo():
    todos = todo_serializer_list(collection.find())
    return {'data' : todos, 'status' : "Ok"}


@todo_apis_router.get('/{id}')
async def get_todo_by_id(id : str):
    todo = todo_serializer_list(collection.find({ '_id' : ObjectId(id)}))
    return{'data' : todo, 'status' : "OK"}


@todo_apis_router.post('/')
async def post_todo(todo :ToDoMOdel):
   _id =  collection.insert_one(dict(todo))
   getTodoFromDB = todo_serializer_list(collection.find({ '_id' : _id.inserted_id}))
   return{'data' : getTodoFromDB, 'status' : "OK"}



@todo_apis_router.put('/{id}')
async def update_todo(id : str,todo : ToDoMOdel):
    collection.find_one_and_update({"_id" : ObjectId(id)},{
        "$set" : dict(todo)
    })
    todo = collection.find({"_id" : ObjectId(id)})
    return{'data' : todo, 'status' : "OK"}


@todo_apis_router.delete('/{id}')
async def deleteApis(id : str):
    todo = collection.find_one_and_delete({"_id" : ObjectId(id)})
    return{'data' : [], 'status' : "OK", 'message' : 'Delete operation perfrom successfully'}







