import pytest

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user(api, user_id):
    response = api.get_user(user_id)
    assert response.status_code == 200

@pytest.mark.parametrize(
    "user_id, expected_name",
    [
        (1, "Leanne Graham"),
        (2, "Ervin Howell"),
        (3, "Clementine Bauch")
    ]
)
def test_user_name(api, user_id, expected_name):
    response = api.get_user(user_id)
    data = response.json()
    assert data["name"] == expected_name

@pytest.mark.parametrize(
    "username",
    [
        "Bret",
        "Antonette",
        "Samantha"
    ]
)
def test_users_by_username(api, username):
    response = api.get_users_by_username(username)
    data = response.json()
    assert response.status_code == 200
    for user in data:
        assert user["username"] == username


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

@pytest.mark.parametrize(
    "user_id, email",
    [
        (1, "new@test.com"),
        (2, "qa@test.com"),
        (3, "vlad@test.com")
    ],
    ids=[
        "new_email",
        "qa_email",
        "vlad_email"
    ]
)
def test_patch_email(api, user_id, email):
    response = api.patch_user(user_id, email)
    data = response.json()
    assert response.status_code == 200
    assert data["email"] == email

def test_delete_user(api):
    user_id = 1
    response = api.delete_user(user_id)
    assert response.status_code == 200

@pytest.mark.parametrize(
    "user_id, expected_status",
    [
        (1, 200),
        (999, 404),
        (1000, 404)
    ],
    ids=[
        "existing_user",
        "user_not_found_999",
        "user_not_found_1000"
    ]
)
def test_get_user_by_id(api, user_id, expected_status):
    response = api.get_user(user_id)
    data = response.json()
    assert response.status_code == expected_status
    if expected_status == 200:
        assert data != {}
    else:
        assert data == {}

def test_user_with_data(api):
    response = api.get_user(1)
    data = response.json()
    assert response.status_code == 200
    assert "id" in data
    assert "name" in data
    assert "email" in data

def test_users_with_unique_email(api):
    emails = []
    response = api.get_users()
    data = response.json()
    assert response.status_code == 200
    for user in data:
        emails.append(user["email"])
    assert len(emails) == len(set(emails))

