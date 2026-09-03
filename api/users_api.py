import requests
BASE_URL = "https://jsonplaceholder.typicode.com"

class UsersApi:
    headers = {
        "Accept": "application/json",
    }

    def get_user(self, user_id):
        response = requests.get(
            f"{BASE_URL}/users/{user_id}",
            headers=self.headers
        )
        return response

    def get_users(self):
        response = requests.get(
            f"{BASE_URL}/users"
        )
        return response

    def get_users_by_username(self, username):
        response = requests.get(
            f"{BASE_URL}/users",
            params={
                "username": username
            }
        )
        return response

    def create_user(self, name, email):
        response = requests.post(
            f"{BASE_URL}/users",
            json={
                "name": name,
                "email": email
            }
        )
        return response

    def update_user(self, user_id, name, email):
        response = requests.put(
            f"{BASE_URL}/users/{user_id}",
            json={
                "name": name,
                "email": email
            }
        )
        return response

    def patch_user(self, user_id, email):
        response = requests.patch(
            f"{BASE_URL}/users/{user_id}",
            json={
                "email": email
            }
        )
        return response

    def delete_user(self, user_id):
        response = requests.delete(
            f"{BASE_URL}/users/{user_id}"
        )
        return response