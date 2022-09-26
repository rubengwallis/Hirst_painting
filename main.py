
from turtle import *
import random

# colors = color-gram.extract('image.jpg', 30)
# all_colors=[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     all_colors.append(new_color)
# print(all_colors)
color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83),
              (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47),
              (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186),
              (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82),
              (46, 73, 62), (47, 66, 82)]

turt = Turtle()
colormode(255)
turt.penup()
x = -200
y = -200
for z in range(0, 10):
    y += 50
    turt.goto(x, y)
    for i in range(0, 10):
        turt.dot(20, random.choice(color_list))
        turt.penup()
        turt.forward(50)


screen = Screen()
screen.exitonclick()
