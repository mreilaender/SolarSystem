from pyglet.gl import gluLookAt


class CameraLookAt(object):

    def __init__(self):
        self.eyex , self.eyey, self.eyez = 0, 0, 50
        self.centerx, self.centery, self.centerz = 0, 0, 0
        self.upx, self.upy, self.upz = 0, 1, 0

    def draw(self):
        gluLookAt(
            self.eyex,    self.eyey,    self.eyez,
            self.centerx, self.centery, self.centerz,
            self.upx,     self.upy,     self.upz
        )

    def move_backward(self, factor):
        self.eyez += factor
        self.centerz += factor

    def move_forward(self, factor):
        self.eyez -= factor
        self.centerz -= factor

    def move_right(self, factor):
        self.eyex += factor
        self.centerx += factor

    def move_left(self, factor):
        self.eyex -= factor
        self.centerx -= factor

    def move_up(self, factor):
        self.eyey += factor
        self.centery += factor

    def move_down(self, factor):
        self.eyey -= factor
        self.centery -= factor

    def look_vertical(self, factor):
        self.centery += factor

    def look_horizontal(self, factor):
        self.centerx += factor
    """
    def look_down(self, factor):
        self.centery -= factor

    def look_up(self, factor):
        self.centery += factor

    def look_right(self, factor):
        self.centerx += factor

    def look_left(self, factor):
        self.centerx -= factor
    """