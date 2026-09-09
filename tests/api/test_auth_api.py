import json
import uuid
from api.auth_api import AuthAPI
api = AuthAPI()

def test_register_api():
    unique_id = str(uuid.uuid4())[:8]
    email = f"test_{unique_id}@example.com"
    password = "Test123!"
    name = "Test User"
    response = api.register_user(email, password, name)
    assert response.status_code == 201
    data = response.json()
    assert data["user"]["email"] == email
    assert data["user"]["name"] == name

def test_login_api(user_data):

    response = api.login(user_data["valid_user"]["email"], user_data["valid_user"]["password"])
    assert response.status_code == 200
    data = response.json()
    access_token = data["access_token"]
    assert data["access_token"]
    print(access_token)

def test_auth_me_api(auth_api, access_token, user_data):
    response = auth_api.auth_me(access_token)
    assert response.status_code == 200
    data = response.json()
    assert "user" in data
    assert data["user"]["email"] == user_data["valid_user"]["email"]




