import turtle as t
t.speed(10)
t.Screen().bgcolor('white')
n = 39
t.goto(0, -n)
for _ in range(4):
  t.forward(5 * n)
  t.left(90)
t.penup()
for x in range(5):
  for y in range(5):
    if (x + y) % 2 == 0:
      t.goto(x * n, y * n)
      t.begin_fill()
      for _ in range(4):
        t.forward(n)
        t.right(90)
      t.end_fill()
t.hideturtle()