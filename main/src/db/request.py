import os
import mysql.connector


def connect():
    db = mysql.connector.connect(host=os.getenv('DB_HOST'),
                                 database=os.getenv('DB_DATABASE'),
                                 user=os.getenv('DB_USER'),
                                 password=os.getenv('DB_PASSWORD'))
    return db
