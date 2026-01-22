import time

import mysql.connector

from core.errors import DBError
from core.settings import settings


def get_db_connection():
    retries = 10
    while retries > 0:
        try:
            return mysql.connector.connect(
                host=settings.MYSQL_HOST,
                user=settings.MYSQL_USER,
                password=settings.MYSQL_PASSWORD,
                # database=settings.MYSQL_DB,
                port=settings.MYSQL_PORT
            )
        except mysql.connector.Error as err:
            time.sleep(2)
            retries -= 1

    raise DBError("Failed to connect to MySQL")
