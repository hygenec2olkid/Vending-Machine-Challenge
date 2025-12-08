from fastapi import FastAPI 
from api import product_routes, coin_routes

app = FastAPI()

app.title = "My FastAPI Application"

app.include_router(product_routes.router, prefix="/products", tags=["products"])
app.include_router(coin_routes.router, prefix="/coins", tags=["coins"])

@app.get("/")
def root():
    return {"message": "Vending Machine API is running"}

