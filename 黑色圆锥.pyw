from turtle import done,Pen
t=Pen()
t.speed (0)
for i in range (1,1000,2):
	t.circle (i)
t.hideturtle()
done()
del t