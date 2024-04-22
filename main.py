def fibonacci(n):
    fib_sequence = [0, 1]  # Starting Fibonacci sequence
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  # Generating next Fibonacci number
    return fib_sequence[:n]

def main():
    n = int(input("Enter the number of Fibonacci terms to generate: "))
    if n <= 0:
        print("Number of terms should be greater than 0.")
    else:
        fib_sequence = fibonacci(n)
        print("Fibonacci sequence up to", n, "terms:", fib_sequence)

if __name__ == "__main__":
    main()
