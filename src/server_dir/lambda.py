from fastapi import FastAPI
from mangum import Mangum
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()
handler = Mangum(app)

@app.get("/")
def health_check():
    return JSONResponse({"status": "OK"})


@app.get("/{text}")
def read_item(text: str):
    return JSONResponse({"result": text})
