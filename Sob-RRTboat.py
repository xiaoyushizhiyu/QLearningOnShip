import pyglet, random, math, copy
#from games import boat, canav1
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
    global j, path
    game_window.clear()
    # print("2")
    #canav_c = canav1.canav()
    canav_c = canav2.canav()
    boat_ship.draw()
    # car_ship.draw()
    if j != 0:
        glBegin(GL_LINE_STRIP)
        gl.glColor4f(0.9, 0.1, 0.1, 1.0)
        for x, y in path:
            glVertex2f(x, y)
        glEnd()

class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None

class RRT(object):
    def __init__(self, start, goal, rand_area):
        self.start = Node(start[0], start[1])
        self.end = Node(goal[0], goal[1])
        self.x_rand = rand_area[0]
        self.y_rand = rand_area[1]
        self.expandDis = 20.0
        self.goalSampleRate = 0.05  # 选择终点的概率是0.05
        self.maxIter = 500
        self.nodeList = [self.start]


    def random_node(self):
        node_x = random.uniform(0, self.x_rand)
        node_y = random.uniform(0, self.y_rand)
        node = [node_x, node_y]
        return node

    def get_nearest_list_index(self, node_list, rnd):
        d_list = [(node.x - rnd[0]) ** 2 + (node.y - rnd[1]) ** 2 for node in node_list]
        min_index = d_list.index(min(d_list))
        return min_index

    def collision_check(self, new_node):
        if (new_node.x-boat_ship.width/2) < 200 or (new_node.x-boat_ship.height/2) > 600:
            return False

        #if 400 < (new_node.x+boat_ship.width/2) < 520 and 100 < (new_node.y+boat_ship.height/2) < 170:
            #return False

        if 300 < (new_node.x+boat_ship.width/2) < 420 and 200 < (new_node.y+boat_ship.height/2) < 270:
            return False

        if 400 < (new_node.x+boat_ship.width/2) < 520 and 450 < (new_node.y+boat_ship.height/2) < 520:
            #print(x,y)
            return False

        if 350 < (new_node.x+boat_ship.width/2) < 470 and 325 < (new_node.y+boat_ship.height/2) < 395:
            # print(x,y)
            return False

        if 400 < (new_node.x+boat_ship.width/2) < 520 and 100 < (new_node.y+boat_ship.height/2) < 170:
            # print(x,y)
            return False

        return True  # safe

    def planning(self):
        global path
        while True:
            if random.random() > self.goalSampleRate:
                rnd = self.random_node()
            else:
                rnd = [self.end.x, self.end.y]

            min_index = self.get_nearest_list_index(self.nodeList, rnd)
            nearest_node = self.nodeList[min_index]
            theta = math.atan2(rnd[1] - nearest_node.y, rnd[0] - nearest_node.x)
            new_node = copy.deepcopy(nearest_node)
            new_node.x += self.expandDis * math.cos(theta)
            new_node.y += self.expandDis * math.sin(theta)
            new_node.parent = min_index
            if not self.collision_check(new_node):
                continue

            self.nodeList.append(new_node)
            dx = new_node.x - self.end.x

            dy = new_node.y - self.end.y
            d = math.sqrt(dx * dx + dy * dy)

            if d <= self.expandDis:
                print("Goal!!")
                break

        path = [[self.end.x, self.end.y]]
        last_index = len(self.nodeList) - 1
        while self.nodeList[last_index].parent is not None:
             node = self.nodeList[last_index]
             path.append([node.x, node.y])
             last_index = node.parent
        path.append([self.start.x, self.start.y])
        return path


def main(dt):
    global path
    pyglet.clock.unschedule(main)
    rrt = RRT(start=[400, 30], goal=[400, 550], rand_area=[800, 600])
    path = rrt.planning()
    print(path)

def paint(dt):
    global path, j
    # pyglet.clock.unschedule(paint)
    # print(1)
    i = len(path)
    j += 1
    if (i - j) > 0:
        x, y = path[i - j]
        x1, y1 = path[i - j - 1]
        angel = math.atan2(y1 - y, x1 - x)
        angel = angel * 180/math.pi
        angel = 90 - angel
        boat_ship.rotation = angel
        boat_ship.x, boat_ship.y = x, y

if __name__ == "__main__":
    # pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.clock.schedule_interval(main, 0.1)
    pyglet.clock.schedule_interval(paint, 0.2)
    pyglet.app.run()
    # qfunc = qlearning()