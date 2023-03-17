from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from typing import List

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "title": "My Shop Home", "current_year": 2023})

@app.get("/catalog", response_class=HTMLResponse)
async def catalog(request: Request):
    return templates.TemplateResponse("catalog.html", {"request": request, "title": "My Shop Catalog", "current_year": 2023})

@app.get("/products", response_class=HTMLResponse)
async def catalog(request: Request):
    return templates.TemplateResponse("products.html", {"request": request, "title": "My Products", "current_year": 2023})