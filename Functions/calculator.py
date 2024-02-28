def sum(num1,num2):
    return num1+num2
def multiplication(num1,num2):
    return num1*num2
def subtraction(num1,num2):
    return num1-num2
def division(num1,num2):
    return num1/num2

x=input("Enter the first number: ")
y=input("Enter the second number: ")
print("Addition of numbers: ",sum(int(x),int(y)))
print("Subtraction of numbers: ",subtraction(int(x),int(y)))
print("Multiplication of numbers: ",multiplication(int(x),int(y)))
print("Division of numbers: ",division(int(x),int(y)))