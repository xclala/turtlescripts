from turtle import Pen,done
t=Pen()
t.speed (0)
t.pensize (2.5)
for i in range(300):
	t.forward (i)
	t.left (88)
del i
t.hideturtle()
done()
del t