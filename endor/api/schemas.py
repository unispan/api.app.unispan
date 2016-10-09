import colander


class Role(colander.MappingSchema):
    name = colander.SchemaNode(
        colander.String(),
        validator=colander.Length(min=4, max=60),
    )
    # enabled = colander.SchemaNode(colander.Boolean())
