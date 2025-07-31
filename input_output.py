#Simple Input Output Functions

#input()-This function is used to get simple input from the user(always return a value in string type)
name=input("enter your name:")
print(name)
#--------------------------------------------------------------------------------------------------------------------------------
#output through print()
print(5*2) #output 10
print("hello") #output hello
#-----------------------------------------------------------------------------------------------------------------------------
#Program to add two numbers
a=int(input("Enter 1st no:"))
print(a)
b=int(input("Enter 2nd no:"))
print(b)
c=a+b
print("sum of two number:", c)
#------------------------------------------------------------------------------------------------------------------------------------
#Program to multiply and subtract
a=int(input("Enter 1st no:"))
print(a)
b=int(input("Enter 2nd no:"))
print(b)
c=a*b
print("Multiply is:", c)
d=a-b
print("subtraction is:",d)
#---------------------------------------------------------------------------------------------------------------------------------
#program of addtion in float no
a=float(input("Enter 1st no:"))
print(a)
b=float(input("Enter 2nd no:"))
print(b)
c=a+b
print("sum of two number:", c)
#-----------------------------------------------------------------------------------------------------------------------------------
#progarm to calculate simple interest and compound interest
P=int(input("Enter Principle:"))
print(a)
R=int(input("Enter Rate:"))
print(b)
T=int(input("Enter time:"))
SI=(P*R*T)/100
print("Simple Interest:", SI)
CI= P-SI
print("Compound Interest:",CI)
#-----------------------------------------------------------------------------------------------------------------------------------
