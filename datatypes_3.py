#Dictionary(used to store data vlauees in key:value pairs,ordered,changable,no dupicate)
thisdict={"brand":"ford", "model":"mustang","year":1967}
print(thisdict) #output {'brand': 'ford', 'model': 'mustang', 'year': 1967}

#dictionary items
thisdict={"brand":"ford", "model":"mustang","year":1967}
print(thisdict["brand"]) #output ford

#duplicate value not allowed
thisdict={"brand":"ford", "model":"mustang","year":1967,"year":2020}
print(thisdict) #output {'brand': 'ford', 'model': 'mustang', 'year': 2020}

#dictionary len()
thisdict={"brand":"ford", "model":"mustang","year":1967}
print(len(thisdict)) #output 3

#type()
thisdict={"brand":"ford", "model":"mustang","year":1967}
print(type(thisdict)) #output <class 'dict'>

#accessing dictionary items
thisdict={"brand":"ford", "model":"mustang","year":1967}
x=thisdict["brand"]
print(x) #output ford

#accessing dictionary items using get()
thisdict={"brand":"ford", "model":"mustang","year":1967}
x=thisdict.get("model")
print(x) #output mustang

#accessing dictionary items using keys()
thisdict={"brand":"ford", "model":"mustang","year":1967}
x=thisdict.keys() #returns keys
print(x) #output dict_keys(['brand', 'model', 'year'])

#accessing dictionary items using values()
thisdict={"brand":"ford", "model":"mustang","year":1967}
x=thisdict.values() #returns values
print(x) #output dict_values(['ford', 'mustang', 1967])

#accessing dictionary items using items()
thisdict={"brand":"ford", "model":"mustang","year":1967}
x=thisdict.items() #returns key:value pairs
print(x) #output dict_items([('brand', 'ford'), ('model', 'mustang'), ('year', 1967)])

#Adding items to dictionary
thisdict={"brand":"ford", "model":"mustang","year":1967}
thisdict["color"]="red"
print(thisdict) #output {'brand': 'ford', 'model': 'mustang', 'year': 1967, 'color': 'red'}

#Adding items to dictionary using update()
thisdict={"brand":"ford", "model":"mustang","year":1967}
thisdict.update({"color": "red"})
print(thisdict) #output {'brand': 'ford', 'model': 'mustang', 'year': 1967, 'color': 'red'}

#Adding items OF List to dictionary
thislist=["apple","banana","cherry"]
thisdict={"brand":"ford", "model":"mustang","year":1967}
thisdict.update({"fruits": thislist})
print(thisdict) #output {'brand': 'ford', 'model': 'mustang', 'year': 1967, 'fruits': ['apple', 'banana', 'cherry']}

#changing(updating) value in dictionary
thisdict={"brand":"ford", "model":"mustang","year":1967}
thisdict["year"]=2020
print(thisdict) #output {'brand': 'ford', 'model': 'mustang', 'year': 2020}

#Removing items from dictionary
#using pop() method
thisdict={"brand":"ford", "model":"mustang","year":1967}
thisdict.pop("model")
print(thisdict) #output {'brand': 'ford', 'year': 1967}

#using popitem() method (removes last inserted item)
thisdict={"brand":"ford", "model":"mustang","year":1967}
thisdict.popitem()
print(thisdict) #output {'brand': 'ford', 'model': 'mustang'}

#using del keyword
thisdict={"brand":"ford", "model":"mustang","year":1967}
del thisdict["year"]
print(thisdict) #output {'brand': 'ford', 'model': 'mustang'}

#using clear() method (removes all items)
thisdict={"brand":"ford", "model":"mustang","year":1967}
thisdict.clear()
print(thisdict) #output {}

#using del keyword to delete the dictionary
thisdict={"brand":"ford", "model":"mustang","year":1967}
del thisdict       #deletes the entire dictionary
# print(thisdict) #will give error as dictionary is deleted




