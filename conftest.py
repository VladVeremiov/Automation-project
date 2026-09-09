import json
import pytest

from api.tasks_api import TasksAPI
from api.users_api import UsersApi
from api.auth_api import AuthAPI


@pytest.fixture
def api():
    return UsersApi()

@pytest.fixture
def auth_api():
    return AuthAPI()

@pytest.fixture
def tasks_api():
    return TasksAPI()

@pytest.fixture
def access_token(auth_api,user_data):
    response = auth_api.login(user_data["valid_user"]["email"], user_data["valid_user"]["password"])
    data = response.json()
    access_token = data["access_token"]
    return access_token

@pytest.fixture
def user_data():
    with open("test_data/users.json") as file:
        users = json.load(file)
    return users


