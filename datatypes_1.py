#Data Types
#-------------------------------------------------------------------------------------------------------------------------------------
#Number(Interger(int,bool),Floating Point,Complex)
#Sequence(String,Tuple,list)
#Mapping(dictionary)
#-------------------------------------------------------------------------------------------------------------------------------------
#Number
#Interger(int,boolean)
print(int(3.0)) #output 3
print(bool(0))  #output false
a=6
print(type(a)) #output <class 'int'>
#-------------------------------------------------------------------------------------------------------------------------------------
#Floating point
print(float(5)) #output 5.0
#-----------------------------------------------------------------------------------------------------------------------------------
#complex
x=2+5j
print(x.real, x.imag) #output 2.0 5.0
x=-2-5j
print(x.real, x.imag) #output -2.0 -5.0
#------------------------------------------------------------------------------------------------------------------------------------
#sequence
#string sequence of character(index 0 to.......(forward) -1 to--------------(backward))
name="PYTHON"
print(name[0]) #output p
#--------------------------------------------------------------------------------------------------------------------------------------
#List (uses Square bracket,ordered ,changable,allow duplicate value)
a=[1,2,3,4]
print(a[3])  #output 4
#add

a=[1,2,3,4]
a[4:5]=7,8
print(a)  #output [1, 2, 3, 4, 7, 8]

a=[1,2,3,4,7,8]
a[5:6]=6,8
print(a)  #output [1, 2, 3, 4, 7, 6,8]
a=[1, 2, 3, 4, 7, 6,8]
a[6]=7
print(a[-1]) #output 7
print(a)  #output [1, 2, 3, 4, 7, 6,7]
print(len(a)) #output 7
print(type(a)) #output <class 'list'>

#insert(change list item in specified index)
thislist=["apple","banana","cherry"]
thislist.insert(2,"watermelon")
print(thislist)

#Add list item using append(add in last)
thislist=["apple","banana","cherry"]
thislist.append("orange")
print(thislist) #output ['apple', 'banana', 'cherry', 'orange']

#using Extend method(adding two list)
thislist=["apple","banana","cherry"]
thistuple=["kiwi","watermelon"]
thislist.extend(thistuple)
print(thislist) #output ['apple', 'banana', 'cherry', 'kiwi', 'watermelon']

#Remove item from the list
thislist=["apple","banana","cherry"]
thislist.remove("apple")
print(thislist) #output ['banana', 'cherry']

#pop item from specified index
fruit=["apple","banana","cherry","Watermelon","kiwi"]
fruit.pop(2)
print(fruit) #output ['apple', 'banana', 'Watermelon', 'kiwi']

#Sort list(case sensitive)
fruit=["apple","banana","cherry","Watermelon","kiwi"]
fruit.sort()
print(fruit) #output ['Watermelon', 'apple', 'banana', 'cherry', 'kiwi']
fruit.sort(reverse= True) #descending order
print(fruit) #output ['kiwi', 'cherry', 'banana', 'apple', 'Watermelon']

#case insensitive
fruit=["apple","banana","cherry","Watermelon","kiwi"]
fruit.sort(key= str.lower)
print(fruit) #output ['apple', 'banana', 'cherry', 'kiwi', 'Watermelon']

#Reverse order
fruit=['apple', 'banana', 'cherry', 'kiwi', 'Watermelon']
fruit.reverse()
print(fruit) #output ['Watermelon', 'kiwi', 'cherry', 'banana', 'apple']

#index list.index(element,start,end)
fruit=['apple', 'banana', 'Watermelon', 'kiwi']
fruit.index("apple") #output 0

fruit=['apple', 'banana', 'Watermelon',"apple", 'kiwi']
print(fruit.index("apple",2)) #output 3

#count list.count(value)
fruit=['apple', 'banana', 'Watermelon', 'kiwi',"apple","apple"]
print(fruit.count("apple")) #output 3

#copy list.copy()
fruit=['apple', 'banana', 'Watermelon', 'kiwi']
fruit.copy()
print(fruit) #output ['apple', 'banana', 'Watermelon', 'kiwi']

#clear  list.clear()
fruit=['apple', 'banana', 'Watermelon', 'kiwi']
fruit.clear()
print(fruit) #output []

#----------------------------------------------------------------------------------------------------------------------------------
#Tuples(uses parantheses braket(),ordered unchangable,Allow duplicates,if there is commas then only it is tuple)

thistuple=("apple","banana","cherry","watermelon") 
print(thistuple) #output ("apple","banana","cherry","watermelon") 

thistuple=("apple") #this is not a tuple

thistuple=("apple",) #this is a tuple

#Datatypes in tuple (can hold differnt types of data)

tuple1=("A","B","C","D","E")
tuple2=(1,3,4,5,6)
tuple3=(True,False,True,False)
tuple4=("abc",True,1,40,"cherry")
print(type(tuple1))
print(tuple2)
print(tuple3)

#Access of tuples can done using index no inside square bracket
print(tuple1[2])
print(tuple4[-4])
print(tuple2[1:3])
print(tuple2[1:])
print(tuple2[:3])
print(tuple2[-1:-3])

#check if item exit or not
tuple1=("A","B","C","D","E")
if "A" in tuple1:
    print("yes")

#update tuples (as said tuples are unchanglable to update convert tuples into list,upadate exiting item)
tuple1=("A","B","C","D","E")
tup=list(tuple1)
tup[3]="k"
tuple1=tuple(tup)
print(tuple1)

#append(by coverting into list,adding new item)
thistuple=("palak","gaurav","pallii","laddo")
thistuple1=list(thistuple)
thistuple1.append("pallu")
thistuple=tuple(thistuple1)
print(thistuple)

#remove item form tuple by converting into list
thistuple=("palak","gaurav","pallii","laddo","pallu")
thistuple1=list(thistuple)
thistuple1.remove("pallu")
thistuple=tuple(thistuple1)
print(thistuple)

#adding tuple to tuple
thistuple=("palak","gaurav","pallii","laddo","pallu")
thistuple1=("GG",)
thistuple+=thistuple1
print(thistuple)
 
# To delete complete tuple use del
thistuple=("palak","gaurav","pallii","laddo","pallu")
del thistuple
#print(thistuple) #show error

#unpacking the tuple(when we create tuple,we normally assign values to it.this is called packing a tuple. 
#but in python we are also allowed to extracte the vaules back into the variables this is called unpacking)
fruits=("apple","banana","cherry")
(green,yellow,red)=fruits
print(green) #output apple
print(yellow) #output banana
print(red) #output cherry

#NOTE-THE NUMBER OF VARIABLES MUST MATCH THE NUMMBER OF VALUES OF TUPLES
#IF NOT,YOU MUST USE ASTERISK TO COLLECT THE REMSINING VALUES AS A LIST
fruits=("apple","banana","cherry","watermelon")
(green,yellow,*red)=fruits
print(green) #output apple
print(yellow) #output banana
print(red) #output ['cherry','watermelon']\

#find length of tuples using len()
print(len(fruits)) #OUTPUT 4

#join tuples using adition,multiply
tuple1=(1,2,3)
tuple2=(4,5,6)
tuple3=tuple1+tuple2
print(tuple3) #output (1, 2, 3, 4, 5, 6)

tuple1=(1,2,3)
tuple3=tuple1*2
print(tuple3) #output (1, 2, 3, 1, 2, 3)

#Mthod(count(),index())
tuple1=(1,2,3,4,5,6,7,8,9)
print(tuple1.index(2)) #output 1

tuple1=(1,2,3,4,5,6,7,8,9,2,4,2,5)
print(tuple1.count(2)) #output 3










