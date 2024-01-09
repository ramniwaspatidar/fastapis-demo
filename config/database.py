from pymongo import MongoClient

client = MongoClient('mongodb+srv://ramniwaspatidar:FDtcQ1q6qlBv5Ptk@cluster0.lgj7jzf.mongodb.net/mydatabase?retryWrites=true&w=majority')

db = client.todo_database
collection = db["todo_collection"]