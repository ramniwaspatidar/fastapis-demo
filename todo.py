from fastapi import FastAPI
from routes.todo_routes import todo_apis_router

app = FastAPI()
app.include_router(todo_apis_router)




