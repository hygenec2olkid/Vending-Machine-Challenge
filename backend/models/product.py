from pydantic import BaseModel

class Product(BaseModel):
    id: int 
    name: str 
    price: float 
    quality: int 
    img_url: str
    