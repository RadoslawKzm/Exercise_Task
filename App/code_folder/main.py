# built in imports
# pip3 install imports
import requests
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

# user created modules
from App.code_folder.models import InfoResponseModel, PingRequestBody, PingResponseModel

app = FastAPI()


@app.get("/info", responses={200: {"model": InfoResponseModel}})
async def info():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"Receiver": "Cisco is the best!"})


@app.post(
    "/ping",
    responses={
        200: {"model": PingResponseModel},
        204: {"content": None, "description": "Mr.Sum Ting Wong suggests problem with url"},
    },
)
async def ping(body: PingRequestBody):
    response = requests.get(body.url)
    if response.status_code == status.HTTP_200_OK:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"content": response.text})
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)


# if __name__ == "__main__":
#     """For local development"""
#     import uvicorn
#
#     uvicorn.run(app, host="0.0.0.0", port=8000)
