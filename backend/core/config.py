from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import Field 
from urllib.parse import quote_plus

load_dotenv()

class Config(BaseSettings):
    app_name: str = "Vending Machine"
    debug: bool = False
    
    db_user: str = Field(default="vending_user", alias="MYSQL_USER")
    db_password: str = Field(default="P@ssw0rd", alias="MYSQL_PASSWORD")
    db_root_password: str = Field(default="root", alias="MYSQL_ROOT_PASSWORD")
    db_name: str = Field(default="vending_db", alias="MYSQL_DATABASE")
    db_host: str = Field(default="localhost", alias="MYSQL_HOST")
    db_port: int = Field(default=3306, alias="MYSQL_PORT")

    @property
    def db_url(self) -> str:
        encoded_password = quote_plus(self.db_password)
        encoded_user = quote_plus(self.db_user)

        return (
            f"mysql+pymysql://{encoded_user}:{encoded_password}@"
            f"{self.db_host}:{self.db_port}/{self.db_name}"
        )

config = Config()