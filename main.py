from fastapi import FastAPI
import datetime


app = FastAPI()


@app.get('/hello')
def hello_world():
    return  {
        "message": "Hello World Updated Via Cicd",
        "time": datetime.datetime.now(),
        "status": 200,
    }