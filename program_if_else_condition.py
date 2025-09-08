#even number
num=int(input("Enter number:"))
if num % 2 == 0:
    print("The number is even")

#odd number
num=int(input("Enter number:"))
if(num%2!=0):
    print("The number is odd")
    
num=int(input("Enter number:"))
if(num%2==0):
    print("This is the  even no")
else:
    ("This is the odd no") 

#program for eligiblity
age=int(input("Enter your age"))
if(age>=18):
    print("eligible")
else:
    print("Not eligible")  

#program to find largest no from 3 numbers
num1=int(input("Enter 1st no:"))
num2=int(input("Enter 2st no:"))
num3=int(input("Enter 3st no:"))
if(num1 >= num2) and (num1 >=num3):
    print("number 1 is the largest no:",+num1)
elif(num2 >= num1) and (num2 >= num3):
    print("number 2 is the largest no",+num2)
else:
    print("number 3 is the largest no",+num3)

#WAP that takes marks of 3 subjects then calculate its totsl,percentage and display its grades as per given certeria
M1=int(input("Enter marks 1st"))
M2=int(input("Enter marks 2nd"))
M3=int(input("Enter marks 3rd"))
Total=M1 + M2 + M3
Percentage = Total *100/3
if Percentage>=90:
    print("Grade:A")
elif Percentage >=80:
     print("Grade=b")
elif Percentage>=60:
    print("Grade:c")
else:
    print("Grade:D")
    




   