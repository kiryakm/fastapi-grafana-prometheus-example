from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()


@app.get("/")
def hello():
    return "Hello World"


@app.get("/test")
def test(i: bool):
    if not i:
        raise HTTPException(status_code=400)
    else:
        return "ok"


Instrumentator().instrument(app).expose(app)
