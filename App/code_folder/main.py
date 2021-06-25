# built in imports
# pip3 install imports
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import requests


# user created modules


class GetResponseModel(BaseModel):
    Receiver: str = "is Cisco the best!"


class PostRequest(BaseModel):
    url: str = "http://cisco.com"


class PostResponseModel(BaseModel):
    content: str


app = FastAPI()


@app.get("/info", responses={200: {"model": GetResponseModel}})
async def info():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"Receiver": "Cisco is the best!"})


@app.post("/ping", responses={200: {"model": PostResponseModel},
                              204: {"content": None, "description": "Mr.Sum Ting Wong suggests problem with url"}})
async def ping(body: PostRequest):
    response = requests.get(body.url)
    if response.status_code == status.HTTP_200_OK:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"content": response.text})
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
