import pytest
from db.connection import create_connection

def test_user_exists():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users;')
    rows = cursor.fetchall()
    assert any(
        row[2] == 'qa@test.com'
        for row in rows
    )
    cursor.close()
    connection.close()

def test_developer_age(db_cursor):
    db_cursor.execute("SELECT * FROM users WHERE age = 28;")
    rows = db_cursor.fetchall()
    assert any(
        row[1] == 'developer' and row[3] == 28
        for row in rows
    )

def test_qa_user_email(db_cursor):
    db_cursor.execute("SELECT * FROM users WHERE username = 'qa_user';")
    row = db_cursor.fetchone()
    assert row is not None
    assert row[2] == 'qa@test.com'

@pytest.mark.parametrize(
    "username, expected_email",
    [
        ("admin", "admin@test.com"),
        ("qa_user", "qa@test.com"),
        ("tester", "tester@test.com"),
        ("developer", "dev@test.com")
    ]
)
def test_users_emails(db_cursor, username, expected_email):
    db_cursor.execute(
        "SELECT * FROM users WHERE username = %s;",
        (username,)
    )
    row = db_cursor.fetchone()
    assert row is not None
    assert row[2] == expected_email

def test_create_user(db_connection):
    cursor = db_connection.cursor()
    username = "db_test_user"
    email = "db_test@test.com"
    age = 25

    try:
        cursor.execute(
            "INSERT INTO users (username, email, age) VALUES (%s, %s, %s);",
            (username, email, age)
        )
        db_connection.commit()
        cursor.execute(
            "SELECT * FROM users WHERE username = %s;",
            (username,)
        )
        row = cursor.fetchone()
        assert row is not None
        assert row[2] == email
        assert row[3] == age

    finally:
        cursor.execute(
            "DELETE FROM users WHERE username = %s;",
            (username,)
        )
        db_connection.commit()

def test_update_user_age(db_connection):
    cursor = db_connection.cursor()
    username = "developer"
    old_age = 28
    new_age = 35
    try:
        cursor.execute(
            "UPDATE users SET age = %s WHERE username = %s;",
            (new_age, username)
        )
        assert cursor.rowcount == 1
        db_connection.commit()
        cursor.execute(
            "SELECT * FROM users WHERE username = %s;",
            (username,)
        )
        row = cursor.fetchone()
        assert row is not None
        assert row[3] == new_age

    finally:
        cursor.execute(
            "UPDATE users SET age = %s WHERE username = %s;",
            (old_age, username)
        )
        db_connection.commit()

def test_delete_user(db_connection):
    cursor = db_connection.cursor()
    username = "db_delete_user"
    email = "db_delete@test.com"
    age = 25
    try:
        cursor.execute(
            "INSERT INTO users (username, email, age) VALUES (%s, %s, %s);",
            (username, email, age)
        )
        db_connection.commit()
        cursor.execute(
            "DELETE FROM users WHERE username = %s;",
            (username,)
        )
        db_connection.commit()
        cursor.execute(
            "SELECT * FROM users WHERE username = %s;",
            (username,)
        )
        row = cursor.fetchone()
        assert row is None
    finally:
        cursor.execute(
            "DELETE FROM users WHERE username = %s;",
            (username,)
        )
        db_connection.commit()

def test_find_adult_users(db_connection):
    cursor = db_connection.cursor()
    age = 25
    username = "admin"
    cursor.execute(
        "SELECT * FROM users WHERE age > %s AND username != %s;",
        (age, username)
    )
    rows = cursor.fetchall()
    for user in rows:
        assert user[1] != username
        assert user[3] > age

def test_find_youngest_user(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM users ORDER BY age ASC LIMIT 1;")
    row = cursor.fetchone()
    assert row is not None
    cursor.execute("SELECT MIN(age) FROM users;")
    min_age = cursor.fetchone()[0]
    assert row[3] == min_age





