import pytest
from hamcrest import *
from api.model.warning_preset_model import preset_name, ValidationError


def test_warning_preset_name_validation():
	with pytest.raises(ValidationError) as e:
		preset_name('Preset1 NOTYPE')

	exception_message = str(e.value)

	assert_that(exception_message, equal_to('Preset name is not including a type'))
