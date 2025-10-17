import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(500,500)
hexagon=turtle.Turtle()
side=6
sidelength=70
angle=360/side
for i in range(side):
    hexagon.forward(sidelength)
    hexagon.right(angle)
turtle.done()