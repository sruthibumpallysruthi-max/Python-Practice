#Python Calculator

'''operator=input("Enter an operator(+ - * /):") 
num1=float(input("Enter the 1st number:"))          
num2=float(input("Enter the 2nd number:"))
if operator=="+":
    result=num1+num2
    print(round(result))
elif operator =="-":
    result=num1-num2
    print(round(result))
elif operator=="*":
    result=num1*num2
    print(round(result))
elif operator =="/":
    result=num1/num2
    print(round(result))
elif operator =="//":
    result=num1//num2
    print(round(result))
elif operator =="%":
    result=num1%num2   
    print(round(result)) 
else:
    print("operator is not valid")''' 


    #Python weight calculator
'''weight=float(input("Enter your weight"))
    unit=input("Kilograms or pounds?(K or L):")
    if unit=="K":
        weight=weight*2.205
        unit="Lbs."
    elif unit=="L":
        weight=weight/2.205
        unit="Kgs."  
    else:
        print("Invalid unit")   
    print("Your weight is:",round(weight,2),unit)'''    




#typecasting=process of converting a variable from one data type to another
#str(), int(), float(), bool()
#string----integer
'''age="19"
age=int(age)
print(age)
print(type(age))'''

#string--float
'''price="99.99"
price=float(price)
print(price)
print(type(price))'''

#integer---string
'''marks=85
marks=str(marks)
print(marks)
print(type(marks))'''


#integer--float
'''number=25
number=float(number)
print(number)
print(type(number))'''


#float---integer
'''height=5.6
height=int(height)
print(height)
print(type(height))'''


#integer---boolean
'''number=1
number=bool(number)
print(number)
print(type(number))'''

#Arithmetical operators
'''a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Modulo:",a%b)
print("Exponentiation:",a**b)'''

'''#Assignment operators
# =(Assignment)
name="Abhi"
print(name)

#+=(Addition assignment)
marks=90
marks+=5
print(marks)

#-=(Subtraction assignment)
balance=1000
balance-=250
print(balance)


salary = 15000
salary *= 2
print(salary)


money = 100
money /= 4
print(money)

students = 23
students //= 5
print(students)


number = 17
number %= 5
print(number)


number = 4
number **= 2
print(number)'''

#Relational operators
'''# ==(Equals to)
a=10
b=20
c=(a==b)
print(c)

#!=(Not equals to)
a=10
b=5
print(a!=b)

#>(Greater than)
marks=90
print(marks>75)

#<(Less than)
age=18
print(age<21)

#>=(Greater than or equals to)
marks=100
print(marks>=90)

#<=(Less than or equals to)
height=6
print(height<=7)'''

#Logical operators

'''#and=both conditions must be true,even if one condition is false,the answer is false
age=18
id=True
print(age>=18 and id)

#or=at least one condition must be true
is_weekend=True
is_holiday=False
print(is_weekend or is_holiday)

#not=not reverses the result
#true becomes False
#false becomes true
is_raining=True
print(not is_raining)

age=19
has_ticket=True
print(age>=18 and has_ticket)'''

#Membership operator

'''#in=checks whether something is present

name="abhi"
print("a" in name)

fruit="mango"
print("g" in fruit)

#not in=checks something is not present
name="abhi"
print("x" not in name)

fruit="apple"
print("a" not in fruit)'''

# identity Operator

'''#==
#is(Identity comparision)
a=[10,20]
b=a
print(a is b)

#is not=checks whether two variables are not the same object
a=[10,20]
b=a
print(a is not b)'''

#Built-in functions

'''#print()
name="sruthi"
print(name)

#input()
name=input("Enter your name:")

#int()
age=int(input("Enter your age"))

#float()
price=float(input("Eter price:"))

#str()
num=100
print(str(num))

#bool()
print(bool(1))

#type()
print(type(25))

#round()
print(round(6.5))

#abs()
print(abs(-26))

#pow()
print(pow(2,3))

#max()
print(max(10,20,30))

#min()
print(min(1,5,6,))'''

