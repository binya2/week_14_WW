from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MYSQL_HOST: str = "localhost"
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = "Benny31."
    MYSQL_DB: str = "week_14_WW"
    MYSQL_PORT: int = 3306

settings = Settings()
