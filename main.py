import turtle as t
import random

color_list = [(185, 162, 132), (129, 92, 70), (79, 93, 118), (147, 161, 180), (179, 152, 162), (210, 207, 135), (28, 35, 49), (119, 79, 92), (54, 24, 33), (46, 25, 19), (147, 170, 154), (86, 107, 91), (161, 156, 60), (113, 31, 43), (168, 107, 98), (27, 37, 33), (51, 58, 92), (212, 179, 189), (110, 123, 155), (117, 37, 27), (161, 107, 118), (219, 178, 170), (177, 202, 186), (180, 187, 209), (106, 144, 116), (67, 75, 35)]

tim = t.Turtle()
screen = t.Screen()

t.colormode(255)
tim.speed("fastest")
tim.hideturtle()
tim.penup()

def reset_pos(x):
    tim.backward(x * 10)
    tim.left(90)
    tim.forward(x)
    tim.right(90)

def horizontal_dots(spaces):
    for _ in range(10):
        dot_color = random.choice(color_list)
        tim.dot(20, dot_color)
        tim.forward(spaces)
    reset_pos(spaces)

for _ in range(10):
    horizontal_dots(40)


screen.exitonclick()