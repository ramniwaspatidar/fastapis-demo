from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()


# get all blogs
@app.get('/')
def index():
    return {'data' : 'blog list'}

@app.get('/blog') # query params
def blogLimit(limit = 10,published : bool = True, sort : Optional[str] = None):

    if published:
        return {'data' : f'{limit} published blogs from the db'}
    elif sort:
        return {'data' : 'sort list'}
    else:
        return {'data' : f'all data from the db'}


@app.get('/blog/unpublished')
def getUnpublishedBlog():
    return {'data' : "List of unpublished blogs"}


@app.get('/blog/{id}')
def blog(id : int):
    return {'data' : id}


@app.get('/blog/{id}/comments')
def getBlogComments(id):
    return {'data' : ['1','2','3']}


class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool] = False



@app.post('/blog')
def getblogRequest(request : Blog):
    return {'data' : f"Blog is crreated with {request.title}"}


