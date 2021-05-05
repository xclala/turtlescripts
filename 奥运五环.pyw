from turtle import done,Pen
t=Pen()
t.pensize (10)
t.speed (0)
colors=["black","red","green","yellow","blue"]
Pos=[(0,0),(100,0),(50,-55),(-50,-55),(-100,0)]
name=["非洲","美洲","澳洲","亚洲","欧洲"]
Pos_name=[(0,50),(100,50),(50,5),(-50,5),(-100,50)]
for i in range(5):
	t.penup()
	t.goto (Pos[i])
	t.pendown()
	t.pencolor (colors[i])
	t.circle (50)
	t.penup()
	t.goto (Pos_name[i])
	t.pendown()
	t.write (name[i],font=8)
del Pos,Pos_name,colors,i
t.hideturtle()
del t
done()