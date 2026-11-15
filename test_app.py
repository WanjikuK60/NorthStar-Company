from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_index_serves_the_test_page():
    response = client.get("/")
    assert response.status_code == 200
    assert "Webhook Chat Widget" in response.text


def test_webhook_echoes_the_event():
    response = client.post("/webhook", json={"event": "order.created", "message": "hello"})
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "received": {"event": "order.created", "message": "hello"},
    }


def test_message_is_optional():
    response = client.post("/webhook", json={"event": "ping"})
    assert response.json()["received"] == {"event": "ping", "message": ""}


def test_missing_event_is_rejected():
    assert client.post("/webhook", json={"message": "no event"}).status_code == 422


def test_empty_event_is_rejected():
    assert client.post("/webhook", json={"event": ""}).status_code == 422
