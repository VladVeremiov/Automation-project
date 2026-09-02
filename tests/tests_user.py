

def test_get_user(api):
    response = api.get_user(1)
    assert response.status_code == 200

def test_user_name(api):
    response = api.get_user(1)
    data = response.json()
    assert data["name"] == "Leanne Graham"

def test_get_all_users(api):
    response = api.get_users()
    assert response.status_code == 200

def test_all_users_have_id(api):
    response = api.get_users()
    data = response.json()
    for user in data:
        assert "id" in user

def test_all_users_type_id(api):
    response = api.get_users()
    data = response.json()
    for user in data:
        assert type(user["id"]) == int

def test_all_users_email(api):
    response = api.get_users()
    data = response.json()
    for user in data:
        assert "@" in user["email"]

def test_number_of_users(api):
    response = api.get_users()
    data = response.json()
    assert len(data) == 10

def test_create_user(api):
    response = api.create_user(name="Vlad", email="vlad@test.com")
    data = response.json()
    assert response.status_code == 201
    assert "id" in data
    assert data["name"] == "Vlad"
    assert data["email"] == "vlad@test.com"

def test_update_user(api):
    user_id = 1
    name = "Vlad"
    email = "vlad@test.com"
    response = api.update_user(user_id, name, email)
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == name
    assert data["email"] == email

def test_patch_email(api):
    user_id = 1
    email = "new@test.com"
    response = api.patch_user(user_id, email)
    data = response.json()
    assert response.status_code == 200
    assert data["email"] == email

def test_delete_user(api):
    user_id = 1
    response = api.delete_user(user_id)
    assert response.status_code == 200

def test_get_user_by_id(api):
    user_id = 999
    response = api.get_user(user_id)
    data = response.json()
    assert response.status_code == 404
    assert data == {}

def test_user_with_data(api):
    response = api.get_user(1)
    data = response.json()
    assert response.status_code == 200
    assert "id" in data
    assert "name" in data
    assert "email" in data