#conditional statements

#if statement=used to execute a block of clock only when a condition is true
'''age=20
if age>=18:
    print("You can vote")

#if-else statement=used whenthere are two possible choices
#if condition is true -if blocks executes
#if condition is false-else block executes
marks=40
if marks>=35:
    print("Pass")
else:
    print("Fail") 

#if-elif-else statement=used when there are multiple conditions
marks=85
if marks>=75:
    print("Grade A") 
elif marks>=65:
    print("Grade B") 
elif marks>=45:  
    print("Grade C")  
else:
    print("Fail")'''    

#loop=a loop is used to repeat a block of code multiple times without writing it again and again

#2 types
# 1.for loop
#a for loop is used when you know how many times you want to repeat something
#Syntax:for variable in range(start,stop)
#          statements

'''for i in range(1,6):
    print(i)

for i in range(1,6):
    print(i*2) 

for i in range(5):
    print(i+1)   

for i in range (3):
    print(i)
    print("Hello")'''        

#range

'''for i in range(2,11,2):
    print(i)
for i in range(10,0,-1):
    print(i)  
for i in range(1,10,2):
    print(i)  
for i in range(20,0,-5):
    print(i) '''
       
# 2. while loop =is used until the condition is true
'''i=5
while i>=1:
    print(i)
    i=i-1

i=1    
while i<=5:
    print(i)
    i=i+1

i=1
while i<=10:
    print(i)
    i=i+1

i=10
while i>=1:
    print(i)
    i=i-1

#print even numbers
i = 2
while i <= 10:
    print(i)
    i = i + 2

i=1
while i<=9:
    print(i)
    i=i+2 
  
count=1
while count<=5:
    print("sruthi")
    count=count+1

#multiplication table of 5
i=1
while i<=10:
    print(i*5)
    i=i+1

    i = 20

while i >= 10:
    print(i)
    i = i - 2'''

#break
'''for i in range(1,11):
    if i==6:
        break
    print(i)

password = ""

while password != "python":
    password = input("Enter password: ")

print("Access Granted")'''

#continue
'''for i in range(1,6):
    if i==3:
        continue
    print(i)'''

#pass
'''for i in range(5):
 if i == 2:
    pass
    print(i)''' 

#nested loops
'''for i in range(1,4):
  for j in range(3,6):
    print(i,j) 

for i in range(7):
  for j in range(9):
    print(i,j)          

for i in range(3):
  for i in range(3):
    print("*")'''

'''for i in range(3):
    for j in range(3):
        print("*", end="")
    print()  

for i in range(4):
    for j in range(5):
        print("Hello")      

for i in range(2):
    print("Python")
    for j in range(2):
        print("AI")

for i in range(2):
    for j in range(3):
        print(j)''' 

'''for i in range(3):
    for j in range(4):
        print("*", end="")
    print()'''
'''for i in range(2):
    print(i)
    for j in range(2):
        print(j)'''

#math module
'''#square root
import math
print(math.sqrt(25))

#power
import math
print(math.pow(2,3))

#value of pi
import math
print(math.pi)

#math.ceil=Returns the smallest integer greater than or equal to the given number.Think of it as rounding UP.
#it returns exact integer but without float
import math
print(math.ceil(4.2))

import math
print(math.ceil(8.01))

#math.floor=Returns the largest integer less than or equal to the given number.Think of it as rounding DOWN.
import math
print(math.floor(8.01))

import math
print(math.floor(4.2))

#math.factorail()=A factorial of a number is the product of all positive integers from 1 to that number.
import math
print(math.factorial(9))

#math.gcd=gcd() returns the Greatest Common Divisor (GCD) of two numbers.
import math
print(math.gcd(12,18))
print(math.gcd(20,30))

#math.fabs()=Returns the absolute (positive) value of a number.it will return a float value
import math
print(math.fabs(-26))

#math.e=math.e is a mathematical constant.
import math
print(math.e)'''

