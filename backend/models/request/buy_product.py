from pydantic import BaseModel

class BuyProductRequest(BaseModel):
    id: int 
    quality: bool 
    balance: int
    