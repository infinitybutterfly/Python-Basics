#print
#1. string
print("Hello world")

Output
Hello World

#2. number

a = 5
print("Type of a: ", type(a))
b = 5.0
print("\nType of b: ", type(b))
c = 2 + 4j
print("\nType of c: ", type(c))

Output:
Type of a:  <class 'int'>
Type of b:  <class 'float'>
Type of c:  <class 'complex'>

#3. Sequence type

str = "This single line"
print(str)
s1 = "This is /nMultiline""
print(s1)

Output
This is single ine
This is
Multiline

#4. boolean

x = 5
y = 10 print(bool(x==y))
# Returns False as x is None
x = None
print(bool(x))
# Returns False as x is an empty sequence x = ()
print(bool(x))
# Returns False as x is an empty mapping x = {}
print(bool(x))
# Returns False as x is 0
x = 0.0
print(bool(x))
# Returns True as x is a non empty string x = 'GeeksforGeeks'
print(bool(x))
Output
False
False
False
False
False
True

#5.

arr=[1,2,3]
print(arr)

Output
[1,2,3]

print("* " * 10)

Output
* * * * * * * * * * 

str = "Hello World"
print(len(str))
print(str[-1])
print(str[3])
print(str[0:3])

Output
11
d
l
Hel


first = "Hello"
last = "World"
full = f"{first} {last}"

Output
Hello World


#Input

x = input("x = ")
y = int(x) +3
print(y)

optput
x = 12
15

#Math
 for math programs search Python <python version> math module
 some standard:
+, -, *, /, %, //, **

