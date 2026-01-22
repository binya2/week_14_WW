from connection import get_db_connection, settings


def init_tables():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {settings.MYSQL_DB};")
        cursor.execute(f"USE {settings.MYSQL_DB};")
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS weapons
                       (
                           id
                           INT
                           AUTO_INCREMENT
                           PRIMARY
                           KEY,
                           weapon_id
                           INT
                           not
                           NULL,
                           weapon_name
                           VARCHAR
                       (
                           50
                       ) not NULL,
                           weapon_type VARCHAR
                       (
                           50
                       ) not NULL,
                           range_km INT not NULL,
                           weight_kg FLOAT not NULL,
                           manufacturer VARCHAR
                       (
                           50
                       ) not NULL,
                           origin_country VARCHAR
                       (
                           50
                       ) not NULL,
                           storage_location VARCHAR
                       (
                           50
                       ) NOT NULL,
                           year_estimated INT not NULL,
                           risk_level VARCHAR
                       (
                           50
                       ),
                           timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                           )
                       """)
        conn.commit()
        conn.close()
        print("Tables initialized.")
    except Exception as e:
        print(f"Table Init Error: {e}")


def insert_record(name: str, value: float, category: str):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO records (name, value, category) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, value, category))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        raise Exception(f"Insert failed: {str(e)}")
