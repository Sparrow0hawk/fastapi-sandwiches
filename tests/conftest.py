import pytest
from fastapi.testclient import TestClient

from fastapi_sandwiches.main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
