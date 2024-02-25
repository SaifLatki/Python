def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

n = input("Enter the number: ")
num=int (n)
print("Factorial of", num, "is : ", factorial(num))