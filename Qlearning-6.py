import pyglet, random, math, time
from games import boat, canav2, resources
from pyglet.gl import *
import numpy as np
import sympy
# from sympy.abc import theta
import pygame
# 试试重新设置奖励函数

game_window = pyglet.window.Window(800, 600)
# main_batch = pyglet.graphics.Batch()
t = False
r = 1
s = []
p = 0
states = []
distance = 0
boat_ship = boat.Player(x=400, y=30)
#dia_land = pyglet.sprite.Sprite(img=resources.dia_image, x = 350, y = 250)
#tia_land = pyglet.sprite.Sprite(img=resources.tia_image, x = 450, y = 500)
#dia_land.scale = 0.5
#dia_land.rotation = 30
#tia_land.scale = 0.5
# car_ship = boat.Player(x=400, y=-300)
game_window.push_handlers(boat_ship.key_handler)
K = 0.08
T = 10.8


@game_window.event
def on_draw():
    global p, s
    game_window.clear()
    # print("2")
    canav_c = canav2.canav()
    boat_ship.draw()
    #dia_land.draw()
    #tia_land.draw()
    if p != 0:
        glBegin(GL_LINE_STRIP)
        gl.glColor4f(0.9, 0.1, 0.1, 1.0)
        for x, y, z in s:
            glVertex2f(x, y)
        glEnd()
    # car_ship.draw()


def reset():
    global t, r
    # 状态空间
    boat_ship.x, boat_ship.y, boat_ship.rotation = states[int(random.random() * len(states))]
    # boat_ship.rotation = 0
    t = True
    r = -1000


def step(action):
    global K, T
    #radians = 90 - boat_ship.rotation
    #angle_radians = math.radians(radians)
    #an = (K * action * (theta - T + T * sympy.exp(-theta / T))) * np.pi / 180
    i = 0
    while i < 20:
        ane1 = (K * action * (i - T + T * sympy.exp(-i / T)))
        ane2 = (K * action * ((i + 2) - T + T * sympy.exp(-(i + 2) / T)))
        #print(ane1, ane2)
        ane0 = (ane1 + ane2)/2
        #print(ane0)
        rolativeangel0 = boat_ship.rotation + ane0
        radians = 90 - rolativeangel0
        angle_radians = math.radians(radians)
        # 将角度转化为弧度
        #reangle = angle_radians + ane0
        force_x = math.cos(angle_radians) * 2
        force_y = math.sin(angle_radians) * 2
        # r_x = abs(force_x)
        boat_ship.x += force_x
        boat_ship.y += force_y
        i += 2

    #radians = 90 - boat_ship.rotation
    #angle_radians = math.radians(radians)
    #xn = sympy.cos(angle_radians + an) * 0.5
    #yn = sympy.sin(angle_radians + an) * 0.5
    #xnn = sympy.integrate(xn, (theta, 0, 20)).evalf()
    #ynn = sympy.integrate(yn, (theta, 0, 20)).evalf()
    bn = K * action * (20 - T + T * sympy.exp(-20 / T))
    boat_ship.rotation += bn
    rolativeangel1 = boat_ship.rotation
    #for t in tmeintervals:
        #print(t)
    #px = boat_ship.x + xnn
    #py = boat_ship.y + ynn
    #boat_ship.x, boat_ship.y = px, py
    print(boat_ship.x, boat_ship.y, boat_ship.rotation)
    # car_ship.draw()
    # time.sleep(1)
    #visualx = boat_ship.x - 350
    #visualy = boat_ship.y - 30
    while rolativeangel1 >= 180:
        rolativeangel1 -= 360

    while rolativeangel1 < -180:
        rolativeangel1 += 360
    return (boat_ship.x, boat_ship.y, rolativeangel1)


def greedy(actions, qfunc, x, y, z):
    #max = 0
   #key = "%d_%d_%d_%d" % (x, y, z, actions[0])
    #if key not in qfunc:
        #qfunc[key] = 0
    #qmax = qfunc[key]
    sa = []
    for i in range(len(actions)):
        key = "%d_%d_%d_%d" % (int(x/5)*5, int(y/5)*5, int(z/20)*20, actions[i])
        #if key not in qfunc:
            #qfunc[key] = 0
        sa.append(qfunc[key])

    amax = sa.index(max(sa))
        #q = qfunc[key]
        #if qmax < q:
            #qmax = q
            #amax = i
    print(actions[amax])
    return actions[amax]


