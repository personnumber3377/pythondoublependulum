
class DoublePendulum:
    def __init__(self, l0, l1, w0, w1, v0, v1) -> None:
        # Constructor. l0 and l1 are the lengths of the massless rods connecting the two balls.
        # w0 and w1 are the weights of the balls. v0 and v1 are the initial angular velocities. (in rads/second)
        
        # Do the basic stuff, such that we can access these variables inside this class too.
        self.l0 = l0
        self.l1 = l1
        self.w0 = w0
        self.w1 = w1
        self.v0 = v0
        self.v1 = v1
    def update(d_t) -> None: # Goes forward in time by d_t
    

