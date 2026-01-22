from .connection import get_db_connection, settings, get_db_first_connection
from models import WeaponsDB


def init_tables():
    try:
        conn = get_db_first_connection()
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {settings.MYSQL_DB};")
        cursor.execute(f"USE {settings.MYSQL_DB};")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weapons (
                id INT AUTO_INCREMENT PRIMARY KEY,
                weapon_id VARCHAR(10) NOT NULL,
                weapon_name VARCHAR(20) NOT NULL,
                weapon_type VARCHAR(20) NOT NULL,
                range_km INT NOT NULL,
                weight_kg FLOAT NOT NULL,
                manufacturer VARCHAR(20) NOT NULL,
                origin_country VARCHAR(20) NOT NULL,
                storage_location VARCHAR(20) NOT NULL,
                year_estimated INT NOT NULL,
                risk_level VARCHAR(20) NOT NULL);
        """)
        conn.commit()
        conn.close()
        print("Tables initialized.")
    except Exception as e:
        print(f"Table Init Error: {e}")


def insert_weapon(data: WeaponsDB)-> bool:
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = (f"INSERT INTO weapons (weapon_id, weapon_name, weapon_type, range_km, weight_kg, "
               f"manufacturer, origin_country, storage_location, year_estimated, risk_level) "
               f"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);")
        values = (data.weapon_id, data.weapon_name, data.weapon_type, data.range_km,
                  data.weight_kg, data.manufacturer, data.origin_country, data.storage_location,
                  data.year_estimated, data.risk_level)
        cursor.execute(sql, values)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        raise Exception(f"Insert failed: {str(e)}")

def fetch_all_weapons()-> list[dict]:
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM weapons;")
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as e:
        raise Exception(f"Fetch failed: {str(e)}")