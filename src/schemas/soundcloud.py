from marshmallow import Schema, fields


class SoundCloudSchema(Schema):
    query = fields.Str(required=True)
