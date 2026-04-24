import psycopg2
from config import DB_CONFIG

def get_connection():
    """Установка соединения с базой данных"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.Error as e:
        print(f"Ошибка подключения к базе данных: {e}")
        raise