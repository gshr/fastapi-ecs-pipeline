from fastapi import FastAPI
import datetime


app = FastAPI()


@app.get('/hello')
def hello_world():
    return  {
        "message": "Hello World",
        "time": datetime.datetime.now(),
        "status": 200,
    }