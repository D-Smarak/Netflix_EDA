

# Write a program to generate the Fibonacci sequence of a given number.

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

number = int(input("Enter the number of Fibonacci sequence elements to generate: "))
print("Fibonacci sequence:", fibonacci(number))


# Output:
# Enter the number of Fibonacci sequence elements to generate: 10
# Fibonacci sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
