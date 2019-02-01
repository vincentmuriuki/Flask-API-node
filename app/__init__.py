
# libraies
from flask import Blueprint, Flask
# local
from instance.config import config_settings
from .api.v2.db.conn import init_db

def create_app():
    app = Flask(__name__)
    init_db()

    from .api.v1 import version1 as v1
    app.register_blueprint(v1)

    from .api.v2 import version2 as v2
    app.register_blueprint(v2)

    return app
    