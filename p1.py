print("HELLO WORLD!")
import sys
print(sys.version)

if 5>2:
    print("Five is greater than two!")
    
#this is a comment

#Python does not really have a syntax for multiline comments.
#To add a multiline comment you could insert a # for each line:
#Or, not quite as intended, you can use a multiline string.

""""
Since Python will ignore string literals that are not assigned to a variable, 
you can add a multiline string (triple quotes) in your code, 
and place your comment inside it:
"""
'''hiii
hello
hii
'''
#Variables

#Variables are containers for storing data values.
x=5
y="Hello, World!"
print(x)
print(y)
x="mishree"#  is same as 'mishree'
print(x)
#Casting
x=str(3)#x will be '3'
y=int(3)#y will be 3
z=float(3)#z will be 3.0
print(type(x))
print(type(y))
print(type(z))
#case sensitive
a=4
A="Sally"
#A will not overwrite a
print(a)
print(A)
""" variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords"""

#camel case myVariableName
#Pascal Case MyVariableName
#Snake Case my_variable_name

# carname="Volvo"  

#many values to multiple variables
x,y,z="Orange","Banana","Cherry"
print(x)
print(y)
print(z)

#One value to multiple variables
x=y=z="Orange"
print(x)
print(y)
print(z)

#Unpack a collection
fruits=["apple","banana","cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)

#output variables
x="python is awesome"
print(x)
x="python"
y="is"
z="awesome"
print(x,y,z)
print(x+y+z)#gape will not be there in btw the words

x=5
y=10
print(x+y)
a="5"
b="10"
print(a+b)
m=24
n="mishree"
#print(m+n) error will be generated.
print(m,n)

#global variables
#variables that are created outside of a function (as in all of the examples above) are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.
x="awesome"
def myfunc():
    print("Python is "+x)
myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

x="awesome"
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#built-in data types
#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview
#none type:NoneType
"""Example	Data Type	Try it
x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType	
"""
#int
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#float
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#float
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#complex
x=3+5j
y=5j
z=-5j
print(type(x))
print(type(y))
print(type(z))

#type conversion
x=1
y=2.8
z=1j
a=float(x)
b=int(y)
c=complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
#you cannot convert complex numbers into another number type.

#random number
import random
print(random.rand(1,10))#display a number between 1 to 9

#casting
x=int(1)
y=str(2.8)
z=float("3")
print(x)
print(y)
print(z)

#quotes inside quotes
print("it's alright.")
print('he is called as "JOHNNY"')

#multiline string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


'''Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.'''

a="hello,world"
print(a[1])

#looping through a string
for x in "banana":
  print(x)
'''
b
a
n
a
n
a
'''

#string length
a="hello,world"
print(len(a))#11

#check the sting.if a certain pharse or characer is present in a string,use keyword in.
txt="the best thing in life are free!"
print("free" in txt)#return True

if "free" in txt:
  print("YES")

print("expensive" not in txt)#return True

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
  
#slicing string
'''You can return a  of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.'''
b= "Hello, World!"
print(b[2:5])#llo
#Hello
#llo, World!
#orl
print(b[:5])
print(b[2:])
print(b[-5:-2])

#modify string
#upper case
a = "Hello, World!"
print(a.upper())
#lower case
print(a.lower())
#remove whitespace
print(a.strip())
#replace string
print(a.replace("H", "J"))
#split string
print(a.split(","))

#string concatenation
a = "Hello"
b = "World"
c = a + b
print(c)
c = a + " " + b
print(c)

#string format
"""age = 36
txt = "My name is John, I am " + age
print(txt)
error will be generated"""
age=36
txt=f"my name is john,i am {age}"
print(txt)
"""Placeholders and Modifiers
A placeholder can contain variables, operations, functions, and modifiers to format the value.
A placeholder can include a modifier to format the value.
A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:"""
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
#perform math operation
txt = f"The price is {20 * 59} dollars"
print(txt)

#escape character
"""To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
An example of an illegal character is a double quote inside a string that is surrounded by double quotes:"""

txt = "We are the so-called \"Vikings\" from the north."
print(txt)
"""
Code	Result	Try it"""
#\'	Single Quote	
#\\	Backslash	
#\n	New Line	
#\r	Carriage Return	
#\t	Tab	
#\f	Form Feed	
#\ooo	Octal value	
#\xhh	Hex value"""

#string method
"""Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""

#python booleans
print(10 > 9)
print(10 == 9)
print(10 < 9)
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15))
"""false vale
print(bool(False))
print(bool(None))
bool(0)
bool("")
bool(())
bool([])
bool({})
"""

"""One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or Fals"""
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  
x = 200
print(isinstance(x, int))

#python operator
print(10+5)

"""Operator	Name	Example	Try it
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y"""

x = 2
y = 5

print(x ** y) #same as 2*2*2*2*2

x = 15
y = 2

print(x // y)

#the floor division // rounds the result down to the nearest whole number
"""Operator	Example	Same As	Try it
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
:=	print(x := 3)	x = 3
print(x)	
"""

# Using x = 5 for all examples initially
x = 5
print("Initial value:", x)

x = 5
x += 3
print("x += 3:", x)  # Output: 8

x = 5
x -= 3
print("x -= 3:", x)  # Output: 2

x = 5
x *= 3
print("x *= 3:", x)  # Output: 15

x = 5
x /= 3
print("x /= 3:", x)  # Output: 1.6666666666666667 (float division)

x = 5
x %= 3
print("x %= 3:", x)  # Output: 2 (remainder of 5 / 3)

x = 5
x //= 3
print("x //= 3:", x)  # Output: 1 (floor division)

x = 5
x **= 3
print("x **= 3:", x)  # Output: 125 (5 to the power of 3)

x = 5
x &= 3
print("x &= 3:", x)  # Output: 1 (bitwise AND: 5 (101) & 3 (011) = 001)

x = 5
x |= 3
print("x |= 3:", x)  # Output: 7 (bitwise OR: 5 (101) | 3 (011) = 111)

x = 5
x ^= 3
print("x ^= 3:", x)  # Output: 6 (bitwise XOR: 5 (101) ^ 3 (011) = 110)

x = 5
x >>= 3
print("x >>= 3:", x)  # Output: 0 (right shift 5 by 3 bits: 000000101 >> 3 = 000)

x = 5
x <<= 3
print("x <<= 3:", x)  # Output: 40 (left shift 5 by 3 bits: 000000101 << 3 = 101000)

# Using walrus operator (:=)
print("Walrus operator:", x := 3)  # Output: 3 (assigns 3 to x and prints it)
print("Value of x:", x)            # Output: 3 (x is now 3)

#python lists
thislist=["apple","banana","cherry"]
#list,tupple,set,dictionary

#list
thislist=["apple","banana","cherry"]
print(thislist)
#list items are ordered,changeable and allow duplicate values.
#list items are indexed,start from 0
#the list() constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
"""Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["blackcurrant","watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#to add an item to the end of the list, use the append() method
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#extend() method to add elements from another list to the current list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#remove() method removes the specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#pop() method removes the specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
3

#IF you do not specify the index, the pop() method removes the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#del keyword removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#del keyword can also delete the list completely
thislist = ["apple", "banana", "cherry"]
del thislist

#clear() method empties the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
"""
apple
banana
cherry
"""

#loop through the index numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
"""
apple
banana
cherry
"""
#using a while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
"""
apple
banana
cherry
"""
#looping using list comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
"""
apple
banana
cherry
"""
#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"] 
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#using list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

iterable = [1, 2, 3, 4, 5]
condition = lambda x: x % 2 == 0
expression = lambda x: x * 2
newlist = [expression(item) for item in iterable if condition(item)]
print(newlist)

newlist=[x for x in fruits if x!="apple"]
print(newlist)
"""
['banana', 'cherry', 'kiwi', 'mango']"""
newlist=[x for x in fruits]
print(newlist)
"""
['apple', 'banana', 'cherry', 'kiwi', 'mango']"""
newlist=[x for x in range(10)]
print(newlist)
"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"""
newlist=[x for x in range(10) if x<5]
print(newlist)
"""
[0, 1, 2, 3, 4]"""
newlist=[x.upper() for x in fruits]
print(newlist)
"""
['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']"""
newlist=["hello" for x in fruits]
print(newlist)
"""
['HELLO', 'HELLO', 'HELLO', 'HELLO', 'HELLO']
"""

#return orange instead of banana
newlist=["orange" if x=="banana" else x for x in fruits]
print(newlist)
"""
['apple', 'orange', 'cherry', 'kiwi', 'mango']
"""

newlist=[x if x!="banana" else "orange" for x in fruits]
print(newlist)
"""
['apple', 'orange', 'cherry', 'kiwi', 'mango']
"""

#sort list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
"""
['banana', 'kiwi', 'mango', 'orange', 'pineapple']
"""
#sort list numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
"""
[23, 50, 65, 82, 100]
"""
#sort descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
"""
['pineapple', 'orange', 'mango', 'kiwi', 'banana']
"""

#customize sort function
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
"""
[50, 65, 23, 82, 100]
"""
#case insensitive sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
"""
['Kiwi', 'Orange', 'banana', 'cherry']
"""

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
"""
['banana', 'cherry', 'Kiwi', 'Orange']
"""

#reverse the order of the list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
"""
['cherry', 'Kiwi', 'Orange', 'banana']
"""

#copy a list
"""You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2."""

#make a copy of a list with the copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#make a copy of a list with the list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
"""
['apple', 'banana', 'cherry']
"""

#use slice operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
"""
['apple', 'banana', 'cherry']
"""

#join two list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
"""
['a', 'b', 'c', 1, 2, 3]
"""

#append list2 into list1
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)
"""
['a', 'b', 'c', 1, 2, 3]
"""

#use extend() method to add list2 at the end of list1
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
"""
['a', 'b', 'c', 1, 2, 3]
"""

"""List Methods
Python has a set of built-in methods that you can use on lists.
Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""

#python tuples
#python tuples
#python tuples
#python tuples
#python tuples

#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
thistuple=("apple","banana","cherry")
print(thistuple)
#tuple items are ordered,unchangeable and allow duplicate values.
#tuple items are indexed,start from 0

#create tuple with one item
thistuple=("apple",)
print(type(thistuple))
#NOT a tuple
thistuple=("apple")
print(type(thistuple))
"""
<class 'tuple'>
<class 'str'>
"""

#tuple items can be of any data type
thistuple=("apple","banana","cherry",1,2,3)
print(thistuple)
"""
('apple', 'banana', 'cherry', 1, 2, 3)
"""
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
"""
('apple', 'banana', 'cherry')
(1, 5, 7, 9, 3)
(True, False, False)
('abc', 34, True,40,'male')
"""

#tuple() constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
"""
('apple', 'banana', 'cherry')
"""

#access tuple items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
"""
banana
"""

#check of item exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
"""
Yes, 'apple' is in the fruits tuple
"""
#Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
#But there are some workarounds.
#change tuple values
#convert the tuple into a list to be able to change it
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
"""
('apple', 'kiwi', 'cherry')
"""
#add items
#convert the tuple into a list, add the item, and convert it back into a tuple
x = ("apple", "banana", "cherry")
y = list(x)
y.append("orange")
x = tuple(y)
print(x)
"""
('apple', 'banana', 'cherry', 'orange')
"""
#add atuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
"""
('apple', 'banana', 'cherry', 'orange')
"""
#remove items
#convert the tuple into a list, remove the item, and convert it back into a tuple
x = ("apple", "banana", "cherry")
y = list(x)
y.remove("apple")
x = tuple(y)
print(x)
"""
('banana', 'cherry')
"""

#del keyword can delete the tuple completely
"""thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)""" #this will raise an error because the tuple no longer exists

#in,python we are also allowed to extract the values back into variables.this is called unpacking.
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
"""
apple
banana
cherry
"""

#using asterisk
#if the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
"""
apple
banana
['cherry', 'strawberry', 'raspberry']
"""

#loop through a tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
"""
apple
banana
cherry
"""

#join two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
"""
('a', 'b', 'c', 1, 2, 3)
"""
#multiply tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
"""
('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
"""

'''SET
A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
set items are unordered, unchangeable, and do not allow duplicate values.'''
thisset = {"apple", "banana", "cherry"}
print(thisset)

"""True and 1 both are same considered
and False and 0 both are same considered"""

#set() constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#access items
'''
You cannot access items in a set by referring to an index or a key, since sets are unordered the items has no index.
But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
'''
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
"""
apple
banana
cherry
"""

#check if item exists
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
"""
True
"""

#change items
"""Once a set is created, you cannot change its items, but you can add new items."""
#add items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
"""
{'apple', 'banana', 'cherry', 'orange'}
"""

#update() method to add multiple items
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)
"""
{'apple', 'banana', 'cherry', 'mango', 'grapes', 'orange'}
"""
#you can not use insert method in set
#remove items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
"""
{'apple', 'cherry'}
"""
#discard() method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
"""
{'apple', 'cherry'}
"""
#pop() method
#sets are unordered, so when using the pop() method, you will not know which item that gets removed.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
"""
banana
{'apple', 'cherry'}
"""
#clear() method
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
"""
set()
"""
#del keyword
thisset = {"apple", "banana", "cherry"}
del thisset
#print(thisset) #this will raise an error because the set no longer exists

#loop set
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
"""
apple
banana
cherry
"""

#join two sets
"""
union() and update() will exclude any duplicate items.
The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.

"""

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

#join multiple sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
myset = set1 | set2 | set3 |set4
print(myset)

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

#update
#insert all items from one set to another.
#it changes the orignal set and does not return a new set.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
"""
{1, 2, 'c', 3, 'b', 'a'}"""

#intersection
set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set3=set1.intersection(set2)
print(set3)

#use & instead of intersection
set3=set1 & set2
print(set3)

"""The intersection_update() method will also keep ONLY the duplicates, 
but it will change the original set instead of returning a new set."""
set1.intersection_update(set2)
print(set1)
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

#difference() method will return a new set that will contain only the items from the first set that are not present in other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)
#use - instead of difference
set3 = set1 - set2
print(set3)

#symmetric difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
 
print(set3)

set3 = set1 ^ set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)


"""
Method	Shortcut	Description
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns whether another set contains this set or not
 	<	Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others
"""


#python dictionaries
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["brand"])

#duplicate not allowed last one will be printed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#it can have all types of data items
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#the dict() constructor
thisdict=dict(name="mishree",age="19",country="india")

#accessing items using keyword from dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
x = thisdict.get("model")
print(x)
x=thisdict.keys()
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

#get items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x)
'''
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
items() method will return each item in a dictionary, as tuples in a list.'''

#check if key exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
'''
Yes, 'model' is one of the keys in the thisdict dictionary
'''
#chNGE VALUES
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
'''
{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
'''
#update dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)
'''
{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
'''

#adding items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
'''
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
'''
#update dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)
'''
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
'''

#remove items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model") #remove item with key name
print(thisdict)
'''
{'brand': 'Ford', 'year': 1964}
'''
#popitem() method removes the last inserted item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
'''
{'brand': 'Ford', 'model': 'Mustang'}
'''

#del keyword removes the item with the specified key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
'''
{'brand': 'Ford', 'year': 1964}
'''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#del keyword can also delete the dictionary completely
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
#print(thisdict) #this will raise an error because the dictionary no longer exists

#clear() method empties the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
'''
{}
'''

#loop through a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
for x in thisdict:
  print(thisdict[x])#print all values
for x in thisdict.values():
  print(x)
for x in thisdict.keys():
  print(x)
for x, y in thisdict.items():
  print(x, y)
  
#copy dictionaries
"""you can not copy a dictionary by simply typing dict2=dict1
because:dict2 will only be a reference to dict1,ND CHANGES MADE IN
dict1 will automatically also be made in dict2"""
thisdict = {
  "brand":"Ford",
  "model":"Mustang",
  "year":1964,
}
mydict=thisdict.copy()
print(mydict)

mydict=dict(thisdict)
print(mydict)

#doctonariy acn contain dictionaries,this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#access items in nested dictionaries
print(myfamily["child2"]["name"])

#loop through nested dictionaries
for x,obj in myfamily.items():
  print(x)

  for y in obj:
    print(y+':',obj[y])
"""Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary"""


#if-else
"""Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b"""

a=33
b=200
if b>a:
  print("b is greater than a")
elif a==b:
  print("a and b are equal")
else:
  print("a iis less than b")

#short hand if(ternary operator/conditional)
if a>b:print("a is greater than b")

#short hand is else
a=2
b=330
print("A") if a>b else print("B")

#one line if else
a=330
b=330
print("a") if a >b else print("=") if a==b else print("b")

#and
a=200
b=33
c=500
if a>b and c>a:
  print("print both conditions are true")
  
#or
if a>b or a>c:
  print("at least one of the combination is true")
  
#not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
  
#nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
#pass statement
"""if statements cannot be empty, but if you for some reason have an if statement with 
no content, put in the pass statement to avoid getting an error."""
a = 33
b = 200

if b > a:
  pass
#while loop
i=1
while i<6:
  print(i)
  i+=1  
  
#break statement
i=1
while i<6:
  print(i)
  if i==3:
    break
  i+=1

#continue statement
i=0
while i<6:
  i+=1
  if i==3:
    continue
  print(i)
#stop the current iteration and continue with the next                       

#else(statement)
i=1
while i<6:
  print(i)
  i+=1
else:
  print("i is no longer less than 6")

#python for loops
fruits=["apple","banana","cherry"]
for x in fruits:
  print(x)

#loop through a string
for x in "banana":
  print(x)
  
#break statement
fruits=["apple","banana","cherry"]
for x in fruits:
  print(x)
  if x=="banana":
    break
  
#exit the loop when x is banana, but this time the break comes before the print
fruits=["apple","banana","cherry"]
for x in fruits:
  if x=="banana":
    break
  print(x)
  
#continue statement
fruits=["apple","banana","cherry"]
for x in fruits:
  if x=="banana":
    continue
  print(x)
  
#range() function
for x in range(6):
  print(x)
#range function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(2,6):
  print(x)
  
  #increment the sequence with 3 (default is 1)
for x in range(2,30,3):
  print(x)
#increment the sequence with 3 (default is 1)

#else in for loop
for x in range(6):
  print(x)
else:
  print("finally finished")
#the else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
  if x==3:break
  print(x)
else:
  print("finally finished")
  
#nested loops
adj=["red","big","tasty"]
fruits=["apple","banana","cherry"]
for x in adj:
  for y in fruits:
    print(x,y)
  
#pass statement
for x in [0,1,2]:
  pass
#to avoid getting error.

#functions
"""A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result."""

#creating a function
def my_function():
  print("Hello from a function")
  
#calling a function
my_function()

#arguments
"""Information can be passed into functions as arguments.
arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
"""
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#parameters or arguments
"""the terms parameter and argument can be used for the same thing: information that are passed into a function."""
"""From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called."""

#number of arguments
"""By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less."""
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")

#arbitrary arguments, *args
"""If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition."""
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

#keyword arguments
"""You can also send arguments with the key = value syntax."""
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#arbitrary keyword arguments, **kwargs
"""If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition."""
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

#default parameter value
"""If we call the function without argument, it uses the default value"""
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#passing a list as an argument
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#return values
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

#pass statement
def myfunction():
  pass

#positional arguments
"""you can specify that a function caan have only postional arguments,add , / before the parameter name in the function definition"""
def my_function(x, /):
  print(x)
my_function(5)#get erroe if=
#keyword-only arguments
"""you can specify that a function can only be called with keyword arguments,add * before the parameter name in the function definition"""
def my_function(*, child3):
  print("The youngest child is " + child3)
my_function(child3 = "Emil")#get error if not write =

#combine positional,keyword-only,arbitrary arguments
def my_function(a,b,/,c,*,d):
  print(a,b,c,d)
my_function(10,20,c=30,d=40)

#recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)


#lambda function
"""A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression."""
x = lambda a : a + 10
print(x(5))

x=lambda a,b:a*b
print(x(5,6))

x=lambda a,b,c:a+b+c
print(x(5,6,2))

def myfunc(n):
  return lambda a:a*n
mydoubler=myfunc(2)
print(mydoubler(11))

#python classes and objects
"""Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects."""

#creating a class
class MyClass:
  x=5
print(MyClass)

#creating an object
p1=MyClass()
print(p1.x)

class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
p1=person("John",36)
print(p1.name)
print(p1.age)
"""THE INIT FUNSTION ISBEING AUTOMATICALLY CALLED
EVERY TIME THE CLASS IS BEING USED TO CREATE A NEW OBJECT"""

#__str__function
"""he __str__() function controls what should be returned when the class object is represented as a string.

If the __str__() function is not set, the string representation of the object is returned"""

class person:
  def __str__(self,name,age):
    self.name=name
    self.age=age
p1=person("John",36)
print(p1)

#string representstion of an obj with __str__()
class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def __str__(self):
    return f"{self.name}({self.age})"
p1=person("john",36)
print(p1)

#insert a funtion that prints a greeting, and execute it on the p1 object:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
"""The self parameter is a reference to the current instance of the class, 
and is used to access variables that belong to the class.
"""
#self parameter
'''The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:
'''
class person:
  def __init__(myobj,name,age):
    myobj.name=name
    myobj.age=age
    
  def myfunc(abc):
    print("hello my name is"+abc.name)
    
p1=person("john",36)
p1.myfunc()

#modify object parameterr
p1.age=40
#delete the property
del p1.age
#delete the objects
del p1
#pass statement
class person:
  pass

#python inheritance
"""Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class."""   

#create a parent class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:


#create a child class
class Student(person):
  pass
x = Student("John", "Doe")
x.printname()


