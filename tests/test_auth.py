import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def test_auth():
    user = os.getenv("API_USERNAME")
    password = os.getenv("API_PASSWORD")
    response = requests.post(
    "https://dummyjson.com/auth/login",
    json={
        "username": user,
        "password": password
    }
)
    assert response.status_code == 200
    data = response.json()
    token = data["accessToken"]

    response = requests.get(
    "https://dummyjson.com/auth/me",
    headers={
        "Authorization": f"Bearer {token}"}
)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "emilys"
    assert data["id"] == 1

def test_auth_chain():
    user = os.getenv("API_USERNAME")
    password = os.getenv("API_PASSWORD")
    response = requests.post(
        "https://dummyjson.com/auth/login",
        json={
            "username": user,
            "password": password
        }
    )
    assert response.status_code == 200
    data = response.json()
    token = data["accessToken"]

    response = requests.get(
    "https://dummyjson.com/auth/me",
    headers={
        "Authorization": f"Bearer {token}"
    }
    )
    assert response.status_code == 200
    data = response.json()
    user_id = data["id"]
    print(user_id)

    response = requests.get(
    f"https://dummyjson.com/users/{user_id}"
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id


def test_auth_invalid_password():
    user = os.getenv("API_USERNAME")
    password = "12345"
    response = requests.post(
        "https://dummyjson.com/auth/login",
        json={
            "username": user,
            "password": password
        }
    )
    assert response.status_code == 400

def test_auth_invalid_username():
    user = "invalidpassword"
    password = os.getenv("API_PASSWORD")
    response = requests.post(
        "https://dummyjson.com/auth/login",
        json={
            "username": user,
            "password": password
        }
    )
    assert response.status_code == 400

def test_request_error_try_except():
    try:
        response = requests.get(
            "https://www.saucedemo.com:81",
            timeout=5
        )
    except requests.exceptions.RequestException:
        print("Request failed")

def test_request_error_with():
    with pytest.raises(requests.exceptions.RequestException):
        requests.get(
            "https://www.saucedemo.com:81",
            timeout=5
        )
