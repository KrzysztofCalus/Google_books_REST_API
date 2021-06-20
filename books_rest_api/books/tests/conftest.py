import pytest
from rest_framework.test import APIClient
from .utils import create_book


@pytest.fixture()
def client():
    client = APIClient()
    return client


@pytest.fixture
def set_up():
    create_book()
