#!/usr/bin/python3
"""
A script to calculate the fewest number of operations needed
to result in exactly n H characters in the file.
"""

def minOperations(n):
    if n <= 1:
        return 0
    
    current = 1  # Current number of H characters
    clipboard = current  # Number of characters in the clipboard
    operations_count = 0  # Total operations count
    
    while current < n:
        # If n is divisible by the current number of characters,
        # we can double the characters using copy all and paste (2 ops).
        if n % current == 0:
            clipboard = current
            current *= 2
            operations_count += 2
        else:
            # If not divisible, we paste the characters in the clipboard (1 op).
            current += clipboard
            operations_count += 1
    
    return operations_count

# Example usage:
n = 9
print(minOperations(n))  # Output: 6
