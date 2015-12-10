import pyglet
from pyglet.gl import *

from src.main.Camera import Camera
from src.main.KeyControls import KeyControls
from src.main.Orb import Surface, Planet

window = pyglet.window.Window()

window.set_size(1280, 720)
window.set_mouse_visible(False)

# Field of View
fov = 45
camera = Camera()
camera.x = 10
camera.y = 10
camera.z = 50

orbs = {}
# Initialize planets
# TODO Was wenn ich keine Textur haben will?
# Register directory, in which all resources are stored
pyglet.resource.path = ['resource/']
pyglet.resource.reindex()

# Initialize texture
texplanet = Surface("example.png")

# Initialize planets
center = Planet("Sun", 3, surface=texplanet, day_scale=0.5, year_scale=0)
planet2 = Planet("Test Planet2", 1, surface=False, day_scale=1, year_scale=1)

# Plantes over planets o.O
planet1_1 = Planet("Test Planet", 2, surface=False, day_scale=2, year_scale=2)
planet2_1 = Planet("Test Planet", 0.5, surface=False, day_scale=3, year_scale=2)

# Move planet2_1
planet2_1.pos_x = 3
planet2.add_orb(planet2_1)

orbs["center"] = center
orbs["planet2"] = planet2

# Planet options
# Move planets in x-direction
orbs["planet2"].pos_x = 10

controls = KeyControls(window, camera)


@window.event
def on_draw():
    global window, fov, orbs, camera
    window.clear()

    glLoadIdentity()

    # 3r Projektion einstellen
    glEnable(GL_DEPTH_TEST)
    # Kamera auf Fenstergroesse einstellen
    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, window.width, window.height)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glLoadIdentity()

    # Lege Perspektive fest
    # last parameter: view distance - distance before objects become invisible
    gluPerspective(fov, (window.width/window.height), 0.1, 8000.0)

    # Lade ModelView Matrix
    glMatrixMode(GL_MODELVIEW)

    for planet in orbs:
        glLoadIdentity()
        camera.draw()
        orbs[planet].draw()


def on_resize():
    # TODO evtl.
    pass


def update(dt):
    """
    In this method parameters, which are used in the draw method, are just modified. There is no drawing object in this method

    :param dt: Time which has past during the last call of this method. Pyglet calculates this automatically
    """
    # Updating camera
    global controls, orbs
    controls.camera_update(dt)
    if not controls.stopped:
        for planet in orbs:
            orbs[planet].update(dt)

# Setting method which will be called on an update of the frame
pyglet.clock.schedule(update)
pyglet.app.run()
