# Indexing are included : 1st object replaces 0 index
x = ["Muffin" , "pumpkin" , "Cats"]
print(x)

# Duplicate values

x = ["Muffin" , "pumpkin" , "Cats" , "Cats"]
print(x)

# List length 
x = ["Muffin" , "pumpkin" , "Cats" , "Cats"]
print(len(x))

# List items - Data types
x = ["a" ,"b","c"]
y = [1,4,6,7,9]
z = [True , False , True]
print(x)
print(y)
print(z)
# A List with string ,int and boolean

a = ["khizra" , 5 , True , 10 ,"zahid"]
print(a)

# Data types for lists
a = ["khizra" , 5 , True , 10 ,"zahid"]
print(type(a))

# List[] Constructor

a = list(("khizra" , 5 , True , 10 ,"zahid"))
print(a) 

# How to access items
x = ["Muffin" , "pumpkin" , "Cats"]
print(x[2])

# Range of indexes
x = ["Muffin" , "pumpkin" , "Cats" , "dogs" , "plum" , "sting" , "rings"]
print(x[2:5])

# Negative indexing 
x = ["Muffin" , "pumpkin" , "Cats" , "dogs" , "plum" , "sting" , "rings"]
print(x[-6:-1])

# Leaving out the start values 

x = ["Muffin" , "pumpkin" , "Cats" , "dogs" , "plum" , "sting" , "rings"]
print(x[:4])

# Leaving out the End values 
x = ["Muffin" , "pumpkin" , "Cats" , "dogs" , "plum" , "sting" , "rings"]
print(x[1:])

# How to check if the item Exists in Lists
x = ["Muffin" , "pumpkin" , "Cats" , "dogs" , "plum" , "sting" , "rings"]
if "pumpkin" in x:
    print("yes , 'pumpkin' is in the list")

# Change the item value of the list
x = ["Muffin" , "pumpkin" , "Cats" , "dogs" , "plum" , "sting" , "rings"]
x[0] = "cake"
print(x)

# Change a Range of item values in lists
x = ["Muffin" , "pumpkin" , "Cats" , "dogs" , "plum" , "sting" , "rings"]
x[1:4] = ["plum" , "sting" , "rings"]
print(x)

# Change of one value by replacing it with 2 values
x = ["Muffin" , "pumpkin" , "Cats" , "dogs" , "plum" , "sting" , "rings"]
x[1:2] = ["Hamming","Elephant"]
print(x)
print(len(x))

# Change of two value by replacing it with 1 values
x = ["Muffin" , "pumpkin" , "Cats" , "dogs" , "plum" , "sting" , "rings"]
x[1:3] = ["Cherry"]
print(x)
print(len(x))

