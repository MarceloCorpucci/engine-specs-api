from api.app import ma


class EngineSchema(ma.Schema):
    class Meta:
        fields = ("model", "displacement", "_links")

    _links = ma.Hyperlinks(
         {"self": ma.URLFor("engine_detail", id="<id>"), "collection": ma.URLFor("engines")}
    )


engine_schema = EngineSchema()
engines_schema = EngineSchema(many=True)
