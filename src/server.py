from fastapi import FastAPI
from mangum import Mangum
from fastapi.responses import JSONResponse
from src.usecase.user.get import get as uget

app = FastAPI()
handler = Mangum(app)

@app.get("/")
def health_check():
    return JSONResponse({"status": "OK"})

@app.get("/user/{user_id}")
def get_user(user_id: int):
    res = uget(user_id)
    return JSONResponse({"res": res})