#Basics

print("I love Biryani")
print("Its really good")

#Variable= A variable for a value (string,integer,float,boolean)
#  A variable behaves as if it was the value it contains

#Strings
first_name="bro"
food="biryani"
email="sruthi@gmail.com"
print(f"Hello, {first_name}!")
print(f"You like {food}")
print(f"Your email is {email}")

#Integers
age=25
quantity=3
num_of_students=30

print(f"You are {age} years old ")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

#Float
price=10.99
gpa=9.15
distance=5.5
print("The price is",price)
print("your gpa is",gpa)
print ("you ran",distance)

#Boolean

is_student=True

if is_student:
    print("You are a student")
else:
    print("You are not a student")


is_student=False
print("Are you a student?",is_student)

for_sale=True
if for_sale:
    print("That item is for sale")
else:
    print("That item is not for sale")   

is_online=False
if is_online:
    print("Your on online")
else:
    print("You are not online")    

    #Typecasting=process of converting a variable from one data type to another
    #str(), int(), float(), bool()
    name="shruthi"
    age="19" 
    gpa="9.15" 
    is_name=True
    print(type(name))
    print(type(age))
    print(type(gpa))
    print(type(is_name))

    age=float(age)
    print(age)

    age=str(age)
    age += "1"
    print(age)

name=bool(name)
print(name)





#input()=A function that prompts the user to enter data 
#         Returns the entered data as a string
#name=input("What is your name?")
#age=int(input("What is your age?"))
        #or

#age=int(age)
#age=age+1
          
#print("hello",name)
#print("happy birthday")
#print("your age is",age)

#Exercise 1 Rectangle Area calculation

length=float(input("Enter the length"))
width=float(input("Enter the width"))
area=length*width
print(area)

#SHopping cart program
item=input("What item would you like to buy?")
price=float(input("What is the price?"))
quantity=int(input("How many would you like to buy?"))
total=price*quantity
print("You have bought",quantity,"of",item)
print("The total is:",total)

#Madlibs game
#word game where you create a story
#by filling in blanks with random words

adjective1=input("Enter an adjective ")
adjective2=input("Enter another adjective ")
adjective3=input("Enter one more adjective ")
noun=input("Enter a noun ")
verb=input("Enter a verb ending with 'ing' ")

print("Today i went to a", adjective1, "zoo")
print("In an exhibit,I saw a", noun)
print(noun, "was", adjective2, "and", verb)
print("I was", adjective3, "!")



      
    






