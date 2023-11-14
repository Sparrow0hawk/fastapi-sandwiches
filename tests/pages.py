from __future__ import annotations

from bs4 import BeautifulSoup
from fastapi.testclient import TestClient


class HomePage:
    def __init__(self, client: TestClient):
        self._soup = BeautifulSoup()
        self._client = client

    def open_(self) -> HomePage:
        response = self._client.get("/")
        self._soup = BeautifulSoup(response.text, "html.parser")
        return self

    @property
    def table(self) -> list[tuple[str, int]]:
        rows = self._soup.select_one("main table")
        row_items = rows.select("tbody tr")
        return [tuple(row.stripped_strings) for row in row_items]
