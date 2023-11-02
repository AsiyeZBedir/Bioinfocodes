def generate_fibonacci(n):
    # Initialize the first two Fibonacci numbers
    fib_sequence = [0, 1]

    # Generate the Fibonacci sequence
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    return fib_sequence

# Test the function
if __name__ == "__main__":
    n_terms = 10  # Change this value to generate a different number of terms
    fibonacci_sequence = generate_fibonacci(n_terms)
    print(f"Fibonacci Sequence (first {n_terms} terms): {fibonacci_sequence}")
