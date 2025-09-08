
for i in range(0,10):
    pass
print(i)  #output 9

#nested loop
for a in range(2,7):
    for b in range(1,a):
        print("#",end="")
        print()
#----------------------------------------------------------------------------------------------------------------------------------------\
for i in range(2,7):
    for b in range(1,i):
        print(b,end="")
        print()\
#-------------------------------------------------------------------------------------------------------------------------------------
for a in range(7,-9,-4):
    print(a,end="")

for i in range(3):
    for j in range(3):
     if j==1:
        break
    print(i,j)