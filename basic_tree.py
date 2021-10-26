from turtle import Turtle, Screen
import random
import turtle as t

t.colormode(255)
tim = Turtle()
tim.setheading(90)
tim.width(3)
tim.speed(200)


TURN_ANGLE = 20
SHRINK_FACTOR = 0.8
BRANCH_LEVEL = 8

color_list = [(113, 95, 57), (15, 16, 21), (192, 159, 113), (25, 19, 22), (25, 39, 26), (79, 74, 32), (159, 136, 68),
              (73, 98, 67), (234, 218, 187), (222, 195, 146), (81, 83, 113), (49, 78, 40), (125, 38, 18), (105, 80, 93),
              (47, 53, 101), (147, 148, 168), (141, 160, 139), (169, 143, 151), (85, 50, 66), (118, 112, 159),
              (175, 109, 90), (111, 143, 100), (155, 111, 124), (211, 216, 226), (214, 225, 213), (230, 209, 214),
              (221, 179, 168), (182, 183, 216), (221, 174, 181)]


def tree(size, color_scheme, TREE_LEVEL=0):
    if TREE_LEVEL <= BRANCH_LEVEL:
        tim.width(BRANCH_LEVEL - TREE_LEVEL)
        if color_scheme == 'random':
            tup = random.choice(color_list)
            tim.color(tup)
        elif color_scheme == 'green_trees':
            if TREE_LEVEL == 0:
                tim.color("brown")
            elif TREE_LEVEL < 3:
                tim.color("green")
            elif TREE_LEVEL < 5:
                tim.color((100, 248, 0))
            else:
                tim.color((225, 248, 100))
        tim.forward(size)
        tim.right(TURN_ANGLE)
        tree(size*SHRINK_FACTOR, color_scheme, TREE_LEVEL+1)
        tim.left(2*TURN_ANGLE)
        tree(size*SHRINK_FACTOR, color_scheme, TREE_LEVEL+1)
        tim.right(TURN_ANGLE)
        tim.backward(size)


tree(70, 'random')
my_screen = Screen()
my_screen.exitonclick()
