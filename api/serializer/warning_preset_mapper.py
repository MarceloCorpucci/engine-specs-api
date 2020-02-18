from kim import Mapper, field
from api.model.warning_preset_model import WarningPreset
from api.serializer.engine_mapper import EngineMapper
from bson import ObjectId


class WarningPresetMapper(Mapper):
    __type__ = WarningPreset()
    id = ObjectId()
    ect_warning = field.Integer()
    oil_temp_warning = field.Integer()
    rpm_warning = field.Integer()
    engine = field.Nested(EngineMapper, read_only=True)
