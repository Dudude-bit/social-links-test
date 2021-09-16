from flask import request
from flask_restful import fields, marshal_with, Resource, abort

from schemas.soundcloud import SoundCloudSchema
from service.utils import get_data_for_soundcloud_resource

web_profiles_fields = {
    'url': fields.String,
    'network': fields.String,
    'title': fields.String,
    'username': fields.String
}

soundcloud_fields = {
    'id': fields.Integer,
    'alias': fields.String,
    'name': fields.String,
    'country': fields.String,
    'web_profiles': fields.List(fields.Nested(web_profiles_fields))
}


class SoundCloudResource(Resource):

    @marshal_with(soundcloud_fields)
    def get(self):
        schema = SoundCloudSchema()
        errors = schema.validate(request.args)
        if errors:
            abort(400, errors=errors)
        data = get_data_for_soundcloud_resource(request.args['query'])
        if not data:
            abort(404, errors={'message': 'not-found'})
        return data
