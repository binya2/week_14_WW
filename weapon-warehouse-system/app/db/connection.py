import time

import mysql.connector
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MYSQL_HOST: str = "localhost"
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = "password"
    MYSQL_DB: str = "weapons"
    MYSQL_PORT: int = 3306


settings = Settings()


def get_db_connection():
    settings = Settings()
    retries = 10
    while retries > 0:
        try:
            print(f"Connecting to DB at {settings.MYSQL_HOST}...")
            return mysql.connector.connect(
                host=settings.MYSQL_HOST,
                user=settings.MYSQL_USER,
                password=settings.MYSQL_PASSWORD,
                database=settings.MYSQL_DB,
                port=settings.MYSQL_PORT
            )
        except mysql.connector.Error as err:
            print(f"DB Error: {err}. Retrying...")
            time.sleep(2)
            retries -= 1

    raise Exception("Could not connect to MySQL after multiple attempts")
