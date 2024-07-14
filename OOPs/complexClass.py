class Complex:
    
    def __init__(self,r,i): 
        self.r=r
        self.i=i

    def showNumber(self):
        print(self.r,"i + ",self.i,"j")

    #dunder function (addition) for complex numbers
    def __add__(self,num):
        realNew=self.r+num.r
        imgNew=self.i+num.i

        return Complex(realNew,imgNew)
    
     #dunder function (Subtraction) for complex numbers
    def __sub__(self,num):
        realNew=self.r-num.r
        imgNew=self.i-num.i

        return Complex(realNew,imgNew)
    

num1=Complex(1,3)
num1.showNumber()
num2=Complex(2,5)
num2.showNumber()

#additon call 
#operator overloading
num3=num1+num2
num3.showNumber()

#Subtraction call
#operator overloading 
num4=num1-num2
num4.showNumber()