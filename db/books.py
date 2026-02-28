from .connection import get_db_connection


def get_genres():
    db = get_db_connection()
    with db.cursor() as cursor:
        cursor.execute("SELECT id, name FROM genres")
        return cursor.fetchall()


def create_book(telegram_id, title, author, genre_id, status, type_):
    db = get_db_connection()
    with db.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO books (added_by, title, author, genre_id, status, type)
            VALUES (
                (SELECT id FROM users WHERE telegram_id = %s),
                %s, %s, %s, %s, %s
            )
            """,
            (telegram_id, title, author, genre_id, status, type_),
        )
    db.commit()
