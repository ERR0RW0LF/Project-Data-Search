from typing import Union
from fastapi import FastAPI, HTTPException, Request, status
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse, RedirectResponse, Response, StreamingResponse, PlainTextResponse
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
import json
import os
import sys

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
app.add_middleware(GZipMiddleware)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("home-page.html", {"request": request})




# run the server with the command: uvicorn main:app --reload
