from pyglet.window import key


class KeyControls(object):

    def __init__(self, window, camera):
        self.camera = camera
        self.window = window
        self.keys = key.KeyStateHandler()

        self.stopped = False

        self.window.push_handlers(self.keys, self.on_key_press, self.on_mouse_motion)

    def on_key_release(self, symbol, modifiers):
        """
        Gets called on key release

        :param symbol: Key which has been pressed
        :param modifiers: ?
        """
        self.keys[symbol] = False

    def on_key_press(self, symbol, modifiers):
        """
        Key press handler

        :param symbol: actual pressed symbol
        :param modifiers: ?
        """
        self.keys[symbol] = True

        # Pause
        if symbol == key.P:
            self.stopped = not self.stopped
        # Close Window on ESC
        if symbol == key.ESCAPE:
            self.window.close()

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Mouse movement/motion handler

        :param x: mouse x-Coordinate
        :param y: mouse y-Coordinate
        :param dx: Changed x-Coordinate since last call of mouse_motion
        :param dy: Changed y-Coordinate since last call of mouse_motion
        """
        print("dx: %s, dy: %s" % (dx, dy))
        if dx != 0:
            # self.camera.reset()
            self.camera.rotatey = 1
            self.camera.angle += dx
            self.camera.rotatey = 0
        if dy != 0:
            # self.camera.reset()
            self.camera.rotatex = 1
            self.camera.angle -= dy
            self.camera.rotatex = 0
        if dx != 0 and dy != 0:
            pass

    def camera_update(self, dt):
        """
        Updating the camera position

        :param dt:
        :return:
        """
        # Implementing minecraft like camera movement
        # TODO Factor value oriented on mouse sensitivity
        factor = 0.4
        if self.keys[key.W]:
            self.camera.move_forward(factor)
        if self.keys[key.A]:
            self.camera.move_left(factor)
        if self.keys[key.S]:
            self.camera.move_backward(factor)
        if self.keys[key.D]:
            self.camera.move_right(factor)
        if self.keys[key.SPACE]:
            self.camera.move_up(factor)
        if self.keys[key.LCTRL]:
            self.camera.move_down(factor)
