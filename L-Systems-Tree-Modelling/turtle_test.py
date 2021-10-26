from Turtle2D_interpretation import *
import cv2
import numpy as np


turtle=Turtle2D(p0=np.array([300,0]),o0=np.array([0,1]),std_d=100,std_delta=45)
next_position=turtle.next_position()

drawer=Tree_drawing_2D(turtle,(600,600))

test_string='[F[+F][-F[-F]F]F[+F][-F]]'
drawer.draw_branch(test_string,0)
drawer.show_tree()
