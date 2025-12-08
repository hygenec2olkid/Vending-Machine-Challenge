from sqlalchemy.orm import Session
from sqlalchemy import select 
from db.schema import DBProductInventory
from models.product import Product
from services.coin_service import CoinService   

class ProductService:
    def __init__(self, session: Session):
        self._db = session
        self.coin_service = CoinService(session=session)  

    def get_product_stock(self) -> list[Product]:
        stmt = select(DBProductInventory) 
        result = self._db.execute(stmt)
        
        return result.scalars().all()
    
    def buy_product(self, product_id: int, amount: int, balance: int) -> dict[int, int]:
        stmt = select(DBProductInventory).where(DBProductInventory.id == product_id)
        result = self._db.execute(stmt)
        product = result.scalar_one_or_none()
        
        if product is None:
            raise ValueError("Product not found")
        
        if product.quantity <= 0 or product.quantity < amount:
            raise ValueError("Product out of stock")
        
        if balance < product.price * amount:
            raise ValueError("Balance is insufficient for purchase product")
        
        result = self.coin_service.can_change_coin(balance - (product.price * amount))
        if result[0] is False:
            raise ValueError("Machine cannot provide coin to change for purchase product")
        
        for coin_value, qty in result[1].items():
            self.coin_service.update_coin_stock(coin_value, -qty)
        
        product.quantity -= amount
        self._db.commit()
        
        return result[1]


