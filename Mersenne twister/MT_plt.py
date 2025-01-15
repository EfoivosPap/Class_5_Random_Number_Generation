import time
import matplotlib.pyplot as plt

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
        self.u = 4
        self.s = 3
        self.b = 0x5A
        self.t = 5
        self.c = 0x1F
        self.l = 6
        
        self.initialize_state(seed)
        
    def initialize_state(self, seed):
        """Initialize the state array with values derived from the seed."""
        self.state[0] = seed
        for i in range(1, self.n):
            self.state[i] = self.int_32(1812433253 * (self.state[i - 1] ^ (self.state[i - 1] >> 30)) + i)
        
    def twist(self):
        """Perform the twist operation."""
        for i in range(self.n):
            x = self.int_32((self.state[i] & self.u_mask) + (self.state[(i + 1) % self.n] & self.l_mask))
            x_a = x >> 1
            if x % 2 != 0:  # If the lowest bit of x is 1, apply constant matrix a
                x_a ^= self.a
            self.state[i] = self.state[(i + self.m) % self.n] ^ x_a
        self.index = 0
        
    def get_key(self):
        """Get the next pseudo-random number."""
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
        """Ensure the number is a 32-bit integer."""
        return number & 0xFFFFFFFF
w = 32
n = 624
m = 397
r = 31
a = 0x9908b0df
seed = 5

def stopwatch():
    # Start the stopwatch
    start_time = time.time()
    
    # Parameters: w, n, m, r, a, and seed
    mt = MersenneTwister(w, n, m, r, a, seed)    # Using a larger w and a different seed for more variety

    # Generate 100 random numbers (you can change the range to suit the needs)
    random_numbers = [mt.get_key() for _ in range(1000)]  # Use modulo 100 to keep the numbers within a range (0-99)

    # Stop the stopwatch
    end_time = time.time()
    
    # Calculate elapsed time
    elapsed_time = end_time - start_time
    
    # Print the results
    print(f"Time taken to generate 100 random numbers: {elapsed_time:.10f} seconds")

    # Create a histogram of the random numbers
    plt.hist(random_numbers, color='blue', edgecolor='black')
    plt.title('Distribution of 100 Generated Random Numbers')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

# Execute the stopwatch function
stopwatch()
