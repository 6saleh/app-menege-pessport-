import sqlite3
from .models import create_table


def get_connection():
    conn = sqlite3.connect("passports.db")
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    conn = get_connection()
    create_table(conn)
    conn.close()
