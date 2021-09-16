from flask import Flask

from config import *
from db.soundcloud.models import db
from routes.soundcloud import soundcloud_bp

app = Flask(__name__)
app.register_blueprint(soundcloud_bp, url_prefix='/soundcloud')

if os.getenv('DEBUG', 'true') == 'true':
    config_object = TestConfig
else:
    config_object = ProductionConfig

app.config.from_object(config_object)

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
        # mock_soundcloud_user = SoundCloudUser(alias='123alias', name='123name', country='123country')
        # mock_web_profile = WebProfile(network='twitter', title='twitter', username='123', url='https://twitter.com/JuiceWorlddd')
        # mock_soundcloud_user.web_profiles.append(mock_web_profile)
        # db.session.add(mock_soundcloud_user)
        # db.session.commit()
    app.run('0.0.0.0', 5000)
