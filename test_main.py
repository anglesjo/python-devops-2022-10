from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API. Endpoints: /search or /wiki"}


def test_phrase_route():
    response = client.get("/phrase/Ragnarok")
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            "norse",
            "ragnarök",
            "norse",
            "ragnarǫk",
            "great battle",
            "numerous great figures",
            "odin",
            "thor",
            "týr",
            "freyr",
            "heimdallr",
            "loki",
            "natural disasters",
        ]
    }