def epsilon_greedy(actions, qfunc, x, y, z, epsilon):
    #amax = 0
    #key = "%d_%d_%d_%d" % (x, y, z, actions[0])
    # if key not in qfunc:
    # qfunc[key] = 0
    #qmax = qfunc[key]
    #for i in range(len(actions)):
        #key = "%d_%d_%d_%d" % (x, y, z, actions[i])
        # if key not in qfunc:
        # qfunc[key] = 0
        #q = qfunc[key]
        #if qmax < q:
            #qmax = q
            #amax = i
    sa = []
    for i in range(len(actions)):
        key = "%d_%d_%d_%d" % (int(x/5)*5, int(y/5)*5, int(z/20)*20, actions[i])
        #if key not in qfunc:
            #qfunc[key] = 0
        sa.append(qfunc[key])

    amax = sa.index(max(sa))
    if np.random.uniform() < 1 - epsilon:
        return actions[amax]
    else:
        return actions[int(random.random() * len(actions))]


    #pro = [0.0 for i in range(len(actions))]
    #pro[amax] += 1 - epsilon
    #for i in range(len(actions)):
        #pro[i] += epsilon / len(actions)

    #r = random.random()
    #s = 0.0
    #for i in range(len(actions)):
        #s += pro[i]
        #if s >= r:
            #return actions[i]
    #print(1)
    #return actions[len(actions) - 1]


def update(z):
    # pyglet.clock.unschedule(update)
    #print(boat_ship.x, boat_ship.y)
    global r, t, distance
    cz = False
    #boat_ship.update(dt)
    #boat_ship.contact()
    #z = boat_ship.rotation
    #while z >= 180:
        #z -= 360

    #while z < -180:
        #z += 360
    #r = boat_ship.y/10
    if z < 0:
        z = -1 * z

    elif z > 0:
        z = 360 - z

    dis = math.sqrt(np.square(boat_ship.x - 400) + np.square(boat_ship.y - 550))
    r = 1 - 0.003 * dis

    a = math.radians(z)
    w = boat_ship.width/2
    h = boat_ship.height/2
    ret = [(-w, h), (w, h), (-w, -h), (w, -h)]
    for w0, h0 in ret:
        x = boat_ship.x + w0
        y = boat_ship.y + h0
        x0 = (x - boat_ship.x) * math.cos(a) - (y - boat_ship.y) * math.sin(a) + boat_ship.x
        y0 = (x - boat_ship.x) * math.sin(a) + (y - boat_ship.y) * math.cos(a) + boat_ship.y
        #print(x0, y0)
        # 障碍1
        if 300 < x0 < 400 and 200 < y0 < 250:
            cz = True

        # 障碍2
        if 400 < x0 < 500 and 450 < y0 < 500:
            cz = True

        if x0 < 200 or x0 >600 or y0 < 0 or y0 > 600:
            cz = True

            # 障碍3
        if 350 < x0 < 450 and 325 < y0 < 375:
             cz = True

            # 障碍4
        #if 400 < x0 < 500 and 100 < y0 < 150:
            #cz = True

        # 禁航区
        # if 400 < x0 < 500 and 75 < y0 < 125:
            # cz = True
    #if (boat_ship.x + boat_ship.con) < 450 and boat_ship.rotation > 150:
        #reset()
    if cz:
        reset()



    #if boat_ship.y == 550 and boat_ship.x == 400:
    if boat_ship.y > 550 and 400 < boat_ship.x < 450:
        r = 1000
        t = True
        boat_ship.x, boat_ship.y, boat_ship.rotation = states[int(random.random() * len(states))]
        # r = r - 0.3 * distance

        #for i in range(len(states)):

        # s += pro[i]
        # if s >= r:
        # return actions[i
        #boat_ship. rotation = 0



    #if 480 > boat_ship.x > 420 and 522 > boat_ship.y > 518 and 95 > boat_ship.rotation > 85:
        #r = 1000
        #t = True
        #boat_ship.x, boat_ship.y = 400, 30
        #boat_ship.rotation = 0


