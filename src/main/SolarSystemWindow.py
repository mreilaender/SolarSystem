from pyglet.window import Window, pyglet
from pyglet.gl.gl import *
from pyglet.gl.glu import gluPerspective, gluNewQuadric
from src.main.Camera import Camera
from pyglet.window import key

from src.main.KeyHoldHandler import KeyHoldHandler
from src.main.Orb import Planet


class SolarSystemWindow(Window):

    def __init__(self):
        super().__init__()
        self.keyboard = key.KeyStateHandler()
        self.push_handlers(self.keyboard)

        self.set_mouse_visible(False)

        self.camera = Camera()
        self.camera.x = 10
        self.camera.y = 10
        self.camera.z = 50

        self.orbs = {}
        # Initialize planets
        # gluNewQuadrtic ist die standard textur
        q = gluNewQuadric()

        planet1 = Planet("Test Planet", 3, q, day_scale=0)
        planet2 = Planet("Test Planet2", 1, q, day_scale=2, year_scale=2)
        planet3 = Planet("Test Planet3", 1, q, year_scale=0.5, day_scale=1)

        mond2 = Planet("Mond", 0.5, q, year_scale=1)
        test2 = Planet("test2", 0.1, q, year_scale=0.3)
        test2.pos_x = 7
        mond2.pos_x = 5
        mond2.add_orb(test2)
        planet2.add_orb(mond2)

        self.orbs["planet1"] = planet1
        self.orbs["planet2"] = planet2
        self.orbs["planet3"] = planet3

        self.stop = True

        # Planet2
        self.orbs["planet2"].pos_x = 10

        # Planet3
        self.orbs["planet3"].pos_x = 20

    def on_draw(self):
        self.clear()

        # draw_lines()
        glLoadIdentity()

        # 3r Projektion einstellen
        glEnable(GL_DEPTH_TEST)
        # Kamera auf Fenstergroesse einstellen
        glMatrixMode(GL_PROJECTION)
        glViewport(0, 0, self.width, self.height)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glLoadIdentity()

        # Lege Perspektive fest
        gluPerspective(45, (self.width/self.height), 1, 100)

        # Lade ModelView Matrix
        glMatrixMode(GL_MODELVIEW)

        for planet in self.orbs:
            glLoadIdentity()
            self.camera.draw()
            self.orbs[planet].draw()

    def update(self, time):
        """
        Update Method - hier wird nur berechnet nicht gezeichnet, bzw die update Methoden der Planeten aufgerufen

        :param time: Time which has past during the last call of this method. Pyglet calculates this automatically
        :return:
        """
        if not self.stop:
            for planet in self.orbs:
                self.orbs[planet].update(time)

    def on_mouse_motion(self, x, y, dx, dy):
        if dx != 0:
            self.camera.reset()
            self.camera.rotatey = 1
            self.camera.angle += dx
        if dy != 0:
            self.camera.reset()
            self.camera.rotatex = 1
            self.camera.angle -= dy
        if dx != 0 and dy != 0:
            pass

    def on_key_press(self, symbol, modifiers):
        KeyHoldHandler(self.keyboard, self.camera).start()
        if symbol == key.SPACE:
            self.stop = not self.stop
        if symbol == key.ESCAPE:
            self.close()

window = SolarSystemWindow()
pyglet.clock.schedule(window.update)
pyglet.app.run()
