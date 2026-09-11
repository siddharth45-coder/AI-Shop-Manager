import sqlite3


DATABASE = "shop.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    return connection


def create_product_table():

    connection = get_connection()

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                stock INTEGER NOT NULL,
                category TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

        connection.commit()

    finally:
        connection.close()


def get_all_products():

    connection = get_connection()

    try:
        cursor = connection.execute("""
            SELECT *
            FROM products
            ORDER BY id DESC
        """)

        return cursor.fetchall()

    finally:
        connection.close()


def add_product(name, price, stock, category):

    connection = get_connection()

    try:
        connection.execute("""
            INSERT INTO products
            (name, price, stock, category)
            VALUES (?, ?, ?, ?)
        """, (
            name,
            price,
            stock,
            category
        ))

        connection.commit()

    finally:
        connection.close()


def delete_product(product_id):

    connection = get_connection()

    try:
        connection.execute("""
            DELETE FROM products
            WHERE id = ?
        """, (product_id,))

        connection.commit()

    finally:
        connection.close()
