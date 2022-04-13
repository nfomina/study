import turtle as t
import random as r

t.Screen().setup(600, 600)
t.Screen().bgcolor('darkblue')
t.speed(0)
bcount = r.randrange(6, 9)
bheights = [r.randrange(40, 400, 25) for i in range(bcount)]
blenghts = [r.randrange((600 // bcount) - 30, (600 // bcount) + 30) for i in range(bcount)]
pos = [-300, -300]


def buildings():
    global pos
    t.pu()
    t.goto(pos)
    t.pd()
    t.fillcolor(0, 102, 218)
    t.begin_fill()
    for i in range(bcount):
        t.goto(pos[0], pos[1] + bheights[i])
        t.forward(blenghts[i])
        pos[0] = t.xcor()
    if t.xcor() != 300:
        t.goto(300, t.ycor())
        t.goto(300, -300)
    t.end_fill()
    pos = [-300, -300]


def windows():
    for i in range(bcount):
        t.pu()
        t.goto(r.randrange(pos[0], pos[0] + blenghts[i] - 20), r.randrange(-280, -300 + bheights[i]))
        print('pos', t.pos())
        t.pd()
        pos[0] = pos[0] + blenghts[i]
        t.fillcolor('yellow')
        t.begin_fill()
        for j in range(4):
            t.forward(20)
            t.right(90)
        t.end_fill()


def stars():
    pos = [-300, -300]
    for i in range(bcount):
        for j in range(4):
            t.pu()
            t.goto(r.randrange(pos[0], pos[0] + blenghts[i] - 20), r.randrange(-290 + bheights[i], 300))
            t.pd()
            t.dot(r.randint(5, 8), 'yellow')

        pos[0] = pos[0] + blenghts[i]


buildings()
windows()
stars()