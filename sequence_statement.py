#if condition 
a=33
b=200
if a>b:
    print("A is greater than B")

#elif condition
a=33
b=200
if a==b:
    print("A is equal to B")
elif a<b:
    print("A is less than B")

#else condition
a=33
b=200
if a==b:
    print("A is equal to B")
else:
    print("A is not equal to B")

#short if condition (one line statement)
a = 2
b = 330
if a > b: print("A is greater than B")
else: print("B is greater than A")

#short if-else condition (one line statement)
a = 2
b = 330
print("A is greater than B") if a > b else print("B is greater than A")

#nested if condition
a = 33
b = 200
if a > b:
    print("A is greater than B")
else:
    if a == b:
        print("A is equal to B")
    else:
        print("A is less than B")
#short nested if condition (one line statement)
a = 2   
b = 330
print("A is greater than B") if a > b else print("A is equal to B") if a == b else print("B is greater than A")
#and or condition
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
