from flask import current_app

from settings_local import APPLICATION_ID, REST_API_KEY
from parse_rest.connection import register
from parse_rest.datatypes import Object

register(APPLICATION_ID, REST_API_KEY)


class User(Object):
    pass

user = User(email="today@email.com", password="testing")
