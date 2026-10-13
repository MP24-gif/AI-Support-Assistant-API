from fastapi.testclient import TestClient
from app.main import app
import app.main as main_module

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_support_success(monkeypatch):
    def fake_ask_model(question):
        return "Restart your laptop and check the connection."

    monkeypatch.setattr(main_module, "ask_model", fake_ask_model)

    response = client.post(
        "/support",
        json={"question": "My laptop cannot connect to Wi-Fi"}
    )

    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "Restart your laptop" in response.json()["answer"]


def test_support_rejects_short_question():
    response = client.post(
        "/support",
        json={"question": "Help"}
    )

    assert response.status_code == 422


def test_support_handles_unexpected_error(monkeypatch):
    def fake_ask_model(question):
        raise RuntimeError("Simulated internal failure")

    monkeypatch.setattr(main_module, "ask_model", fake_ask_model)

    response = client.post(
        "/support",
        json={"question": "My laptop cannot connect to Wi-Fi"}
    )

    assert response.status_code == 500
    assert response.json()["detail"] == "Unexpected server error."

def test_support_rejects_missing_question():
    response = client.post(
        "/support",
        json={}
    )

    assert response.status_code == 422


def test_support_rejects_question_over_1000_characters():
    response = client.post(
        "/support",
        json={"question": "a" * 1001}
    )

    assert response.status_code == 422