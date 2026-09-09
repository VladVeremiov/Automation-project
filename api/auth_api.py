import requests
BASE_URL = "https://dojo.upexgalaxy.com"

class AuthAPI:
    def register_user(self, email, password, name):
        response = requests.post(
            url=f"{BASE_URL}/api/auth/register",
            json={
                "email": email,
                "password": password,
                "name": name
            }
        )
        return response

    def login(self, email, password):
        response = requests.post(
            url=f"{BASE_URL}/api/auth/login",
            json={
                "email": email,
                "password": password
            }
        )
        return response

    def auth_me(self, access_token):
        response = requests.get(
            url=f"{BASE_URL}/api/auth/me",
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )
        return response