x = ("pizza" , "pudding" , "coffee" , "tea")
print(type(x))

# Tuple length

x = ("pizza" , "pudding" , "coffee" , "tea")
print(len(x))

# Create tuple with one item

x = ("Khizra",)
print(type(x))

# Not a tuple 

x = ("Khizra") # Its read as a string
print(type(x))

# tuple items - data types (str , int , boolean)

x = ("pizza" , "pudding" , "coffee" , "tea")
y = (1 , 2 , 4 , 9 , 10)
z = (True , False , True)
print(x)
print(y)
print(z)

# tuples can also contains different datatypes
 
x = ("pizza" , 12 , True , 20 , "tea" , False)
print(x)

# The tuple constructor 
x = tuple(("pizza" , "pudding" , "coffee" , "tea"))
print(x)
print(type(x))

# Access tuples items 
x = ("pizza" , "pudding" , "coffee" , "tea")
print(x[3])

# access tuples item through negative indexing 

x = ("pizza" , "pudding" , "coffee" , "tea")
print(x[-1])

# access tuples item through range of indexes

x = ("pizza" , "pudding" , "coffee" , "tea" , "Khizra" , "zahid" , "cats" , "pandas" , "dogs")
print(x[2:7]) # last item not included

# access tuples item through range of indexes but some index not included

x = ("pizza" , "pudding" , "coffee" , "tea" , "Khizra" , "zahid" , "cats" , "pandas" , "dogs")
print(x[:8])

x = ("pizza" , "pudding" , "coffee" , "tea" , "Khizra" , "zahid" , "cats" , "pandas" , "dogs")
print(x[1:])

# access tuples item through negative range of indexes

x = ("pizza" , "pudding" , "coffee" , "tea" , "Khizra" , "zahid" , "cats" , "pandas" , "dogs")
print(x[-5:-1]) # -1 is not included as positive indexing

# check if the item exits 
x = ("pizza" , "pudding" , "coffee" , "tea" , "Khizra" , "zahid" , "cats" , "pandas" , "dogs")
if "pandas" in x:
    print("yes ,'pandas' is in x")

# Changing in tuple values (* 007)
x = ("pizza" , "pudding" , "coffee" , "tea" , "Khizra" , "zahid" , "cats" , "pandas" , "dogs")
print(type(x))
y = list(x)
print(type(y))
y[3] = "Khizra-student"
x = tuple(y)
print(x)
print(type(x))

# Add items in tuple values (* 007)

x = ("pizza" , "pudding" , "coffee" , "tea" , "Khizra" , "zahid" , "cats" , "pandas" , "dogs")
print(type(x))
y = list(x)
print(type(y))
y.append("Khizraatlast")
x = tuple(y)
print(x)

# Adding tuple to a tuple
x = ("pizza" , "pudding" , "coffee" , "tea")
y = ("Khizrastudent",)
x += y
print(x)

# Removing items from a tuples 

x = ("pizza" , "pudding" , "coffee" , "tea" , "Khizra" , "zahid" , "cats" , "pandas" , "dogs")
print(type(x))
y = list(x)
print(type(y))
y.remove("dogs")
x = tuple(y)
print(x)
print(type(x))

# how to delete tuple 
x = ("pizza" , "pudding" , "coffee" , "tea" , "Khizra" , "zahid" , "cats" , "pandas" , "dogs")
del x 

# Packing a tuple (when we assign a value to tuple)
x = ("Khizra" , "zahid" , "Khizra" , "result")

# Unpacking a tuple (when we extract a value from tuple)
x = ("Khizra" , "zahid" , "Khizra" , "result")
(a , b , *c) = x
print(a)
print(b)
print(c)