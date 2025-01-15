import time
import random

#The array is p g1 g2 g3
p_and_g = [
    [23, 5, 10 ,7],
    [31, 3, 11, 17],
    [97, 5, 62, 45],
    [307, 3, 30, 154]
]

class BlumMicali:
    def __init__ (self, p , g, seed):
    # We will use an array 5X4 so we can fulfill the requirements that are:
    # p must be an odd
    # g be a primitive root modulo p
        self.p = p
        self.g = g
        self.state = seed
        
    def next_bit(self):
        
        self.state = pow(self.g, self.state, self.p)
        #print(f"current state : {self.state}")
        if self.state <= (self.p - 1 )//2:
            return 1
        else:
            return 0
        
        
    def key_generation(self,length):
        
        key = ''.join(str(self.next_bit()) for _ in range(length))
        return key
    
    def get_ArrayValue(p_and_g_array):
        selected_row  = random.choice(p_and_g)
        p = selected_row[0]
        g = random.choice(selected_row[1:])
        seed = random.randint(1, p-1)
        return p, g, seed

# Get the values to but in the digit key

p, g, seed = 97, 5 , 87
bm = BlumMicali(p, g, seed)

def stopwatch(length):
    # Start the stopwatch
    start_time = time.time()
    
    key = bm.key_generation(length)

    # Stop the stopwatch
    end_time = time.time()
    
    # Calculate elapsed time
    elapsed_time = end_time - start_time
    
    # Print the results
    print(f"Selected p: {p}, g: {g}, seed: {seed}")
    print(f"The key is {key}")
    print(f"Time taken to execute {length}-bit key: {elapsed_time:.10f} seconds\n")
    
# Generate and measure keys with different lengths
stopwatch(32)