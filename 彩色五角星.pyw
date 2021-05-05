from turtle import Pen,done
from gc import collect
t=Pen()
t.speed (0)
t.pensize (11)
colors=["red","orange","yellow","green","cyan","blue","purple"]
for a in range (5):
	for c in range (7):
		t.pencolor (colors[c%7])
		t.forward (53)
	t.right (144)
del a,c,colors
t.hideturtle()
del t
done()
collect()