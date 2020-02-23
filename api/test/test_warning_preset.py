import pytest
from api.main import create_app
from api.model.engine_model import Engine
from api.model.warning_preset_model import WarningPreset
import logging


logging.basicConfig(level=logging.INFO)


def test_basic_preset_creation():
    app = create_app(profile='testing')

    engine_to_save = Engine(model='AP-1800',
                            displacement=1781,
                            power=112,
                            forced_induction=False)

    engine_to_save.save()

    warn_preset_to_save = WarningPreset(ect_warning=95,
                                        oil_temp_warning=109,
                                        rpm_warning=6700)

    warn_preset_to_save.engine = engine_to_save
    warn_preset_to_save.save()

    json_data = warn_preset_to_save.to_json()
    logging.info(json_data)

    with app.test_client() as client:
        response = client.post('/api/warning_preset', json=json_data)

        assert response.status_code == 201
