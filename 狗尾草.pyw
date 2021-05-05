from turtle import *
from random import random,randint
speed(0)
color('green')
pensize(10)
up()
goto(0,-300)
down()
left(80)
fd(140)
def draw(length=60):
    if length > 1:
        randangle = random()
        randlen = random()
        right(20 * randangle)
        fd(length)
        up()
        backward(length)
        down()
        left(40 * randangle)
        fd(length)
        draw(length - 10 * randlen)
draw()
done()

