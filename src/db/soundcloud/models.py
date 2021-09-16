from flask_sqlalchemy import SQLAlchemy, orm
import validators


db = SQLAlchemy()


class SoundCloudUser(db.Model):

    __tablename__ = 'soundclouduser'

    id = db.Column(db.BigInteger, primary_key=True)
    alias = db.Column(db.Text, nullable=True)
    name = db.Column(db.Text)
    country = db.Column(db.Text)
    web_profiles = db.relationship('WebProfile',
                                   backref='soundcloud_user',
                                   lazy='dynamic'
                                   )


class WebProfile(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    url = db.Column(db.Text)
    network = db.Column(db.Text, nullable=True)
    title = db.Column(db.Text, nullable=True)
    username = db.Column(db.Text, nullable=True)
    sound_cloud_user_id = db.Column(db.BigInteger, db.ForeignKey('soundclouduser.id'))

    @orm.validates('url')
    def validate_url(self, key, url):
        if not validators.url(url):
            raise AssertionError('not valid url')
        return url


