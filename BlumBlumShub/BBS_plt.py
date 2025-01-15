import time
import matplotlib.pyplot as plt
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
        return self.state & 1 
    
    def key_generation(self,length):
        
        key = ''.join(str(self.next_bit()) for _ in range(length))
        return key
    

def measure_time(p, q, seed, keystring):
    elapsed_time =[]
    bbs = BlumBlumShub(p, q, seed)
    for length in keystring:
        start_time = time.time()
        bbs.key_generation(length)
        end_time = time.time()
        elapsed_time.append(end_time - start_time)
        
    return elapsed_time
        
def timeplot(lengths, times):
    plt.figure(figsize = (10,6))
    plt.plot(lengths, times, marker = "o", color ="b")
    plt.xlabel('Key Length (Number of Bits)', fontsize=12)
    plt.ylabel('Execution Time (Seconds)', fontsize=12)
    plt.title('Execution Time vs Key Length for BlumBlumShub', fontsize=14)
    plt.grid(True)
    plt.legend()
    plt.show()
    
p = 7 
q = 11  
seed = 3  
key_lengths = [32, 64, 512, 1024, 2048, 4096]

times = measure_time(p, q, seed, key_lengths)

# Visualize the results
timeplot(key_lengths, times)
    