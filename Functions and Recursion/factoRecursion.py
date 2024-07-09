def fact_recursion(n):
    if(n==1 or n==0):
        return 1

 
    return fact_recursion(n-1)*n
    print(n)

print(fact_recursion(6))