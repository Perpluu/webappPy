from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

products = [
    {"name": "Product 1", "price": 10.99},
    {"name": "Product 2", "price": 5.99},
    {"name": "Product 3", "price": 15.99},
    {"name": "Product 4", "price": 25.99}
]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "title": "My Shop Home", "current_year": 2023})

@app.get("/catalog", response_class=HTMLResponse)
async def catalog(request: Request):
    return templates.TemplateResponse("catalog.html", {"request": request, "title": "My Shop Catalog", "current_year": 2023})

@app.get("/products", response_class=HTMLResponse)
async def products(request: Request):
    return templates.TemplateResponse("products.html", {"request": request, "title": "My Products", "current_year": 2023})

@app.route("/cart")
async def cart(request: Request):
    return templates.TemplateResponse("cart.html", {"request": request, "products": products})
