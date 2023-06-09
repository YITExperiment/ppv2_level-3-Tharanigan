import turtle

from itertools import cycle
colors = cycle({'Deep Pink','Maroon','Aquamarine','red', 'purple', 'green', 'yellow','white','grey','peru' })

def draw_circle(size,angle,shift):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+5,angle+1,shift+1)

turtle.bgcolor('Misty Rose')
turtle.speed('fast')
turtle.pensize(40)
draw_circle(30,0,1)
