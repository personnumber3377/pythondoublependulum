
import math

class DoublePendulum:
    def __init__(self, l0, l1, w0, w1, v0, v1, a0, a1) -> None:
        # Constructor. l0 and l1 are the lengths of the massless rods connecting the two balls.
        # w0 and w1 are the weights of the balls. v0 and v1 are the initial angular velocities. (in rads/second)
        
        # Do the basic stuff, such that we can access these variables inside this class too.
        self.l0 = l0
        self.l1 = l1
        self.w0 = w0
        self.w1 = w1
        self.v0 = v0
        self.v1 = v1
        # Here a0 and a1 are the initial angles
        self.a0 = a0
        self.a1 = a1
    def get_first_point(self) -> tuple: # This returns the position of the center of the first mass.
        # This gets the first point.
        return (math.sin(self.a0) * l0, math.cos(self.a0) * l1)
    def get_second_point(self) -> tuple:
        # This gets the second point.
        # First get the first point and then use trigonometry to find the second point.
        first_point = self.get_first_point()
        return (math.sin(self.a1) * l1 + first_point[0], math.cos(self.a1) * l1 + first_point[1])
    def render(self) -> None: # This renders the stuff.
        
    def update(d_t) -> None: # Goes forward in time by d_t
        return # Just a stub for now.

