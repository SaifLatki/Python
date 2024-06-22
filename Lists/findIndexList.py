

list=[1,2,3,4,5,6,7,8,9,10]
x=int(input("Enter the numbr you want to serach of list :"))
ind=0
for val in list:
    if(val==x):
        print (" x is found at  ",ind)
    ind +=1
