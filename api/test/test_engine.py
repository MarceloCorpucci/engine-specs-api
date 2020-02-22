import pytest
from api.main import create_app
from api.model.engine_model import Engine
import logging


logging.basicConfig(level=logging.INFO)


def test_basic_engine_creation():
    app = create_app(profile="testing")

    data = {
        "model": "AP-1800",
        "displacement": 1781,
        "valve_amount": 8,
        "injectors": "standard",
        "piston_type": "cast",
        "camshaft": "standard",
        "power": 112,
        "forced_induction": False,
        "fuel_type": "gasoline"
    }

    with app.test_client() as client:
        response = client.post('/api/engine', json=data)

        assert response.status_code == 201
