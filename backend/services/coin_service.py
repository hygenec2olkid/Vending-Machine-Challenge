from sqlalchemy.orm import Session
from sqlalchemy import select 
from db.schema import DBCoinStock
from models.coin import Coin

class CoinService:
    def __init__(self, session: Session):
        self._db = session

    def get_coin_stock(self) -> list[Coin]:
        stmt = select(DBCoinStock).order_by(DBCoinStock.coin.desc())
        result = self._db.execute(stmt)
        db_coins = result.scalars().all()
        
        return db_coins
    
    def can_change_coin(self, value: int) -> tuple[bool, dict[int, int]]:
        coin_stock = self.get_coin_stock();
        coin_dict = {coin.coin: coin.quantity for coin in coin_stock}

        coin_makes_change = {} # store coins used for change

        for coin, quality in coin_dict.items():
            coins_used = self.get_change_coin(value, coin, quality)
            value -= coins_used * coin
            coin_makes_change[coin] = coins_used

        if value > 0:
            return False, {}
                
        return True, coin_makes_change
    
    def update_coin_stock(self, coin: int, quantity_change: int) -> None:
        sql = select(DBCoinStock).where(DBCoinStock.coin == coin)
        result = self._db.execute(sql)
        coin_stock = result.scalar_one_or_none()
        
        if coin_stock:
            new_quantity = coin_stock.quantity + quantity_change
            if new_quantity < 0:
                raise ValueError(f"Insufficient stock for coin {coin}")
            coin_stock.quantity = new_quantity
        else:
            # If coin does not exist in stock, only allow adding positive quantity
            raise ValueError(f"Invalid operation for non-existing coin {coin}")
        
        self._db.commit()

    def get_change_coin(self, value: int, coin_type: int, coin_stock: int) -> int:
        if coin_type > value:
            return 0
        
        max_coins_needed = value // coin_type
        coins_to_use = min(max_coins_needed, coin_stock)

        return coins_to_use


