import time
from math import gcd

class BlumBlumShub:
    def __init__(self, p, q, seed=None):
        
        if p % 4 != 3 or q % 4 != 3:
            print("Both p and q must be primes congruent to 3 Mod 4")  
            
        self.m = p * q
        
        if gcd(seed,self.m)  != 1:
            print("Seed must be coprime to M")
            
        self.state = seed
        
    def next_bit(self):
        self.state = pow(self.state, 2, self.m)  # x_n+1 = x_n^2 mod M
        print(f"the state is {self.state}")
        return self.state & 1 
    
    def key_generation(self,length):
        
        key = ''.join(str(self.next_bit()) for _ in range(length))
        return key
  
p = 7
q = 11
seed = 3

def stopwatch(length):
    # Start the stopwatch
    
    start_time = time.time()
    
    bbs = BlumBlumShub(p,q,seed)

    key = bbs.key_generation(length)
    
    # Stop the stopwatch
    end_time = time.time()
    
    # Calculate elapsed time
    elapsed_time = end_time - start_time
    
    # Print the results

    print(f"The key is {key}")
    print(f"Time taken to execute: {elapsed_time:.10f} seconds")
    

# Execute the stopwatch function
stopwatch(10)