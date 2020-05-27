import pytest
from main.src.api.request import *


def test_connection():
    req = Request()
    assert req.get('/todos/1').status_code == 200