#Functions=A function is a reusable block of code that performs a specific task.


''' greet():
    print("Hello")
greet() 

def welcome():
    print("Welcome to Python!")
welcome()    

def stars():
    print("****")
stars()
stars()
stars()

def hello():
    print("Shruthi")
hello()
hello()
hello()'''

#PArameter=A parameter is a variable that is written inside the function definition.

'''def greet(name):
    print("Hello",name)
greet("Shruthi")        

def make_pizza(topping):
    make_pizza("cheese")
    make_pizza("paneer")
    make_pizza("corn")
    print("topping")

def student(name):
    print("Student Name",name)
student("SHruthi")
student("Vasundara")
student("Akhila")'''

#multiple parameters=
'''def student(name,age):
    print(name)
    print(age)
student("Ruthi",19)    

def multiply(a,b):
    print(a*b)
multiply(5,4)'''    

#return statement
''' def (a,b:
    print(a+b)
result=add(10,20)
print(result)

def square(n):
    return n*n
x=square(5)
print(x)

def math(n):
    return n*n+10
y=square(5)+10
print(y)'''

#Default arguments=A default argument is a parameter that already has a value. If no argument is passed, Python uses the default value.
'''    def country(name="guest"):
    print("Hello",name)
greet()

def country(name="India"):
    print("Country:",name)
country()
country("Japan")'''

#local variables and global variables
'''def demo():
    x=10                 #it is of local variable =exists only inside demo()
    print(x)
demo()   

x=10
def demo():
    print(x)             #global variable=can be used by the entire program
demo()   
print(x)''' 

#strings=A string is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
#String Concatenation=Concatenation means joining strings together.  
'''first="HEllo"
second="Shruthi"   
#print(first+second) 
 
#to add space
print(first+" "+second)'''

#string repetition=You can repeat a string using *.
'''print("Vasundara" * 3)'''

#indexing=Indexing is used to access individual characters of a string using their position.
'''name="python"
print(name[0])
name="Vasundara"
print(name[4])
name="Sameeksha"
print(name[5])

#negative indexing=it means python allows us to count even from the last giving the last digit the value -1 and the before one is -2
word="Python"
print(word[-1])
print(word[-3])'''

#slicing=Slicing is used to extract a part of a string.
'''word="Python"
print(word[0:3])
word="Shruthi"
print(word[1:5])
name="Vasundara"
print(name[0:4])'''

#string methods=String methods are predefined functions used to perform different operations on strings.

'''#upper()=Converts all characters to uppercase.
name="Akshitha"
print(name.upper())

#lower()=converts all characters to lowercase.
name="Sameeksha"
print(name.lower())

#title=Makes the first letter of every word capital.
name=" i love myself"
print(name.title())

#capitalize()=Makes only the first letter of the first word capital.
name="hey google"
print(name.capitalize())

#strip()=Removes extra spaces from the beginning and end of a string.
name="   shruthi   "
print(name.strip())

name="python     "
print(name.strip())

#replace()=Replaces one word or character with another.
name="Rajulake Raju RaaRaju"
print(name.replace("RaaRaju","Prabhas Raju"))

text="banana"
print(text.replace("a","*"))

#find()=Finds the index of the first occurrence of a character or word.
text="Python"
print(text.find("t"))

tfi="Prabhas"
print(tfi.find("b"))

nani="Paradise"
print(nani.find("z"))
#if the letter is not found in the word it simply returns -1

#count()=Counts how many times a character or word appears.
text="Baahubali"
print(text.count("a"))

name="Billa You Changed Billa"
print(text.count("a"))

#startswith()=Checks whether a string starts with a given word or character.
text="Python Programming"
print(text.startswith("Python"))
print(text.startswith("Java"))

#endswith=Checks whether a string ends with a given word or character.
text="Python programming"
print(text.endswith("programming"))
print(text.endswith("JAva"))

#isalpha=Checks if all characters are alphabets.
print("Shruthi".isalpha())
print("Shruthi@123".isalpha())

#isdigit()=Checks if all characters are digits.
print("12345".isdigit())
print("123@a".isdigit())

#isalnum()=Checks if the string contains only letters and numbers (no spaces or symbols).
print("Python123".isalnum())
print("Sam123@".isalnum())

#split()=Splits a string into a list.
text="My name is shruthi"
print(text.split())

name="kaateramma koduku"
print(name.split())

#join()=This is the opposite of split().It joins a list into one string.
name="kaateramma koduku"
print(" ".join("kaateramma koduku"))'''

