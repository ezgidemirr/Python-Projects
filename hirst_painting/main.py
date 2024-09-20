# # This is a sample Python script.
#
# import colorgram
# # Extract 6 colors from an image.
# colors = colorgram.extract('painting.jpg', 30)
# print(colors)
#
#
# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
# first_color = colors[0]
# second_color= colors[1]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion  = first_color.proportion # e.g. 0.34

# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:
#red = rgb[0]
#red = rgb.r
#saturation = hsl[1]
#saturation = hsl.s

# rgb_colors= []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,b,g)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

turtle= turtle_module.Turtle()
turtle.penup()
turtle_module.colormode(255)
color_list = [ (151, 46, 104), (178, 22, 150), (83, 27, 34), (12, 73, 57), (31, 120, 100), (101, 47, 41), (56, 122, 137), (108, 29, 39), (22, 50, 65), (39, 7, 81), (94, 68, 62), (199, 65, 91), (110, 9, 8), (116, 77, 167), (226, 227, 232), (131, 92, 178), (139, 176, 167), (217, 140, 203), (179, 151, 148), (177, 178, 205), (226, 167, 177), (160, 112, 109), (26, 93, 76), (215, 181, 178), (95, 149, 141), (45, 6, 81)]


turtle.setheading(225)
turtle.forward(310)
turtle.setheading(0)

for i in range(5):
    for i in range(10):
        turtle.dot(20, random.choice(color_list))
        turtle.forward(50)

    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)

    for j in range(10):
          turtle.forward(50)
          turtle.dot(20, random.choice(color_list))

    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(0)






