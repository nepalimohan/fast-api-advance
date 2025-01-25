from typing import Optional
from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    ENV_STATE: Optional[str] = None
    class Config:
        env_file: str = ".env"
        

class GlobalConfig(BaseConfig):
    DATABASE_URL: Optional[str] = None
    DB_FORCE_ROLL_BACK: bool = False
    
    
class DevConfig(GlobalConfig):
    class Config:
        env_prefix: str = "DEV_"


class TestConfig(GlobalConfig):
    DATABASE_URL = "sqlite:///test.db"
    DB_FORCE_ROLL_BACK: bool = True
    class Config:
        env_prefix: str = "TEST_"


class ProductionConfig(GlobalConfig):
    class Config:
        env_prefix: str = "PROD_"