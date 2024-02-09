def logistic_map(r, x0, num_iterations):
    """
    Calculate the logistic map for a given parameter 'r',
    initial value 'x0', and number of iterations.
    """
    results = []
    x = x0
    
    for _ in range(num_iterations):
        x = r * x * (1 - x)
        results.append(x)
    
    return results

# Example usage:
r = 3.9  # Parameter 'r' for the logistic map
x0 = 0.5 # Initial value of 'x'
num_iterations = 100

chaotic_sequence = logistic_map(r, x0, num_iterations)
print(chaotic_sequence)
