import pytest
from fastapi.testclient import TestClient

from fastapi_sandwiches.main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


def test_home(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "<h1>Big Sandwiches Sandwich Shop</h1>" in response.text
