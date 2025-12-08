from fastapi import FastAPI, Request, status
from api import product_routes, coin_routes
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

app.title = "My FastAPI Application"

origins = [
    "http://localhost:5174",
]

# 2. Add the CORSMiddleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,                    
    allow_credentials=True,                   
    allow_methods=["*"],                      
    allow_headers=["*"],                      
)

@app.exception_handler(ValueError)
async def value_error_exception_handler(request: Request, exc: ValueError):
    print(f"ValueError caught: {exc}")
    
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": str(exc)},
    )

app.include_router(product_routes.router, prefix="/products", tags=["products"])
app.include_router(coin_routes.router, prefix="/coins", tags=["coins"])

@app.get("/")
def root():
    return {"message": "Vending Machine API is running"}

