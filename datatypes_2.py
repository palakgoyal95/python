#sets(unordered,unchangable,do not allow dupicate data,uses curly bracket{},no indexing)
thisset={"apple","cherry","watermelon","kiwi"}
print(thisset) #output {'apple', 'cherry', 'watermelon', 'kiwi'}
#sets are unorered so you do not know in which order output will display.

#Duplicate not allowed (will appear single time in output)
thisset={"apple","cherry","watermelon","kiwi","apple"}
print(thisset) #output {'apple', 'cherry', 'watermelon', 'kiwi'}

#value True and 1 are considered same so it will appear one time only also for false,
#false and 0 are considered same in sets so it will also appear one time only.
thisset={1,True,"apple","abc",False}
print(thisset) #output {'apple', 1, 'abc', False}


#len() of the set
print(len(thisset)) #output 4

#set can contain any datatypes and be a mixture of data
thisset={1,True,"apple","abc",False}
print(thisset) #output {'apple', 1, 'abc', False}

#type()
thisset={1,True,"apple","abc",False}
print(type(thisset))  #output <class 'set'>

#accessing set
thisset={"apple","cherry","watermelon","kiwi"}
if "apple" in thisset:
    print("yes") #output yes
else:
    print("no")


print("apple" in thisset) #output True

#Adding items to set (add(),new item will be added only if it is not already present)
thisset={"apple","cherry","watermelon","kiwi"}
thisset.add("orange")
print(thisset) #output {'kiwi', 'cherry', 'watermelon', 'apple', 'orange'}

#upadating set (update(),can add multiple items at once)
thisset={"apple","cherry","watermelon","kiwi"}
thisset.update(["orange", "banana"])
print(thisset) #output {'kiwi', 'cherry', 'watermelon', 'apple', 'orange', 'banana'}

thisset={"apple","cherry","watermelon","kiwi"}
thisset2={"orange", "banana"}
thisset.update(thisset2)
print(thisset) #output {'kiwi', 'cherry', 'watermelon', 'apple', 'orange', 'banana'}

#add any iterable (list, tuple, set) to set
thisset={"apple","cherry","watermelon","kiwi"}
thisset.update(["orange", "banana"], ("grape", "mango"))
print(thisset) #output {'kiwi', 'cherry', 'watermelon', 'apple', 'orange', 'banana', 'grape', 'mango'}


#Removing items from set (remove(),discard(),pop(),clear(),del)
thisset={"apple","cherry","watermelon","kiwi"}
thisset.remove("apple")
print(thisset) #output {'kiwi', 'cherry', 'watermelon'}
thisset={"apple","cherry","watermelon","kiwi"}
thisset.discard("apple")
print(thisset) #output {'kiwi', 'cherry', 'watermelon'}
thisset={"apple","cherry","watermelon","kiwi"}
thisset.pop() #removes a random item
print(thisset) #output {'kiwi', 'cherry', 'watermelon'} (random item removed)
thisset={"apple","cherry","watermelon","kiwi"}
thisset.clear() #removes all items
print(thisset) #output set() (empty set)

#del thisset #deletes the set
# print(thisset) #will give error as set is deleted

#copying set
thisset={"apple","cherry","watermelon","kiwi"}
thisset2=thisset.copy() #copying set
print(thisset2) #output {'kiwi', 'cherry', 'watermelon','apple'}

#Set operations (union, intersection, difference, symmetric difference)
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "kiwi", "orange"}
# Union (combines both sets)
set_union = set1.union(set2)
print(set_union)  # output {'kiwi', 'orange', 'banana', 'cherry', 'apple'}

# Intersection (common items in both sets)
set_intersection = set1.intersection(set2)
print(set_intersection)  # output {'banana'}

# Difference (items in set1 but not in set2)
set_difference = set1.difference(set2)
print(set_difference)  # output {'apple', 'cherry'}

# Symmetric Difference (items in either set1 or set2 but not both)
set_symmetric_difference = set1.symmetric_difference(set2)
print(set_symmetric_difference)  # output {'kiwi', 'orange', 'cherry', 'apple'}

#set symbol
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "kiwi", "orange"}
# Union using | operator
set_union = set1 | set2
print(set_union)  # output {'kiwi', 'orange', 'banana', 'cherry', 'apple'}

# Intersection using & operator
set_intersection = set1 & set2
print(set_intersection)  # output {'banana'}

# Difference using - operator
set_difference = set1 - set2
print(set_difference)  # output {'apple', 'cherry'}

# Symmetric Difference using ^ operator
set_symmetric_difference = set1 ^ set2
print(set_symmetric_difference)  # output {'kiwi', 'orange', 'cherry', 'apple'}

#difference_update() (removes items in set1 that are also in set2)
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "kiwi", "orange"}
set1.difference_update(set2)
print(set1)  # output {'apple', 'cherry'}

#intersection_update() (keeps only items in set1 that are also in set2)
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "kiwi", "orange"}
set1.intersection_update(set2)
print(set1)  # output {'banana'}

#symmetric_difference_update() (keeps only items that are in either set1 or set2 but not both)
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "kiwi", "orange"}
set1.symmetric_difference_update(set2)
print(set1)  # output {'kiwi', 'orange', 'cherry', 'apple'}

#isdisjoint() (checks if two sets have no items in common)
set1 = {"apple", "banana", "cherry"}
set2 = {"kiwi", "orange"}
print(set1.isdisjoint(set2))  # output True (no common items)
set3 = {"banana"}
print(set1.isdisjoint(set3))  # output False (common item 'banana')

#issubset() (checks if set1 is a subset of set2)
set1 = {"apple", "banana"}
set2 = {"banana", "kiwi", "orange", "apple"}
print(set1.issubset(set2))  # output True (all items in set1 are in set2)

#issuperset() (checks if set1 is a superset of set2)
set1 = {"banana", "kiwi", "orange", "apple"}
set2 = {"apple", "banana"}
print(set1.issuperset(set2))  # output True (all items in set2 are in set1)   

#frozenset (immutable set, cannot be changed after creation)
frozen_set = frozenset({"apple", "banana", "cherry"})
print(frozen_set)  # output frozenset({'apple', 'banana', 'cherry'})
# Attempting to add or remove items will raise an error
# frozen_set.add("orange")  # This will raise an AttributeError
# frozen_set.remove("apple")  # This will also raise an AttributeError
#frozenset can be used as a key in a dictionary or an element in another set
#frozenset can be created from any iterable
#frozenset from a list
frozen_set_from_list = frozenset(["apple", "banana", "cherry"])
print(frozen_set_from_list)  # output frozenset({'apple', 'banana', 'cherry'})
#frozenset from a tuple
frozen_set_from_tuple = frozenset(("apple", "banana", "cherry"))
print(frozen_set_from_tuple)  # output frozenset({'apple', 'banana', 'cherry'})
#frozenset from a set
frozen_set_from_set = frozenset({"apple", "banana", "cherry"})
print(frozen_set_from_set)  # output frozenset({'apple', 'banana', 'cherry'})
#frozenset from a string
frozen_set_from_string = frozenset("apple")
print(frozen_set_from_string)  # output frozenset({'a', 'p', 'l', 'e'})






