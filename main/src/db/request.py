import mysql.connector
from main.src.db.config import DB_CONFIG


def connect():
    db = mysql.connector.connect(host=DB_CONFIG.get('host'),
                                 database=DB_CONFIG.get('database'),
                                 user=DB_CONFIG.get('user'),
                                 password=DB_CONFIG.get('password'))
    return db
