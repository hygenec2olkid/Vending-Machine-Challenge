from pydantic import BaseModel

class Coin(BaseModel):
    coin: int 
    quantity: int
    