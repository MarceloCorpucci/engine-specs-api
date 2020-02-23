import pytest
from api.main import create_app
import logging


logging.basicConfig(level=logging.INFO)


def test_basic_creation():
    app = create_app(profile="testing")

    data = {
        'model': 'AP-1800',
        'displacement': 1781,
        'power': 112,
        'forced_induction': False
    }

    with app.test_client() as client:
        response = client.post('/api/engine', json=data)

        assert response.status_code == 201


def test_mandatory_fields():
    app = create_app(profile="testing")

    data = {
        'valve_amount': 8,
        'injectors': 'standard',
        'piston_type': 'cast',
        'camshaft': 'standard',
        'forced_induction_type': 'turbo',
        'forced_induction_model': 'K16',
        'fuel_type': 'gasoline'
    }

    with app.test_client() as client:
        response = client.post('/api/engine', json=data)

        assert response.status_code == 400
