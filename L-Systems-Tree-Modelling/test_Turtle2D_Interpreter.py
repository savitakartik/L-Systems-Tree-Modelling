import unittest
from Turtle2D import Turtle2D

class Turtle2DTest(unittest.TestCase):
    """
    Tests the :class:`Turtle2D` class.
    """
    def test_show_tree(self):
        turtle=Turtle2D(p0=np.array([250,0]),o0=np.array([0,1]),std_d=10,std_delta=29.5)
        next_position=turtle.next_position()
        drawer=Tree_drawing_2D(turtle,(50,50),color_scheme='natural',color_type='sequential')
        test_string='[F[+F][-F[-F]F]F[+F][-F]]'
        drawer.draw_tree(test_string)
        with self.assertRaises(TypeError):
            drawer.show_tree()

