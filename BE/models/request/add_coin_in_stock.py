from pydantic import BaseModel

class AddCoinIntoStockRequest(BaseModel):
    coin: int 
    quantity: int
    