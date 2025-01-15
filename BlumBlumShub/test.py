from math import gcd

# BlumBlumShub Algorithm
class BlumBlumShub:
    def __init__(self, p, q, seed=None):
        if p % 4 != 3 or q % 4 != 3:
            print("Both p and q must be primes congruent to 3 Mod 4")  
            
        self.m = p * q
        
        if gcd(seed, self.m) != 1:
            print("Seed must be coprime to M")
        
        self.state = seed
        
    def next_bit(self):
        self.state = pow(self.state, 2, self.m)  # x_n+1 = x_n^2 mod M
        return self.state & 1 
    
    def key_generation(self, length):
        bits = []
        
        # Generate the bits until we reach the desired length
        for _ in range(length):
            bits.append(self.next_bit())
        
        return ''.join(map(str, bits))

# Function to print all keys for the given seeds
def print_all_keys(p, q, seeds, key_length):
    for seed in seeds:
        bbs = BlumBlumShub(p, q, seed)
        key = bbs.key_generation(key_length)
        print(f"Seed: {seed} -> Key: {key}")

# Example usage
p = 7
q = 11
key_length = 10  # You can adjust the length of the generated key

# Predefined array of valid seeds
seeds = []

# Print all keys for the given seeds
print_all_keys(p, q, seeds, key_length)
