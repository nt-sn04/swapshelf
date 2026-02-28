import psycopg2

from config import Settings


def get_db_connection():
    connection = psycopg2.connect(
        host=Settings.DB_HOST,
        port=Settings.DB_PORT,
        dbname=Settings.DB_NAME,
        user=Settings.DB_USER,
        password=Settings.DB_PASSWORD,
    )
    return connection
