import matplotlib.pyplot as plt

class BlumMicali:
    def __init__(self, p, g, seed):
        self.p = p
        self.g = g
        self.state = seed

    def next_bit(self):
        print(f"the state is {self.state}")
        self.state = pow(self.g, self.state, self.p)
        if self.state <= (self.p - 1) // 2:
            return 1
        else:
            return 0

    def key_generation(self, length):
        # Generate a key of given length
        key = ''.join(str(self.next_bit()) for _ in range(length))
        return key

# Parameters
p, g = 97, 5
seed = 46  # A valid seed

# Create the Blum-Micali instance
bm = BlumMicali(p, g, seed)
key_length = 100  # Length of the key to generate

# Generate the key
key = bm.key_generation(key_length)

# Count the number of 1s and 0s in the generated key
count_ones = key.count('1')
count_zeros = key.count('0')

# Plot the result
labels = ['1s', '0s']
counts = [count_ones, count_zeros]

# Create a bar chart to visualize the counts of 1s and 0s
plt.bar(labels, counts, color=['blue', 'red'])
plt.title(f'Binary Key Distribution (Length = {key_length})')
plt.xlabel('Binary Value')
plt.ylabel('Count')
plt.show()

# Output the key and counts
print(f"Generated key: {key}")
print(f"Number of 1s: {count_ones}")
print(f"Number of 0s: {count_zeros}")
