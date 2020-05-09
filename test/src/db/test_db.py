import pytest
import mysql.connector
from main.src.db.request import *


def test_connection():
    try:
        connect()
    except mysql.connector.errors as e:
        assert False
    assert True
