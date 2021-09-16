import flask
from flask_restful import Api

from resources.soundcloud import SoundCloudResource

soundcloud_bp = flask.Blueprint('soundcloud', __name__)

soundcloud_api = Api(soundcloud_bp)

soundcloud_api.add_resource(SoundCloudResource, '/users')