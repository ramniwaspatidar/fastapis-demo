
def todo_serializer(todo) -> dict:
    return {
        "id" : str(todo["_id"]),
         "name" : todo["name"],
        "description" : todo["description"],
        "complete" : todo["complete"]
    }


def todo_serializer_list(todos) -> list:
    return [todo_serializer(todo) for todo in todos]