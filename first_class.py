
# class todo
# variable
# data types
# commenting
# inbuilt funx


# commenting: single line  and multiline commenting
"""
class todo
variable
data types
commenting
inbuilt funx
naming convention
naming rules
data type conversion
concatenation

"""
""" 
this is multiline comment. this comment does not throw an error, and it can be outputted on the terminal unlike the single line comment 
"""
# print("hello! welcome to python class")

basket ="mango, orange, pawpaw"
basket2 ="mango is a juicy fruit", "orange", "pawpaw"
basket3 =["mango is a juicy fruit", "orange", "pawpaw"]
# print(basket[0])
# print(basket2[1])
# print(basket2)
# print(len(basket2))
# print(type(basket2))
# print(type(basket), 'this is basket one')
# print(type(basket3), 'this is basket three')
# student_name=input("what is you name>>> ")
# print(student_name)

# naming conventions: pascal naming conven.., camel case, snake naming convention

NameOfStudent ="Abdulmalik"  #pascal
nameOfStudent ="Abdulmalik"  #camel
name_of_student ="Abdulmalik"  #snake

# rules for naming variable
"""
do not start variable name with numbers
do not use reserve words for naming your variable
it must be descriptive
"""
# 2_name
list_itm=('tolu','bolu')


# types of data conversion: explicit and implicit

# implicit
val1=4.8
val2=6
result=val1 + val2
# print(type(val1), "for first val")
# print(type(val2), "for second val")
# print(type(result), "for result")

# # explicit
# set_itm={1, 2, 3, 4, 5}
# new_set=list(set_itm)
# print(type(set_itm))
# print(type(new_set))
total_score=100
score="70"
per=int(score)/total_score * 100
# print(type(score))
# print(per)

# string1= "hello"
# string2= "world"
# result = "string" + "string2"
"""
str1= "hello"
str2= "world"
result= str1+str2
print(result)
"""

#concatenation using f-string

# first_name = "John"
# second_name = "Praise"
# result = f"My name is {first_name} {second_name}. i stay in yoaco"
# print(result)

# 2.declare a variable name, color, weight, and age and out put and information related to the variable store
# variable_name= "ade","bola"
# colour="orange","yellow","pink"
# weight="12kg","13kg","15kg"
# age="14 years","23 years"

# variable_name= "ade"
# colour="orange"
# weight="12kg"
# age="14 years"
# print('my name is',variable_name,"i love",colour,"my weight is", weight,"and my age is ",age)

""" 
concatenation
operators
string
"""
# string1= "Tomiwa"
# string2= " Bankole"
# result = (string1 + string2 + ' you are welcome')
# print(result)


# operator
# operators 
"""
what is operators
type of operator
precedence (PEMDAS)

"""
# operators
# python OPERATORS AND IT USES
# In Python programming, Operators in general are used to perform operations on values and variables.
# Types of Operators in Python
#1 Arithmetic Operators
#2 Comparison Operators
#3 Logical Operators
#4 Assignment Operators
#5 Identity Operators and Membership Operators
"""
Operators	
#1 Arithmetic Operators

+	Addition: adds two operands:	x + y
–	Subtraction: subtracts two operands	x – y
*	Multiplication: multiplies two operands	x * y
/	Division (float): divides the first operand by the second	x / y
//	Division (floor): divides the first operand by the second	x // y
%	Modulus: returns the remainder when the first operand is divided by the second	x % y
**	Power: Returns first raised to power second operand	x ** y
"""
# val1 = 7
# val2 = 3
# print(val1%val2)

# class work
# build an even and ood number checker

# val1=int(input('enter a number>>> '))
val2=2
res=val1%val2
# print("if the result is zero your number is even number and if it is one it is odd number.")
# print(res)
"""
Comparison Operators in Python

>	Greater than: True if the left operand is greater than the right	x > y
<	Less than: True if the left operand is less than the right	x < y
==	Equal to: True if both operands are equal	x == y
!=	Not equal to – True if operands are not equal	x != y
>=	Greater than or equal to True if the left operand is greater than or equal to the right	x >= y
<=	Less than or equal to True if the left operand is less than or equal to the right	x <= y
"""
# print("first operation>>>",4>6)
# print("second operation>>>",4<6)
# print("third operation>>>",4==4)
# print("third operation>>>",4 != 6)

"""
Logical Operators in Python
and	: True if both the operands are true	x and y
or: True if either of the operands is true 	x or y
not	: True if the operand is false 	not x

"""
# val1 = []
# print(not val1)

# value1=[]
# res=bool(value1)
# print('bool value',res)
# print('not: ', not res)
# value2=()
# print(not value2)
"""
Assignment Operators in Python
a = 10
b = a 
print(b) 
b += a 
print(b) 
b -= a 
print(b) 
b *= a 
print(b) 
b <<= a 
print(b)
"""

score = 5
score %= 2
# print(score)
"""
Membership Operators in Python
x = 24
y = 20
list = [10, 20, 30, 40, 50]  

if (x not in list): 
	print("x is NOT present in given list") 
else: 
	print("x is present in given list") 

if (y in list): 
	print("y is present in given list") 
else: 
	print("y is NOT present in given list") 

"""
list_itm=['mango', 'pawpaw', 'cashew']
# print(' mango' in list_itm)
# print( 'orange' not in list_itm)


"""
Bitwise Operators in Python
Python Bitwise operators act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.

&	Bitwise AND	x & y
|	Bitwise OR	x | y
~	Bitwise NOT	~x
^	Bitwise XOR	x ^ y
>>	Bitwise right shift	x>>
<<	Bitwise left shift	x<<

eg

a = 10
b = 4
print(a & b) 
print(a | b) 
print(~a) 
print(a ^ b) 
print(a >> 2) 
print(a << 2) 

Bitwise operators are commonly used in low-level programming, cryptography, and optimization tasks where direct manipulation of binary representations is necessary.
"""

name='john wick'
name.capitalize

#Take input from user
word = input("Enter the word: ").strip()

#Reverse the input taken from the user
reversed_word = word[::-1]

#Check
result = word == reversed_word

#display
print(result)

