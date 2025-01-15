from math import gcd
import matplotlib.pyplot as plt
from collections import Counter

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

def analyze_randomness(bits):
    """
    Perform a cryptographic analysis of the bit sequence.
    1. Count the occurrence of '0's and '1's.
    2. Visualize the bit distribution.
    """
    # Count '0's and '1's
    counter = Counter(bits)
    zeros = counter['0']
    ones = counter['1']
    labels = ['0', '1']
    values = [zeros, ones]
    plt.bar(labels, values, color=['blue', 'orange'])
    plt.title("Bit Distribution in BBS Key")
    plt.ylabel("Count")
    plt.xlabel("Bit Value")
    plt.show()

p = 23  # Prime number congruent to 3 Mod 4
q = 11  # Prime number congruent to 3 Mod 4
seed = 67 # Seed coprime to p*q
key_length = 100  # Length of the key for analysis

# Generate a key using BlumBlumShub
bbs = BlumBlumShub(p, q, seed)
key = bbs.key_generation(key_length)

# Analyze the randomness of the generated key
print(f"the key is {key}")
analyze_randomness(key)

