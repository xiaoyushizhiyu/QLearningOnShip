import pyglet, random, math, time
from games import boat, canav2
from pyglet.gl import *

game_window = pyglet.window.Window(800, 600)
# main_batch = pyglet.graphics.Batch()
boat_ship = boat.Player(x=400, y=30)
game_window.push_handlers(boat_ship.key_handler)
path = []
j = 0

@game_window.event
def on_draw():
    global j
    game_window.clear()
    # print("2")
    canav_c = canav2.canav()
    boat_ship.draw()
    # car_ship.draw()
    if j != 0:
        glBegin(GL_LINE_STRIP)
        gl.glColor4f(0.9, 0.1, 0.1, 1.0)
        for x, y in path:
            glVertex2f(x, y)
        glEnd()

def find_path(dt):
    global path
    pyglet.clock.unschedule(find_path)
    s_x, s_y = 400, 30
    e_x, e_y = 400, 550
    astar = A_star(s_x, s_y, e_x, e_y)
    astar.find_path()
    path = astar.path
    print(path)
    #for i, j in path:
       # boat_ship.x, boat_ship.y = i, j

class point:
    def __init__(self, parent, x, y, gcost):
        self.parent = parent
        self.x = x
        self.y = y
        self.gcost = gcost

class A_star:
    def __init__(self, s_x, s_y, e_x, e_y):
        self.s_x = s_x
        self.s_y = s_y
        self.e_x = e_x
        self.e_y = e_y
        self.open = []
        self.close = []
        self.path = []

    def find_path(self):
        s = point(None, self.s_x, self.s_y, 0.0)
        while True:
            self.extend(s)
            if not self.open:
                return

            id, s = self.getbest()
            if self.is_target(s):
                self.makepath(s)
                return

            self.close.append(s)
            del self.open[id]


    def extend(self, s):
        xn = (0, -10, 10, 0)
        yn = (10, 0, 0, -10)
        for x, y in zip(xn, yn):
            newx, newy = x + s.x, y + s.y
            if self.is_valid(newx, newy):
                continue

            s1 = point(s, newx, newy, s.gcost + self.getcost(s.x, s.y, newx, newy))
            if self.is_close(s1):
                continue

            i = self.is_open(s1)
            if i != -1:
                if self.open[i].gcost > s1.gcost:
                    self.open[i].parent = s
                    self.open[i].gcost = s1.gcost
                continue

            self.open.append(s1)

    def is_valid(self, x, y):
        if (x-boat_ship.width/2) < 200 or (y+boat_ship.height/2) > 600:
            return True

        if 270 < (x+boat_ship.width/2) < 430 and 150 < (y-boat_ship.height/2) < 200:
            #print(x,y)
            return True

        if 320 < (x+boat_ship.width/2) < 480 and 275 < (y-boat_ship.height/2) < 325:
            #print(x,y)
            return True

        if 370 < (x + boat_ship.width / 2) < 530 and 400 < (y - boat_ship.height / 2) < 450:
            # print(x,y)
            return True

        if 300 < (x+boat_ship.width/2) < 430 and 140 < (y-boat_ship.height/2) < 190:
            #print(x,y)
             return True

         if 350 < (x + boat_ship.width / 2) < 480 and 265 < (y - boat_ship.height / 2) < 315:
            print(x,y)
            # return True

        if 410 < (x + boat_ship.width / 2) < 530 and 390 < (y - boat_ship.height / 2) < 440:
        #if 400 < (x + boat_ship.width / 2) < 480 and 390 < (y - boat_ship.height / 2) < 440:
            # print(x,y)
            return True

        # if 400 < (x + boat_ship.width / 2) < 500 and 50 < (y - boat_ship.height / 2) < 100:
            # print(x,y)
            # return True

    def is_close(self, s):
        for i in self.close:
            if s.x == i.x and s.y == i.y:
                return True
        return False

    def getcost(self, x, y, x1, y1):
        return 10

    def is_open(self, s):
        for i, n in enumerate(self.open):
            if s.x == n.x and s.y == n.y:
                return i
        return -1

    def getbest(self):
        best = None
        bv = 10000000
        bi = -1
        for id, i in enumerate(self.open):
            value = self.getfcost(i)
            if value < bv:
                best = i
                bv = value
                bi = id
        return bi, best

    def getfcost(self, i):
        return i.gcost + math.sqrt((self.e_x - i.x) * (self.e_x - i.x) + (self.e_y - i.y) * (self.e_y - i.y)) * 1.2

    def is_target(self, s):
        return s.x == self.e_x and s.y == self.e_y

    def makepath(self, s):
        while s:
            self.path.append((s.x, s.y))
            s = s.parent

def paint(dt):
    global path, j
    #pyglet.clock.unschedule(paint)
    #print(1)
    i = len(path)
    j += 1
    if (i-j)>= 0:
        x, y = path[i-j]
        if (x-boat_ship.x) ==10:
            boat_ship.rotation = 90

        if (y-boat_ship.y) ==10:
            boat_ship.rotation = 0

        boat_ship.x, boat_ship.y = x, y


if __name__ == "__main__":
    # pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.clock.schedule_interval(find_path, 0.1)
    pyglet.clock.schedule_interval(paint, 0.2)
    pyglet.app.run()
    # qfunc = qlearning()