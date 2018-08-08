from time import time
import os

FRAME_BASE = os.join.path(os.environ['AWS_FLASK_FOLDER'],
                          'aws/static/client_img/',
                          'frame')


class Camera(object):
    def __init__(self, frames_nbr):
        self.frames_nbr = frames_nbr
        self.frames = [open(FRAME_BASE + str(f) + '.jpg', 'rb').read()
                       for f in range(self.frames_nbr)]

    def get_frame(self):
        return self.frames[int(time()) % self.frames_nbr]
