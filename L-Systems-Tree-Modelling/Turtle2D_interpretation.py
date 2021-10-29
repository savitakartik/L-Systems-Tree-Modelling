import numpy as np
from numpy.linalg import norm
import cv2
from matplotlib import cm
import warnings
class Turtle2D:
    def __init__(self,p0,o0,std_d,std_delta):
        """Initialise a 2D turtle object with an initial position and orientation

        Parameters
        ----------
        :p0: required, numpy.array, vector encoding the initial position of the turtle ([x,y]), as a numpy array
        :o0: required, numpy.array, vector encoding the initial orientation of the turtle, as a numpy array
        :d: required,  float, standard stepsize. (used whenever a stepsize is not specified in the next_position() method)
        :delta: required, float, standard turning angle. (used whenever an angle is not specified in the turn() method)
        """
        #store initial position/orientation in order to rest
        self.p0=p0
        self.o0=o0

        #Initialise poition as initial position
        self.p=p0
        # Initialise orientation as initial orientation vector
        self.o=o0/norm(o0)
        self.std_d=std_d
        self.std_delta=std_delta
    
    def set_position(self,p):
        self.p=p
    def set_orientation(self,o):
        self.o=o

    def reset(self):
        self.p=self.p0
        self.o=self.o0

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
        #Evaluate the 2D rotation matrix at angle delta (first convert to radians)
        delta=np.radians(delta)
        R=np.array([[np.cos(delta),-np.sin(delta)],[np.sin(delta),np.cos(delta)]])
        new_orientation=R@self.o
        return new_orientation

    def step(self,d=None):
        if d==None:
            d=self.std_d
        self.p=self.next_position(d)

    def turn(self,dir,delta=None):
        if delta==None:
            delta=self.std_delta
        if dir=='+':
            self.o=self.next_orientation(delta)
        elif dir=='-':
            self.o=self.next_orientation(-delta)
        else:
            raise(TypeError('string argument dir should contain either + (anticlockwise) or - (clockwise)'))

class Tree_drawing_2D:
    def __init__(self,turtle,canvas_size,thickness,radius,color_scheme,color_type):
        self.canvas_size=canvas_size
        self.img=255*np.ones((canvas_size[0],canvas_size[1],3))
        self.turtle=turtle
        self.thickness=thickness
        self.leaf_radius=radius
        self.color=(0,0,98)
        self.branch_count=0

        #Colorschemes
        self.color_scheme=color_scheme
        self.color_type=color_type

        if self.color_scheme=='natural':
            self.branch_cmap=cm.get_cmap('copper',1000)
        elif self.color_scheme=='rainbow':
            self.branch_cmap=cm.get_cmap('gist_rainbow',1000)
        self.leaf_cmap=cm.get_cmap('Greens',100)

        #tracker variables for greatest displacement of the turtle in the x and y axis. Useful to make sure the screen size is big enough to contain the tree
        self.biggest_x=0
        self.biggest_y=0
    def random_leaf_color(self):
        color_rgba=self.leaf_cmap(np.random.rand())
        color_bgr=(color_rgba[2],color_rgba[1],color_rgba[0])
        return color_bgr
    def sequential_branch_color(self,k):
        color_rgba=self.branch_cmap(k)
        color_bgr=(color_rgba[2],color_rgba[1],color_rgba[0])
        return color_bgr
    def random_branch_color(self):
        color_rgba=self.branch_cmap(np.random.rand())
        color_bgr=(color_rgba[2],color_rgba[1],color_rgba[0])
        return color_bgr
    def cv_coord(self,cartesian_coords):
        cv_coords=np.zeros(cartesian_coords.shape)
        cv_coords[1]=-cartesian_coords[1]+self.canvas_size[1]
        cv_coords[0]=cartesian_coords[0]
        return cv_coords
    
    def draw_segment(self,start,end,segment_type,n_branches):
        #First, convert between cartesian and cv coordinates
        cv_start=self.cv_coord(start)
        cv_end=self.cv_coord(end)
        if self.color_type=='sequential':
            branch_color=self.sequential_branch_color(self.branch_count/n_branches)
        elif self.color_type=='random':
            branch_color=self.random_branch_color()
        if segment_type=='branch':
            self.img=cv2.line(self.img,cv_start.astype(int),cv_end.astype(int),thickness=self.thickness,color=branch_color)
        elif segment_type=='apex':
            leaf_color=self.random_leaf_color()
            self.img=cv2.line(self.img,cv_start.astype(int),cv_end.astype(int),thickness=self.thickness,color=branch_color)
            self.img=cv2.circle(self.img,cv_end.astype(int),self.leaf_radius,color=leaf_color,thickness=-1)
        #cv2.imshow('img',self.img)
        #cv2.waitKey(0)
    
    def draw_branch(self,L_string,i,n_branches):
        self.branch_count+=1
        while i<len(L_string):
            c=L_string[i]
            if c=='[': #New branch is opened
                #Store current position of the turtle 
                cur_position=self.turtle.p
                cur_orientation=self.turtle.o
                #Draw the branch (reading the string from the next character onwards)
                new_i=self.draw_branch(L_string,i+1,n_branches)
                #restore the position
                self.turtle.set_position(cur_position)
                self.turtle.set_orientation(cur_orientation)
                i=new_i
            elif c==']': #Current branch is closed. return call
                return i
            elif c=='F':
                #Step the turtle forward and draw the corresponding segment
                new_position=self.turtle.next_position()
                if L_string[i+1]==']':
                    self.draw_segment(self.turtle.p, new_position,segment_type='apex',n_branches=n_branches)
                else :
                    self.draw_segment(self.turtle.p, new_position,segment_type='branch',n_branches=n_branches)
                    
                self.turtle.step()
                #if needed, update the "greater displacement" trackers:
                if np.abs(self.turtle.p[0]-self.turtle.p0[0])>self.biggest_x:
                    self.biggest_x=np.abs(self.turtle.p[0]-self.turtle.p0[0])
                if np.abs(self.turtle.p[1]-self.turtle.p0[1])>self.biggest_y:
                    self.biggest_y=np.abs(self.turtle.p[1]-self.turtle.p0[1])
            elif c=='+':
                #Rotate the turtle orientation
                self.turtle.turn('+')
            elif c=='-':
                #Rotate the turtle orientation
                self.turtle.turn('-')
            i+=1
    def count_branches(self,L_string):
        count=0
        for c in L_string:
            if c=='[':
                count+=1
        return count
    def draw_tree(self,L_string):
        self.branch_count=0 #reset branch count
        #Count branches
        n_branches=self.count_branches(L_string)
        #Generate colormap

        self.draw_branch(L_string,0,n_branches)

    def show_tree(self):
        if self.canvas_size[0]<2*self.biggest_x or self.canvas_size[1]<self.biggest_y:
            warnings.warn('Canvas size is too small for the current tree. Please increase the plot size or decrease the turtle stepsize')
            flag=False
            return flag
        cv2.startWindowThread()
        cv2.imshow('tree',self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        flag=True
        #return flag

