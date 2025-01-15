from math import gcd
import numpy as np

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
    
    def key_generation(self):
        bits = []
        seen_states = set()
        while self.state not in seen_states:
            seen_states.add(self.state)
            bits.append(self.next_bit())
        
        # Return the Period
        return len(bits)

# Function to calculate periods for all valid seeds
def calculate_periods(p, q):
    m = p * q
    valid_seeds = [seed for seed in range(2, m) if gcd(seed, m) == 1]
    periods = []
    seeds = []
    
    for seed in valid_seeds:
        bbs = BlumBlumShub(p, q, seed)
        period = bbs.key_generation()
        periods.append(period)
        seeds.append(seed)
    
    return periods, seeds

def print_period_stats(p, q):
    periods, seeds = calculate_periods(p, q)
    
    if periods:
        max_period = max(periods)
        min_period = min(periods)
        avg_period = int(np.mean(periods))  
        
        max_seed = seeds[periods.index(max_period)]
        min_seed = seeds[periods.index(min_period)]
        
        print(f"Maximum Period: {max_period-1} (Seed: {max_seed})")
        print(f"Minimum Period: {min_period} (Seed: {min_seed})")
        print(f"Average Period: {avg_period}")

# Set p and q values
p,q = 524347, 524351

# Print period statistics
print_period_stats(p, q)
