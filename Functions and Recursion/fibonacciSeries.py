def fibonacci(n):
    fibonacci_series = []
    if n <= 0:
        return fibonacci_series
    elif n == 1:
        fibonacci_series.append(0)
    else:
        fibonacci_series = [0, 1]
        while len(fibonacci_series) < n:
            next_num = fibonacci_series[-1] + fibonacci_series[-2]
            fibonacci_series.append(next_num)
    return fibonacci_series


num=input("Give the range of numbers to print the series of Fibonacci: ")
fib_sequence = fibonacci(int (num))
print(f'Fibonacci sequence up to { int (num)}  fibonacci series is : {fib_sequence}')
