#string
print("Hello, World!")  #output Hello, World!

print("its a string")  #output its a string

#Assigning string to variable
x = "Hello, World!"
print(x)  #output Hello, World!

#string with single quote
x = 'Hello, World!'
print(x)  #output Hello, World!

#string with double quote
x = "Hello, 'World'!"
print(x)  #output Hello, 'World'!

#string with triple quotes
x = """Hello,
 World!"""
print(x) #output Hello, 
# World!

#string with escape character
x = "Hello, \"World\"!"
print(x)  #output Hello, "World"!

#string with backslash
x = "Hello, \\World!"
print(x)  #output Hello, \World!

#string with newline character
x = "Hello,\nWorld!"
print(x)  #output Hello,
# World!

#string with tab character
x = "Hello,\tWorld!"
print(x)  #output Hello,	World!

#string with carriage return
x = "Hello,\rWorld!"
print(x)  #output World! (overwrites Hello,)

#string with backspace
x = "Hello,\bWorld!"
print(x)  #output HellWorld! (removes the 'o')

#slicing string
x = "Hello, World!"
print(x[0:5])  #output Hello (slicing from index 0 to 4)
print(x[7:12])  #output World (slicing from index 7 to 11)

#slicing with negative index
print(x[-6:-1])  #output World (slicing from index -6 to -2)
print(x[-12:-7])  #output Hello (slicing from index -12 to -8)

#slicing with step 
print(x[0:5:2])  #output Hlo (slicing from index 0 to 4 with step 2)

#slicing with step and negative index
print(x[-6:-1:2])  #output Wr (slicing from index -6 to -2 with step 2)

#Modify strings
#uppercase
x = "Hello, World!"
print(x.upper())  #output HELLO, WORLD!
#lowercase
print(x.lower())  #output hello, world!
#strip whitespace
x = "   Hello, World!   "
print(x.strip())  #output Hello, World! (removes leading and trailing whitespace)
#replace substring
print(x.replace("World", "Python"))  #output    Hello, Python!   (replaces 'World' with 'Python')
#split string
print(x.split(","))  #output ['   Hello', ' World!   '] (splits string into a list at the comma)


#concatenation
x1 = "Hello"
x2 = "World"
x3 = x1 + ", " + x2 + "!"  #concatenation
print(x3)  #output Hello, World!

#Escaping characters
x = "Hello, \"World\"!"  #escaping double quotes
print(x)  #output Hello, "World"!

#String Methods
#string length
x= "Hello, World!"
print(len(x))  #output 13 (length of the string)
#capitalize
x = "hello, world!"
print(x.capitalize())  #output Hello, world! (capitalizes the first letter)
#center (length,character)
x= "Hello"
print(x.center(20, '*'))  #output *****Hello***** (centers the string)
#endwith()
x= "Hello, World!"
print(x.endswith("!"))  #output True (checks if the string ends with '!')
#find()
x="hello"
print(x.find("l"))  #output 2 (finds the first occurrence of 'l')
#format()
x= "Hello, {}!"
print(x.format("World"))  #output Hello, World! (formats the string with 'World')
#count()
x= "Hello, World!"
print(x.count("o"))  #output 2 (counts occurrences of 'o')
#index()
x= "Hello, World!"
print(x.index("World"))  #output 7 (finds the index of 'World')










#-------------------------------------------------------------------------------------------------------------------------------------
