import pyglet
from pyglet.gl.glu import *
from pyglet.gl.gl import *
from pyglet.window import key

from src.main.Camera import Camera
from src.main.Orb import Planet
from src.main.KeyHoldHandler import KeyHoldHandler

from _thread import start_new_thread

__author__ = 'mreilaender'

# Window
window = pyglet.window.Window(resizable=False, fullscreen=False)


def init():
    # Initialize planets
    pass


@window.event
def on_draw():
    window.clear()

    # draw_lines()
    glLoadIdentity()

    # 3r Projektion einstellen
    glEnable(GL_DEPTH_TEST)
    # Kamera auf Fenstergroesse einstellen
    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, window.width, window.height)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glLoadIdentity()

    # Lege Perspektive fest
    gluPerspective(45, (window.width/window.height), 1, 100)

    # Lade ModelView Matrix
    glMatrixMode(GL_MODELVIEW)

    for planet in orbs:
        glLoadIdentity()
        camera.draw()
        orbs[planet].draw()


@window.event
def on_mouse_motion(x, y, dx, dy):
    # camera.reset()
    if dx != 0:
        pass
    if dy != 0:
        pass
    if dx != 0 and dy != 0:
        pass
    # camera.rotatey = 1
    # camera.angle += dx
    # print("%s %s %s" % (camera.rotatex, camera.rotatey, camera.rotatez))


@window.event
def on_key_press(symbol, mod):
    KeyHoldHandler(keyboard, camera).start()
    if symbol == key.SPACE:
        global stop
        stop = not stop


def update(time):
    """
    Update Method - hier wird nur berechnet nicht gezeichnet, bzw die update Methoden der Planeten aufgerufen
    :param time: Time which has past during the last call of this method. Pyglet calculates this automatically
    :return:
    """
    # TODO evtl Liste aller Planeten -> dann muss man nurmehr mit einer for durchgehen und die update Methode aufrufen
    # print("Time: %s" % time)
    if not stop:
        for planet in orbs:
            orbs[planet].update(time)
    # print("x: %s y: %s z: %s" % (planet2.pos_x, planet2.pos_y, planet2.pos_z))


def draw_lines():
    # TODO Transparenter machen mit glColor4ui
    glLoadIdentity()
    # Rote Achse -- X-Achse
    glLineWidth(2.5)
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(100, 0, 0)
    glEnd()

    glLoadIdentity()
    # Gruene Achse -- Y-Achse
    glLineWidth(2.5)
    glColor3f(1, 1, 0)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 100, 0)
    glEnd()

    glLoadIdentity()
    # Weisse Achse -- Z-Achse
    glLineWidth(2.5)
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 100)
    glEnd()


def set_speed(speed):
    pass


def accelerate():
    # which parameters?
    pass


def deccelerate():
    pass


def show_textures(show=True):
    pass


def pause(pause=True):
    pass


window.set_size(1200, 800)
window.set_mouse_visible(False)

# stateHandler
keyboard = key.KeyStateHandler()
window.push_handlers(keyboard)

# Initialize camera
camera = Camera()
camera.x = 10
camera.y = 10
camera.z = 50

# Initialize planets
# gluNewQuadrtic ist die standard textur
q = gluNewQuadric()

planet1 = Planet("Test Planet", 3, q, day_scale=0)
planet2 = Planet("Test Planet2", 1, q, day_scale=2, year_scale=2)
planet3 = Planet("Test Planet3", 1, q, year_scale=0.5, day_scale=1)

mond2 = Planet("Mond", 0.5, q, year_scale=1)
mond2.pos_x = 5
planet2.add_orb(mond2)
stop = True

orbs = {
    "planet1": planet1,
    "planet2": planet2,
    "planet3": planet3
}

# Planet2
orbs["planet2"].pos_x = 10

# Planet3
orbs["planet3"].pos_x = 20

# Setting update method
pyglet.clock.schedule(update)
pyglet.app.run()
