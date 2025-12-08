from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from core.config import config

engine = create_engine(config.db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class DBCoinStock(Base):
    __tablename__ = "coin_stock"

    coin = Column('coin', Integer, primary_key=True) 
    quantity = Column(Integer, nullable=False, default=0)
    
class DBProductInventory(Base):
    __tablename__ = "product_inventory"

    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False, default=0)

