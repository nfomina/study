import turtle as t


def draw_simple_bear(size):
    # Параметры окна
    t.Screen().setup(720, 720)

    t.speed(11)
    t.pensize(size * 0.03)
    t.pencolor('SaddleBrown')
    t.hideturtle()

    # Программа

    # Бошка
    t.penup()
    t.setpos(0, -size * 1.8)
    t.pendown()
    t.fillcolor('BurlyWood')
    t.begin_fill()
    t.circle(size * 2)
    t.end_fill()

    # Морда
    t.fillcolor('NavajoWhite')
    t.begin_fill()
    t.circle(size * 1.2)
    t.end_fill()

    # Пасть
    t.fillcolor('Maroon')
    t.penup()
    t.setpos(0, -size / 10)
    t.pendown()
    t.begin_fill()
    t.circle(size / 5)
    t.end_fill()
    t.setpos(0, -size)

    # Глазки-бусинки
    for eye_pos in [(-size, size / 3), (size, size / 3)]:
        t.color('Black', 'Black')
        t.penup()
        t.setpos(eye_pos)
        t.pendown()
        t.begin_fill()
        t.circle(size // 5)
        t.end_fill()

    # Дебильные ухи
    for ear_pos in [(-size * 1.7, size * 1.5), (size * 1.7, size * 1.5)]:
        t.fillcolor('LightPink')
        t.penup()
        t.setpos(ear_pos)
        t.pendown()
        t.begin_fill()
        t.circle(size // 2)
        t.end_fill()



crop = int(input('Масштаб мишки относительно окна: '))
draw_simple_bear(crop)
t.done()