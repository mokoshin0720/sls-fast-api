from fastapi import FastAPI
from mangum import Mangum
from fastapi.responses import JSONResponse

app = FastAPI()
handler = Mangum(app)

@app.get("/")
def health_check():
    return JSONResponse({"status": "OK"})
