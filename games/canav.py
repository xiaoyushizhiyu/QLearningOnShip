import pyglet
from pyglet.gl import *

class canav():
    def __init__(self):
        glBegin(gl.GL_QUADS)
        gl.glColor4f(0.6, 0.3, 0.1, 1.0)
        glVertex2f(0, 0)
        glVertex2f(800, 0)
        glVertex2f(800, 600)
        glVertex2f(0, 600)
        gl.glColor4f(0.1, 0.1, 0.3, 1.0)
        glVertex2f(350, 0)
        glVertex2f(350, 600)
        glVertex2f(450, 600)
        glVertex2f(450, 0)
        glVertex2f(450, 350)
        glVertex2f(800, 350)
        glVertex2f(800, 250)
        glVertex2f(450, 250)     
        glEnd()    