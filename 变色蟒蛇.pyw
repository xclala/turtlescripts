try:
	from random import randint,choice
	import turtle
	from time import sleep
	while True:
		turtle.speed(0)
		turtle.setup(650,350,200,200)
		turtle.penup()
		turtle.fd(-250)
		turtle.pendown()
		turtle.pensize(randint(10,25))
		turtle.pencolor(choice(['red','orange','yellow','green','cyan','blue','purple','gold','gray','pink','black','plum','hotpink','salmon','orangered','coral','lightpink','maroon']))
		turtle.seth(-40)
		for i in range(4):
			turtle.circle(40,80)
			turtle.circle(-40,80)
		turtle.circle(40,40)
		turtle.fd(40)
		turtle.circle(16,180)
		turtle.fd(40*2/3)
		sleep(randint(1,5))
		turtle.hideturtle()
		turtle.clear()
		turtle.reset()
except:
	pass