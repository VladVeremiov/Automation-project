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

    def get_task_by_id(self, access_token, id):
        response = requests.get(
            url=f"{BASE_URL}/api/tasks/{id}",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        return response

    def get_all_tasks(self, access_token):
        response = requests.get(
            url=f"{BASE_URL}/api/tasks",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        return response

    def update_task_by_id(self, access_token, id, title, description, priority, status):
        response = requests.put(
            url=f"{BASE_URL}/api/tasks/{id}",
            headers={"Authorization": f"Bearer {access_token}"},
            json={
                "title": title,
                "description": description,
                "priority": priority,
                "status": status
            }
        )
        return response

    def delete_task_by_id(self, access_token, id):
        response = requests.delete(
            url=f"{BASE_URL}/api/tasks/{id}",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        return response

    def update_task_status(self, access_token, id, status):
        response = requests.patch(
            url=f"{BASE_URL}/api/tasks/{id}/status",
            headers={"Authorization": f"Bearer {access_token}"},
            json={
                "status": status
            }
        )
        return response