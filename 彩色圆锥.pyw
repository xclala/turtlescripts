from turtle import done,Pen
t=Pen()
t.speed (0)
t.pensize (3)
colors=["red","orange","yellow","green","cyan","blue","purple"]
for i in range (1,1000,4):
	t.pencolor (colors[i%7])
	t.circle (i)
del i,colors
t.hideturtle()
del t
done()