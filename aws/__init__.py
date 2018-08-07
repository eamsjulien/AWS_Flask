import os
import json

from flask import Flask
from flask import render_template
from aws.auth import login_required


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'aws.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    @login_required
    def index():
        json_path = os.path.join(app.static_folder, 'json', 'current.json')
        with open(json_path) as f:
            data = json.load(f)
        count_nbr = data['count']
        return render_template('detect/index.html', nbr=count_nbr)

    return app
