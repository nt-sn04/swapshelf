from .connection import get_db_connection


def get_genres():
    db = get_db_connection()
    with db.cursor() as cursor:
        cursor.execute("SELECT id, name FROM genres")
        return cursor.fetchall()
