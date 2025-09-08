#for looping (counting loop that repeat a certain number of time)
for a in [1,4,7]:
    print(a)
    print(a*a) #1,1,4,16,7,49

#WAP for table of 5 (range is the fuction range(start,end+1)) ("in"is memebership operator)
n=5
for a in range(1,11):
    print(n*a)

# full table
n=5
for a in range(1,11):
    print(n,"*",a,"=",n*a)

#WAP for sum of five natural number
sum= 0
for a in range(1,6):
    print(a)
    sum=sum+a
    print(sum) 

#string
for ch in "calm":
    print(ch)
#WAP for sum of first 6 natural number
sum=0
for a in range(1,7): 

 sum +=a
print("Sum of first 6 natural number is",sum) #output 21

#--------------------------------------------------------
for a in "abcd":
    print(a,'+')