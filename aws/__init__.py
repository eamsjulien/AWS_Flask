import os

from flask import Flask
from flask import render_template
from flask import Response

from aws.auth import login_required
from aws.camera import Camera


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'aws.sqlite'),
        FRAMES_NBR=1
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

    def gen(camera):
        while True:
            frame = camera.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    @app.route('/')
    @login_required
    def index():
        return render_template('detect/index.html')

    @app.route('/video_feed')
    def video_feed():
        return Response(gen(Camera(app.config['FRAMES_NBR'])),
                        mimetype='multipart/x-mixed-replace; boundary=frame')

    return app
