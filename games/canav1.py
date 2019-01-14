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
        glVertex2f(200, 0)
        glVertex2f(200, 600)
        glVertex2f(600, 600)
        glVertex2f(600, 0)
        gl.glColor4f(0.6, 0.3, 0.1, 1.0)
        glVertex2f(300, 200)
        glVertex2f(400, 200)
        glVertex2f(400, 250)
        glVertex2f(300, 250)
        glVertex2f(400, 450)
        glVertex2f(400, 500)
        glVertex2f(500, 500)
        glVertex2f(500, 450)
        glEnd()