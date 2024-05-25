def fibonacci(n):
    fib_series = [0, 1]  # Initialize the series with the first two Fibonacci numbers
    
    # Generate Fibonacci series up to the nth term
    while len(fib_series) < n:
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)
    
    return fib_series

# Example usage:
n = int(input("Enter the number of terms in the Fibonacci series: "))
print("Fibonacci series:")
print(fibonacci(n))