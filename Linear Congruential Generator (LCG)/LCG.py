import time

def linear_congruential_generator(seed, a, c, m, n):
    # Initialize the sequence with the seed
    number = seed
    random_string = ""
    
    while len(random_string) < n:
        # Generate the next number in the sequence Xn 
        number = (a * number + c) % m 
        # Convert the number to a string and append to the result
        random_string += str(number)
    
    # Trim the result to the desired number of digits
    return random_string[:n]

#Variable Set
seed = 0
a = 0
c = 0
m = 0
length = 0

def stopwatch():
    start_time = time.time()
    
    key = linear_congruential_generator(seed, a, c, m, length)
    
    end_time = time.time()
    
    # Calculate elapsed time
    elapsed_time = end_time - start_time
    
    # Print the results
    print(f"Generated {length}-digit pseudo-random string:")
    print(key)
    print(f"Time taken to execute: {elapsed_time:.10f} seconds")
    
stopwatch()