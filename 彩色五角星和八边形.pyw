from turtle import Pen,done
t=Pen()
t.speed (0)
t.pensize (11)
colors=["red","orange","yellow","green","cyan","blue","purple"]
for a in range (5):
	for c in range(7):
		t.pencolor (colors[c%7])
		t.forward (40)
	t.right (144)
del a,c
t.penup()
t.forward (300)
t.pendown()
for b in range(8):
	for d in range(7):
		t.pencolor (colors[d%7])
		t.forward (40)
	t.right (135)
del b,d,colors
t.hideturtle()
del t
done()
