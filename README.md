# Automation Project

My QA automation project for practicing Python and pytest.

Currently I'm mainly working with API testing using `requests` and pytest.

## Tech Stack

* Python
* pytest
* requests
* Git / GitHub
* GitHub Actions

## API Tests

### Auth

* Registration
* Login
* Bearer token authentication
* Current user
* Positive and negative scenarios
* Parametrized tests
* Response validation

### Tasks

* Create task
* Get all tasks
* Get task by ID
* Update task
* Delete task
* Update task status
* API chaining

## Running tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

Run API tests:

```bash
pytest tests/api
```

## CI

Tests are also running through GitHub Actions.

## Project status

The project is still in development. I'm gradually adding new tests and automation features while learning QA automation with Python.
