import pytest
from api.main import create_app


def test_basic_preset_creation():
    app = create_app(profile='testing')

    with app.test_client() as client:
        response = client.post('/api/warning_preset', json={
            'ect_warning': 95,
            'oil_temp_warning': 109,
            'rpm_warning': 8000,
            'engine': [{
                'model': 'Z24XE',
                'displacement': 2405,
                'power': 138,
                'forced_induction': False
            }]
        })

        assert response.status_code == 201
