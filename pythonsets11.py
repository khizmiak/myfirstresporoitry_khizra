x = {"dogs" , "cats" , "lions" , "parrot"}
print(x)

# Duplicate not allowed 
x = {"a" , "b" , "c" , "c" , "a"}
print(x)

# get the lenght of sets
x = {"dogs" , "cats" , "lions" , "parrot"}
print(len(x))

# Check the data type of sets 
set1 = {"a" , "b" , "c"}
set2 = {1 , 4 , 7 , 9}
set3  = {True , False , True}
print(set1)
print(set2)
print(set3)
print(type(set1))
print(type(set2))
print(type(set3))

# A set with string , integer and Boolean means all data types 
set1 = {4 , "parrot" , 2.5 , True , True}
print(set1)

# The set Constructor
conset = set((4 , "parrot" , 2.5 , True , True))
print(conset)

# How to access items in sets 
accset = {"a" , "b" ,"c"}
for i in accset:
    print(i)

# Check if "cats" is present in set or not

x = {"dogs" , "cats" , "lions" , "parrot"}
print("cats" in x)

# Adding set items
x = {"dogs" , "cats" , "lions" , "parrot"}
x.add("snake")
print(x)

# How to add items from another set into the current set by update()methode
x = {"dogs" , "cats" , "lions" , "parrot"}
y = {"a" , "b" ,"c"}
x.update(y)
print(x)

# Removing set items
x = {"dogs" , "cats" , "lions" , "parrot"}
x.remove("lions")
print(x)

# discard() set items
x = {"dogs" , "cats" , "lions" , "parrot"}
x.discard("lions")
print(x)

# remove the last item by using pop() method will raise the error or you will get the wrong output 
x = {"dogs" , "cats" , "lions" , "parrot"}
y = x.pop()
print(y)
print(x)

# Clear() method is used for empty the set

x = {"dogs" , "cats" , "lions" , "parrot"}
x.clear()
print(x)

# Del keyword is used to delete the set completely
x = {"dogs" , "cats" , "lions" , "parrot"}
del x

# How to use loop in sets
x = {"dogs" , "cats" , "lions" , "parrot"}
for i in x:
    print(i)

# Joining two sets by union() and update()

x = {"dogs" , "cats" , "lions" , "parrot"}
y = {1 , 2 , 4 , 9 , 10}
z = x.union(y)
print(z)

# update() using

x = {"dogs" , "cats" , "lions" , "parrot"}
y = {1 , 2 , 4 , 9 , 10}
x.update(y)
print(x)

# Use intersection which allow duplicate value
x = {"dogs" , "cats" , "lions" , "parrot"}
y = {"dogs" , "cats" , "lions" }
x.intersection_update(y)
print(x)

x = {"dogs" , "cats" , "lions" , "parrot"}
y = {"dogs" , "cats" , "lions" }
z = x.intersection(y)
print(z)

# keep all , but not the duplicate or common value

x = {"dogs" , "cats" , "lions" , "parrot"}
y = {"dogs" , "cats" , "lions" }
x.symmetric_difference_update(y)
print(x)

# Symmetric_difference() method eill return a new set that contain only the element that are not present in Both sets

x = {"dogs" , "cats" , "lions" , "parrot"}
y = {"dogs" , "cats" , "lions" }
z = x.symmetric_difference(y)
print(z)