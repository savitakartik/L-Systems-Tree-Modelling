import numpy as np
from numpy.linalg import norm
class Turtle2D:
    def __init__(self,p0,o0,d,delta):
        """Initialise a 2D turtle object with an initial position and orientation

        Parameters
        ----------
        :p0: required, numpy.array, vector encoding the initial position of the turtle ([x,y]), as a numpy array
        :o0: required, numpy.array, vector encoding the initial orientation of the turtle, as a numpy array
        :d: required,  float, standard stepsize. (used whenever a stepsize is not specified in the next_position() method)
        :delta: required, float, standard turning angle. (used whenever an angle is not specified in the turn() method)
        """
        self.p=p0
        # normalize orientation vector
        self.o=o0/norm(o0)
        self.std_d=d
        self.std_delta=delta

    def next_position(self,d=None):
        """Compute the next position of the turtle given current position, current orientation, and a step length d

        Parameters
        ----------
        :d:  float, stepsize. If not specified, the standard stepsize of the turtle is used
        :returns: next position of the turtle, as a numpy array
        """
        if d==None:
            d=self.std_d
        next_position= self.p+d*self.o
        return next_position

    def next_orientation(self, delta=None):

        if delta==None:
            delta=self.std_delta
        #Evaluate the 2D rotation matrix at angle delta
        R=np.array([[np.cos(delta),-np.sin(delta)],[np.sin(delta),np.cos(delta)]])
        new_orientation=R@self.o
        return new_orientation
