from models.request.add_coin_in_stock import AddCoinIntoStockRequest
from fastapi import APIRouter, HTTPException, Depends
from services.coin_service import CoinService
from db.schema import SessionLocal
from sqlalchemy.orm import Session


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_coin_service(db: Session = Depends(get_db)) -> CoinService:
    return CoinService(session=db)

@router.get("/stock")
def get_coins_stock(service: CoinService = Depends(get_coin_service)):
    return service.get_coin_stock()

@router.post("/add")
def add_coin_in_stock(
    payload: AddCoinIntoStockRequest,
    service: CoinService = Depends(get_coin_service)):
    
    service.update_coin_stock(payload.coin, payload.quantity)
    return service.get_coin_stock()
