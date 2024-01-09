from fastapi import FastAPI

app = FastAPI()

#decorate app using the path
@app.get('/')
def statApisCalling():
    return { 'data' :{'name' :'ramniwas', 'age' : 30,}}


@app.get('/about')
def getAboutPage():
    return { 'data' :{'name' :'ramniwas', 'age' : 30,}}