def qlearning(num=1):
    # boat_ship.x, boat_ship.y = 400,100
    # boat_ship.rotation = 90
    # pyglet.clock.unschedule(qlearning)
    global t, r, states
    actions = [0,15, 35, -15, -35]
    for i in range(100):
        for j in range(140):
            for k in range(72):
                states.append((150+5*i, -50+5*j, -180+5*k))
    qfunc = dict()
    for i, j, k in states:
        for action in actions:
            key = "%d_%d_%d_%d" % (i, j, k, action)
            qfunc[key] = 0
    boat_ship.x, boat_ship.y, boat_ship.rotation = 400, 30, 0
    for l in range(100000):
        boat_ship.x, boat_ship.y, boat_ship.rotation = 400, 30, 0
        x, y, z = boat_ship.x, boat_ship.y, boat_ship.rotation
        t = False
        reload = False
        if reload:
            f = open('qvalue.txt', 'r')
            content = f.read()
            qfunc = eval(content)
            break
        if x < 200 or x > 600 or y < 0 or y > 600:
            t = True
            boat_ship.x, boat_ship.y, boat_ship.rotation = states[int(random.random() * len(states))]
            #print(1)
        a = actions[int(random.random() * len(actions))]
        r = 0
        count = 0
        print(l)
        while False == t and count < 1000:
            # on_draw()
            #r = 0
            key = "%d_%d_%d_%d" % (int(x/5)*5, int(y/5)*5, int(z/20)*20, a)
            #states.append((x, y, z))
            #if (x, y, z) not in states:
                #states.append((x, y, z))
            #if key not in qfunc:
                #states.append((x, y, z))
                #qfunc[key] = 0
            #update(z)
            x1, y1, z1 = step(a)
            update(z1)
            a1 = greedy(actions, qfunc, x1, y1, z1)
            key1 = "%d_%d_%d_%d" % (int(x1/5)*5, int(y1/5)*5, int(z1/20)*20, a1)
            # if key1 not in qfunc:
            # qfunc[key1] = 0
            # 把横向移动考虑进返回值里
            # r = -0.005 * abs(x1-x) # 结果它只走了很短的一段直线
            #dis = math.sqrt(np.square(x1-400)+np.square(y1-550))
            #r = 1-0.00003*dis
            qfunc[key] = qfunc[key] + 0.3 * (r + 0.99 * qfunc[key1] - qfunc[key])
            x, y, z = x1, y1, z1
            a = epsilon_greedy(actions, qfunc, x, y, z, 0.2)
            #print(a)
            count += 1
            print(qfunc[key])
    #for i in range(100):
        #for j in range(40):
            #for k in range(18):
                #for a in actions:
                    #key = "%d_%d_%d_%d" % (150+5*i, -50+5*j, -180+20*k, a)
                    #print(qfunc[key])
    return qfunc, actions


def upwd(dt):
    pyglet.clock.unschedule(upwd)
    # step(0)
    global t, s,distance
    for i in range(1):
        boat_ship.x, boat_ship.y, boat_ship.rotation = 400, 30, 0
        x, y, z = 400, 30, 0
        a = 0
        # boat_ship.rotation = 0
        t = False
        count = 0
        while False == t and count < 300:
            a1 = greedy(actions, qfunc, x, y, z)
            s.append((x, y, z))
            print(len(s))
            # print(x, y, a1)
            # time.sleep(1)
            # key = "%d_%d_%d" % (x, y, a1)
            x1, y1, z1 = step(a1)
            # print(1)
            # boat_ship.x, boat_ship.y = 500, 300
            # glBegin(GL_LINE_STRIP)
            # gl.glColor4f(0.9, 0.1, 0.1, 1.0)
            # glVertex2f(x+350, y+30)
            # glVertex2f(x1+350, y1+30)
            # glEnd()
            #distance += math.sqrt(np.square(x1-x)+np.square(y1-y))
            update(z1)
            x, y, z = x1, y1, z1
            count += 1

        # boat_ship.x, boat_ship.y = 500, 30


def shiyan(dt):
    # pyglet.clock.unschedule(shiyan)
    global p
    p += 1
    if len(s) > p:
        boat_ship.x, boat_ship.y, boat_ship.rotation = s[p]
        # time.sleep(1)
    # print(1)
    if len(s) < p:
        p = 0
    # x = 2/3
    # time.sleep(10)
    # boat_ship.y = 10
    # x,y = step(0)
    # print(x,y)


if __name__ == "__main__":
    #pyglet.clock.schedule_interval(update, 1/120.0)
    qfunc, actions = qlearning()
    #print(qfunc)
    store = True
    if store:
        f = open('qvalue.txt', 'w')
        f.write(str(qfunc))
        f.close()
    pyglet.clock.schedule_interval(upwd, 0.1)
    pyglet.clock.schedule_interval(shiyan, 0.2)
    pyglet.app.run()

    # qfunc = qlearning()