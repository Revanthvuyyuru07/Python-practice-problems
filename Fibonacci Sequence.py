# A program to print the fibonacci sequence using recursion.

def fibonacci(n):

    if n <= 0:
        return "Invalid input"

    elif n == 1:
        return 0

    elif n == 2:
        return 1
        
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n_terms = int(input("Enter number of terms: "))

for i in range(1, n_terms + 1):
    print(fibonacci(i), end=" ")