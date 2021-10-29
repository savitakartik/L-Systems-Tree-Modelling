import unittest
import numpy as np
from Turtle2D_interpretation import *
import cv2
class Turtle2DTest(unittest.TestCase):
    """
    Tests the :class:`Turtle2D` class.
    """
    def test_show_tree(self):
        turtle=Turtle2D(p0=np.array([250,0]),o0=np.array([0,1]),std_d=10,std_delta=29.5)
        drawer=Tree_drawing_2D(turtle,(500,500),2,3,color_scheme='natural',color_type='sequential')
    
        test_string='[F[+F][-F[-F]F]F[+F][-F]]'
        drawer.draw_tree(test_string)
        with self.assertWarns(Warning):
            drawer.show_tree()
            cv2.destroyAllWindows()

