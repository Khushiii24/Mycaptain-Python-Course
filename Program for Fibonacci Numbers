def fibonacci(n):
    fib_sequence = [0, 1]  # First two numbers in the sequence
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence

# Prompt the user to enter the number of Fibonacci numbers to generate
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Call the fibonacci function and print the resulting sequence
fib_nums = fibonacci(n)
print("Fibonacci Sequence:", fib_nums)
