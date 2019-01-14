import pyglet
from pyglet.gl import *

class canav():
    def __init__(self):
        glBegin(gl.GL_QUADS)
        gl.glColor4f(1, 0.6, 0.1, 1.0)
        glVertex2f(0, 0)
        glVertex2f(800, 0)
        glVertex2f(800, 600)
        glVertex2f(0, 600)
        gl.glColor4f(0.007, 0.79, 0.87, 1.0)
        glVertex2f(200, 0)
        glVertex2f(200, 600)
        glVertex2f(600, 600)
        glVertex2f(600, 0)
        gl.glColor4f(1, 0.6, 0.1, 1.0)
        # 第1个障碍
        glVertex2f(300, 200)
        glVertex2f(400, 200)
        glVertex2f(400, 250)
        glVertex2f(300, 250)
        # 第3个障碍
        glVertex2f(350, 325)
        glVertex2f(450, 325)
        glVertex2f(450, 375)
        glVertex2f(350, 375)
        # 第2个障碍
        glVertex2f(400, 450)
        glVertex2f(400, 500)
        glVertex2f(500, 500)
        glVertex2f(500, 450)
        #第四个障碍
        #glVertex2f(400, 100)
        #glVertex2f(500, 100)
        #glVertex2f(500, 150)
        #glVertex2f(400, 150)
        #禁航区
        # gl.glColor4f(0.63, 0.29, 0.99, 1.0)
        # glVertex2f(400, 100)
        # glVertex2f(450, 75)
        # glVertex2f(500, 100)
        # glVertex2f(450, 125)
        glEnd()