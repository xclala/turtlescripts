from turtle import Pen,done
import time
t=Pen()
t.speed(0)
t.color("red")
  
t.begin_fill()
for i in range(50):
	t.forward(200)
	t.left(170)
	t.end_fill()
del i
t.hideturtle()
done()
del t