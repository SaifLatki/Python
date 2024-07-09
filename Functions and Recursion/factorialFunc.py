def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num= input("Enter the number to find Factorial: ")
print(f'Factorial of {num} is:', factorial(int(num)))