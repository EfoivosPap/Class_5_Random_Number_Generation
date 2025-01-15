import time
import random
from math import gcd

# The array includes pairs of primes p and q, both congruent to 3 mod 4
p_and_q = [
    [7, 11],
    [11, 23],
    [47, 59],
    [83,103],
    [524347, 524351]
]

class BlumBlumShub:
    def __init__(self, p, q, seed):
        if p % 4 != 3 or q % 4 != 3:
            print(f"Error: p = {p}, q = {q} do not satisfy p % 4 == 3 and q % 4 == 3")
        
        self.m = p * q
        
        if gcd(seed, self.m) != 1:
            print("Seed must be coprime to M.")
        
        self.state = seed
        
    def next_bit(self):
        self.state = pow(self.state, 2, self.m)  # x_n+1 = x_n^2 mod M
        return self.state & 1 
    
    def key_generation(self, length):
        key = ''.join(str(self.next_bit()) for _ in range(length))
        return key
    
    
    def get_ArrayValue(p_and_q_array):
        # Randomly select a row of primes p and q
        selected_row = random.choice(p_and_q_array)
        p, q = selected_row
        
        # Generate a random seed coprime to m = p * q
        m = p * q
        while True:
            seed = random.randint(2, m - 1)  # Seed must be between 2 and m-1
            if gcd(seed, m) == 1:
                break
        
        return p, q, seed


# Get values from the array for BlumBlumShub
p, q, seed = BlumBlumShub.get_ArrayValue(p_and_q)
bbs = BlumBlumShub(p, q, seed)
length = 10

def stopwatch():
    # Start the stopwatch
    start_time = time.time()
    
    key = bbs.key_generation(length)
    
    # Stop the stopwatch
    end_time = time.time()
    
    # Calculate elapsed time
    elapsed_time = end_time - start_time
    
    # Print the results
    print(f"Selected p: {p}, q: {q}, seed: {seed}")
    print(f"The key is {key}")
    print(f"Time taken to execute: {elapsed_time:.10f} seconds")
    
# Execute the stopwatch function
stopwatch()
