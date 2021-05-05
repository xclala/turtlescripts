from turtle import Pen,done
t=Pen()
t.speed (0)
t.pensize (5)
colors=["red","orange","yellow","green","cyan","sky blue","blue","purple"]
for i in range(300):
	t.pencolor (colors[i%8])
	t.forward (i)
	t.left (88)
del colors,i
t.hideturtle()
del t
done()