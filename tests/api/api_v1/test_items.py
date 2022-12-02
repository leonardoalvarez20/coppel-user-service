from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from tests.utils.item import create_random_item


def test_create_item(client: TestClient, db: Session) -> None:
    """Test API POST items/ endpoint"""
    data = {"title": "Foo", "description": "Bar"}
    response = client.post(
        "/api/v1/items/",
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert "id" in content


def test_read_item(client: TestClient, db: Session) -> None:
    """Test API GET items/ endpoint"""
    item = create_random_item(db)
    response = client.get(
        f"/api/v1/items/{item.id}",
    )
    assert response.status_code == 200
    content = response.json()

    assert content["title"] == item.title
    assert content["description"] == item.description
    assert content["id"] == item.id
