# from api.main import ma
from flask_marshmallow import Marshmallow


ma = Marshmallow()


class EngineSchema(ma.Schema):
    class Meta:
        fields = ("model", "displacement", "_links")

    _links = ma.Hyperlinks(
         {"self": ma.URLFor("engine_detail", id="<reg_id>"), "collection": ma.URLFor("engines")}
    )


engine_schema = EngineSchema()
engines_schema = EngineSchema(many=True)
