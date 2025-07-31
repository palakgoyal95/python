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









