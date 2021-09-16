from db.soundcloud.models import SoundCloudUser


def get_data_for_soundcloud_resource(query):
    try:
        id_param = int(query)
    except ValueError:
        id_param = None
    person = SoundCloudUser.query.filter((SoundCloudUser.id == id_param) | (SoundCloudUser.alias == query)).first()
    return person
