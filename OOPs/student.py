
#creating class named as students
class Student:
    #constructor to initialize the attributes
    def __init__(self,name,marks):
            self.name=name
            self.marks=marks
    #method to print the data
    def print(self):
        print ("Name: " + self.name)
        print ("Marks: " + "[English,Maths,IQ]= " +str(self.marks))

    #method to calculate average marks
    def  get_avg(self):
          sum=0
          for i in self.marks:
                sum+=i
          print ("Hi "+ self.name,"your Average score is: ",sum/3)

#creating the object of class Student
s1=Student("John",[98,87,79])
s1.print()  
s1.get_avg()
s2=Student("Harry",[67,87,86])
s2.print() 
s2.get_avg()