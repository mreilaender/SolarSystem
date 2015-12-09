from threading import Thread

from pyglet.window import key


class KeyHoldHandler(object):

    def __init__(self, key_state_handler, camera):
        # super().__init__()
        self.key_state_handler = key_state_handler
        self.camera = camera

    def pressing(self):
        factor = 0.00003
        while self.key_state_handler[key.W]:
            self.camera.z -= factor
        while self.key_state_handler[key.S]:
            self.camera.z += factor
        while self.key_state_handler[key.A]:
            self.camera.x -= factor
        while self.key_state_handler[key.D]:
            self.camera.x += factor

        while self.key_state_handler[key.UP]:
            self.camera.reset()
            self.camera.rotatex = 1
            self.camera.angle += factor
        while self.key_state_handler[key.DOWN]:
            self.camera.reset()
            self.camera.rotatex = 1
            self.camera.angle -= factor
        while self.key_state_handler[key.LEFT]:
            self.camera.reset()
            self.camera.rotatey = 1
            self.camera.angle += factor
        while self.key_state_handler[key.RIGHT]:
            self.camera.rotatey = 1
            self.camera.angle -= factor