from fastapi.testclient import TestClient

from tests.pages import HomePage


def test_home(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "<h1>Big Sandwiches Sandwich Shop</h1>" in response.text


def test_home_shows_table(client: TestClient) -> None:
    home_page = HomePage(client).open_()
    assert home_page.table == [("Marmite and Cheese", "10")]
