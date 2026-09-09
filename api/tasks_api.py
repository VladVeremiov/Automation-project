import requests
BASE_URL = "https://dojo.upexgalaxy.com"

class TasksAPI:
    def create_task(self, access_token, title, description, priority, status):
        response = requests.post(
            url=f"{BASE_URL}/api/tasks",
            headers={"Authorization": f"Bearer {access_token}"},
            json={
                "title": title,
                "description": description,
                "priority": priority,
                "status": status},
        )
        return response
