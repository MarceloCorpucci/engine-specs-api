import pytest
from api.main import create_app


def test_basic_engine_creation():
    app = create_app(profile="testing")

    with app.test_client() as client:
        response = client.post('/api/engine', json={
            "model": "testD", "displacement": 1400
        })

        assert response.status_code == 201
