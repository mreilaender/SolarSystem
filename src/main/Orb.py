from abc import *

import pyglet
from pyglet.gl.gl import *
from pyglet.gl.glu import *
__author__ = 'mreilaener'


class Orb:
    __metaclass__ = ABCMeta

    def __init__(self, name, radius, surface=False, year_scale=1, day_scale=1, rotation_cw=True):

        self.pos_x, self.pos_y, self.pos_z = 0, 0, 0
        self.cur_rotation_angle_year = 0
        self.cur_rotation_angle = 0

        self.system_center = None
        self.system = []

        self.name = name
        self.radius = radius

        self.surface = surface

        self.year_scale = year_scale
        self.day_scale = day_scale
        self.rotation_cw = rotation_cw

        self.sphere = gluNewQuadric()
        gluQuadricNormals(self.sphere, GLU_SMOOTH)
        gluQuadricTexture(self.sphere, GL_TRUE)

    def add_orb(self, orb):

        if isinstance(orb, Orb):
            self.system.append(orb)
        else:
            raise Exception

    def set_system_center(self, orb):
        if isinstance(orb, Orb):
            self.system_center = orb
        else:
            raise Exception

    def update(self, time):

        self.cur_rotation_angle += self.day_scale
        self.cur_rotation_angle_year += self.year_scale

        for orb in self.system:
            orb.update(time)

    def draw(self):
        # TODO alle Parameter auf attribute beziehen z.B. bei rotate
        # Reihenfolge: Erst wird rotiert DANN transliert, dann wieder rotiert
        # das was ganz unten steht wird als erstes ausgefuehrt

        # yearscale
        glRotatef(self.cur_rotation_angle_year, 0, 1, 0)
        glTranslatef(self.pos_x, self.pos_y, self.pos_z)

        # dayscale
        glRotatef(self.cur_rotation_angle, 0, 1, 0)

        # Textures
        # TODO
        if self.surface is False:
            gluSphere(self.sphere, self.radius, 64, 64)
        else:
            self.surface.draw()
            gluSphere(self.sphere, self.radius, 64, 64)
            glDisable(self.surface.texture.target)

        for orb in self.system:
            orb.draw()


class Planet(Orb):

    def __init__(self, name, radius, surface, year_scale=1, day_scale=1, rotation_cw_=True):
        super(Planet, self).__init__(name, radius, surface, year_scale, day_scale, rotation_cw_)


class Star(Orb):

    def __init__(self, name, radius, year_scale=1, day_scale=1, rotation_cw=True, light_strength=1):
        super(Star, self).__init__(name, radius, year_scale, day_scale, rotation_cw)
        self.__light_strength = light_strength


class Surface(object):
    def __init__(self, texture_path=None):
        self.texture_path = texture_path
        self.image = pyglet.resource.image(self.texture_path)
        self.texture = self.image.texture
        self._verify('width')
        self._verify('height')

    def draw(self):
        glEnable(self.texture.target)
        glBindTexture(self.texture.target, self.texture.id)

    def _verify(self, dimension):
        """
        Verifies the size of the texture. Texture needs to be to the power of 2

        :param dimension: Which dimension to check (width, height)
        :type dimension: str
        :raise Exception: Image is not a power of two
        """
        value = self.texture.__getattribute__(dimension)
        while value > 1:
            div_float = float(value) / 2.0
            div_int = int(div_float)
            if not (div_float == div_int):
                raise Exception('image %s is %d, which is not a power of 2' % (
                    dimension, self.texture.__getattribute__(dimension)))
            value = div_int
