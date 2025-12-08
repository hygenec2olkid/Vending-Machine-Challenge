from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.schema import SessionLocal
from services.product_service import ProductService
from models.request.buy_product import BuyProductRequest

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_product_service(db: Session = Depends(get_db)) -> ProductService:
    return ProductService(session=db)

@router.get("/stock")
def get_products(service: ProductService = Depends(get_product_service)):
    return service.get_product_stock()

@router.post("/purchase")
def buy_product(
    payload: BuyProductRequest,
    service: ProductService = Depends(get_product_service)):
    return service.buy_product(payload.id, payload.quality, payload.balance)