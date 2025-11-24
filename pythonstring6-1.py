x = "Khizra"
y = 'Khizra'
print(x)
print(y)
# Single line string
x = "Khizra"
# Multiline string
z = '''Hi, i am Khizra.
I am learning Python.'''
print(z)

# Strings have indexes like arrays
a = "Khizra Zahid"
print(a[1])

# Looping through the string

for x in "Khizra":
  print(x)
# String length
a = "Khizra"
print(len(a))

# Check string 

txt = "I like reading books"
print("books" in txt)

txt = "Such a beautiful day"
print("books" in txt)

# Check string with If for user friendly 
txt = "I like reading books"
if "books" in txt:
  print("Yes , 'books' is present in string")

# Check  If "much" is not present
txt = "I like reading books"
print("day" not in txt)

# print only if "mucher" is not present
txt = "I like reading books"
if "day" not in txt:
  print("No , 'day' is not present in string")