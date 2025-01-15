import time

class MersenneTwister:
    def __init__(self, w, n, m, r, a, seed):
        self.w = w
        self.n = n
        self.m = m
        self.r = r
        self.a = a
        
        self.u_mask = 1 << (w - 1)  # Upper w - r bits mask
        self.l_mask = (1 << (w - r)) - 1  # Lower r bits mask
        self.state = [0] * n
        self.index = n
        
        # Tempering parameters 
        # #this are the parameters that are recomended for the MT19937
        self.u = 11
        self.s = 7
        self.b = 0x9D2C5680
        self.t = 15
        self.c = 0xEFC60000
        self.l = 18
        
        self.initialize_state(seed)
        
    def initialize_state(self, seed):
        #Initialize the state array with values derived from the seed.
        self.state[0] = seed
        for i in range(1, self.n):
            self.state[i] = self.int_32(1812433253 * (self.state[i - 1] ^ (self.state[i - 1] >> 30)) + i)
        
    def twist(self):
        #Perform the twist operation.
        for i in range(self.n):
            x = self.int_32((self.state[i] & self.u_mask) + (self.state[(i + 1) % self.n] & self.l_mask))
            x_a = x >> 1
            if x % 2 != 0:  # If the lowest bit of x is 1, apply constant matrix a
                x_a ^= self.a # this is used for the bitwise XOR
            self.state[i] = self.state[(i + self.m) % self.n] ^ x_a
        self.index = 0
        
    def get_key(self):
        # Get the next pseudo-random number.
        if self.index >= self.n:
            self.twist()

        y = self.state[self.index]
        self.index += 1

        # Apply tempering transformations
        y ^= (y >> self.u)
        y ^= (y << self.s) & self.b
        y ^= (y << self.t) & self.c
        y ^= (y >> self.l)

        return self.int_32(y)
    
    def int_32(self, number):
        #Ensure the number is a 32-bit integer.
        return number & 0xFFFFFFFF

w = 32
n = 5
m = 397
r = 31
a = 0x9908b0df
seed = 5
    
# Parameters: w, n, m, r, a, and seed
mt = MersenneTwister(w, n, m, r, a, seed)  

key =mt.get_key
print(f"The key is: {key}")
