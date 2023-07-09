from fastapi import FastAPI
from mangum import Mangum
from fastapi.responses import JSONResponse
import src.usecase.user as user

app = FastAPI()
handler = Mangum(app)

@app.get("/")
def health_check():
    return JSONResponse({"status": "OK"})

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return JSONResponse({"user_id": user.say_hello(user_id)})