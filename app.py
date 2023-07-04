from fastapi import FastAPI
from mangum import Mangum
from fastapi.responses import JSONResponse
import uvicorn
app = FastAPI()
handler = Mangum(app)


@app.get("/{text}")
def read_item(text: str):
    return JSONResponse({"result": text})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)