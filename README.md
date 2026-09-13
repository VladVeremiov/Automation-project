# Automation Project

My QA automation project for practicing Python, pytest and test automation.

Currently the project includes API testing and Playwright-based UI automation.

## Tech Stack

* Python
* pytest
* requests
* Playwright
* pytest-playwright
* python-dotenv
* Docker
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

## UI Tests

Authentication:

* User registration
* User login
* Redirect to dashboard after successful authentication

Tasks:

* Create a new task
* Edit an existing task
* Change task priority
* Verify edited task data
* Delete a task

## Running tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests locally:

```bash
pytest
```

Run API tests:

```bash
pytest tests/api
```

## Docker

The project can also be run inside a Docker container.

Build the Docker image:

```bash
docker build -t automation-project .
```

Run all tests inside the container:

```bash
docker run --rm automation-project pytest
```

The Docker image includes Python dependencies and Chromium required for Playwright UI tests.

## CI

Tests are also running through GitHub Actions.

## Project status

The project is still in development.