#lists=A list is an ordered, mutable collection of items that can store multiple values in a single variable.
'''
numbers=[1,2,3,4,5]
print(numbers)

fruits=["Apple","Banana","Mango","Guava"]
print(fruits)

student=["sruthi",19,19.5,True]
print(student)

#mutable means they can be changed 
fruits=["Apple","Mango","Guava"]
fruits[1]='Orange'
print(fruits)

#indexing in lists  
fruits=["APple","BAnana","Grapes"]
print(fruits[0])

#Negative indexing
fruits=["Apple","BAnana","Grapes","Orange"]
print(fruits[-1])

#slicing in lists
numbers=[10,20,30,40]
print(numbers[1:3])

#modifying lists
numbers=[100,200,387]
numbers[0]=80
print(numbers)

tfi=["Prabhas","ALlu Arjun","Nani","RAm charan","Jr.Ntr"]
tfi[1]="Mahesh Babu"
print(tfi)

#append() =adds ONE element to the END of the list.
fruits=["Apple","Banana"]
fruits.append("Grapes")
print(fruits)

prabhas=["billa","darling","mirchi"]
prabhas.append("Baahubali")
print(prabhas)

numbers=[10,20,30]
numbers.append(60)
print(numbers)

#insert()= adds an element at a specific position (index).
nani=["jersey","hit3","saripoda sanivaram"]
nani.insert(1,"paradise")
print(nani)

friends=["shruthi","vasundara","akheela"]
friends.insert(3,"ragnandhini")
print(friends)

#extend()= adds ALL elements from another list.
list1=["shruthi","vasundara"]
list2=["akheela","ragnandhini"]
list1.extend(list2)
print(list1)

list1=["salaar","saaho"]
list2=["vaaranasi","guntoor karam"]
list1.extend(list2)
print(list1)

#remove()=Removes an element by value.
memes=["bhaai","annnaaa","eh"]
memes.remove("bhaai")
print(memes)

heroine=["rashmika","sreeleela","anushka","bhagya sri"]
heroine.remove("sreeleela")
print(heroine)

#pop()=Removes an element by index.
language=["telugu","tamil","malayalam","kannada"]
language.pop(2)
print(language)

baahubali=["bahubali","ballaladeva","devasena"]
baahubali.pop(1)
print(baahubali)

#clear()=Removes everything from the list.
numbers=[1,2,3,4]
numbers.clear()
print(numbers)

statements=["if","else","elif"]
statements.clear()
print(statements)


#sort()=Sorts the list in ascending order.
numbers=[8,46,4,567]
numbers.sort()
print(numbers)

#reverse()=Reverses the order of the list.
numbers=[1,2,3,4,5,6,29]
numbers.reverse()
print(numbers)

#len()=Returns the number of elements.
names=["shruthi","akshitha","soujanya","niharika"]
print(len(names))

#membership operators
fruits=["Apple","Banana","Grapes"]
print("Apple" in fruits)

#not in
prabhas=["mirchi","darling","billa"]
print("mirchi" not in prabhas)
'''

####Tuples
t=(5,)
print(type(t))

#tuple count()
t=("Prabhas","Nani","Nani","Prabhas","Ntr","Prabhas")
print(t.count("Prabhas"))

#tuple indexing
t=("B","R","S","F")
print(t.index("S"))






