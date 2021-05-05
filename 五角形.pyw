from turtle import done,Pen
t=Pen()
t.speed (0)
colors=["red","orange","yellow","green","cyan"]
t.pensize (11)
for i in range(5):
	t.pencolor (colors[i%5])
	t.forward (100)
	t.left (72)
del i,colors
t.hideturtle()
done()
del t