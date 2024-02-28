from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import requests
import json
import os
import sys

app = FastAPI()


@app.get("/")
def read_root():
    html_content = os.open("html/index.html", os.O_RDONLY)
    html_content = os.read(html_content, 1000)
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/theme/{theme_name}")
def read_item(theme_name: str):
    return {"theme_name": theme_name}





# run the server with the command: uvicorn main:app --reload
