f=open("file.txt","r")
s=f.read()
print(s)
f.close()

f= open("file1.txt","w")
s=f.write("This is a new file")
f= open("file1.txt","r")
g=f.read()
print(g)
f.close()

#with statement
with open("file.txt","r") as f:
    s=f.read()
    print(s)
 #Read only part of file 
with open("file.txt","r") as f:
    s=f.read(10)
    print(s)
#Read line by line
with open("file.txt","r") as f:
    s=f.readline()
    print(s) 

#Read all lines and store in list
with open("file.txt","r") as f:
    s=f.readlines()
    print(s)
    for line in s:
        print(line)
#Append to a file (to add more content to an existing file)
with open("file.txt","a") as f:
    f.write("\nThis is an appended line")
#To create a new file  
#with open("file2.txt","x") as f:
    #f.write("This is a new file created using x mode")  
#To create a new file or overwrite an existing file
with open("file3.txt","w") as f:
    f.write("This is a new file created using w mode")
#To read and write to a file
with open("file.txt","r+") as f:
    s=f.read()
    print(s)
    f.write("\nThis is a new line added using r+ mode")

#To append and read a file (cursor is at the end of the file)(all previous content is preserved and will read all content)
with open("file.txt","a+") as f:
    f.write("\nThis is a new line added using a+ mode")
    #f.seek(0)  # Move the cursor to the beginning of the file
    s=f.read()
    print(s)
#To read and write to a file (cursor is at the beginning of the file) (all previous content is deleted)
#with open("file.txt","w+") as f:
    #f.write("This is a new line added using w+ mode")
    #f.seek(0)  # Move the cursor to the beginning of the file
    #s=f.read()
    #print(s)  
 #     