from turtle import Pen,done
from threading import Thread
t=Pen()
t.speed (0)
t.pensize (5)
t.pencolor ("red")
def Star():
	t.forward(200)
def Circle():
	t.circle (7)
	t.right (144)
for i in range(5):
	Star()
	Circle()
del i
t.hideturtle()
del t
done()