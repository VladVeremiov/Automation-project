def test_create_task_api(tasks_api, access_token):
    title = "Test Task"
    description = "Test Description"
    priority = "medium"
    status = "backlog"
    response = tasks_api.create_task(access_token, title, description, priority, status)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == title
    assert data["description"] == description
    assert data["priority"] == priority
    assert data["status"] == status

def test_get_all_tasks_api(tasks_api, access_token):
    response = tasks_api.get_all_tasks(access_token)
    assert response.status_code == 200
    data = response.json()
    assert "tasks" in data
    assert type(data["tasks"]) == list
    assert "meta" in data
    assert data["meta"]["count"] == len(data["tasks"])

def test_get_task_by_id(tasks_api, access_token):
    response = tasks_api.get_all_tasks(access_token)
    assert response.status_code == 200
    data = response.json()
    task_id = data["tasks"][0]["id"]

    response = tasks_api.get_task_by_id(access_token, task_id)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id

def test_update_task_by_id(tasks_api, access_token):
    response = tasks_api.get_all_tasks(access_token)
    assert response.status_code == 200
    data = response.json()
    task_id = data["tasks"][0]["id"]

    title = "Updated Title"
    description = "Updated Description"
    priority = "medium"
    status = "backlog"

    response = tasks_api.update_task_by_id(access_token, task_id, title, description, priority, status)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == title
    assert data["description"] == description
    assert data["priority"] == priority
    assert data["status"] == status

def test_delete_task_by_id(tasks_api, access_token):
    title = "Test Task"
    description = "Test Description"
    priority = "medium"
    status = "backlog"
    response = tasks_api.create_task(access_token, title, description, priority, status)
    assert response.status_code == 201
    data = response.json()
    task_id = data["id"]

    response = tasks_api.delete_task_by_id(access_token, task_id)
    assert response.status_code == 200

    response = tasks_api.get_task_by_id(access_token, task_id)
    assert response.status_code == 404

def test_update_task_status_by_id(tasks_api, access_token):
    title = "Test Task"
    description = "Test Description"
    priority = "medium"
    status = "backlog"
    response = tasks_api.create_task(access_token, title, description, priority, status)
    assert response.status_code == 201
    data = response.json()
    task_id = data["id"]

    status = "in_progress"

    response = tasks_api.update_task_status(access_token, task_id, status)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == status

    response = tasks_api.get_task_by_id(access_token, task_id)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "in_progress"


