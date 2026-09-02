import pytest
from api.users_api import UsersApi

@pytest.fixture
def api():
    return UsersApi()
