import pytest
from main.src.api.request import *


def test_connection():
    assert get('/todos/1').status_code == 200
