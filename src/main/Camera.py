from pyglet.gl import glTranslatef, glRotatef


class Camera(object):

    def update(self):
        pass

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.angle = 0
        self.rotatex = 0
        self.rotatey = 0
        self.rotatez = 0

    def draw(self):
        if self.rotatex != 0 or self.rotatey != 0 or self.rotatez != 0:
            glRotatef(self.angle, self.rotatex, self.rotatey, self.rotatez)
        glTranslatef(-self.x, -self.y, -self.z)

    def move_backward(self, factor):
        self.z += factor

    def move_forward(self, factor):
        self.z -= factor

    def move_right(self, factor):
        self.x += factor

    def move_left(self, factor):
        self.x -= factor

    def move_up(self, factor):
        self.y += factor

    def move_down(self, factor):
        self.y -= factor