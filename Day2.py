#OPerators

friends=10

#Addition
#friends=friends+1  
#friends+=1

#Subtraction
#friends=friends-2
#friends-=2

#Multiplication
#friends=friends*3
#friends*=3

#Division
#friends=friends/2
#friends/=2

#Modular division
#friends=friends**2
#friends**=2
#remainder=friends%3
#print(remainder)

#friends=friends//2
friends//=2
#print(friends)

#Round,absolute,power,max,min
x=3.14
y=4
z=5

#result=round(x)
#result=abs(y)
#result=pow(4,3)
#result=max(x,y,z)
#result=min(x,y,z)
#print(result)


#math functions
#import math
#x=9.9
#print(math.pi)
#print(math.e)
#result=math.sqrt(x)
#result=math.ceil(x)
#result=math.floor(x)
#print(result)

#Exercises

#import math
#radius=float(input("Enter the radius of a circle: "))
#circumference=2*math.pi*radius
#print("circumference of the circle is:",round(circumference,2),"cm")

#import math 
#radius=float(input("Enter the radius of a circle:"))
#area=math.pi*radius**2
#area=math.pi*pow(radius,2)
#print("area of the circle is:",round(area,2),"cm^2")

#import math
#a=float(input("Enter side A:"))
#b=float(input("Enter side B:"))
#c=math.sqrt(pow(a,2)+pow(b,2))
#print("value of side c:",c)

#if=Do some code only if some condition is True 
#   Else do something else

age=int(input("Enter your age:"))
if age >= 18:
    print("you are now signed up!")
elif age<0:
    print("you haven't been born yet!")
elif age>= 100:
    print("you are too old to sign up")
else:
    print("you must be 18+ to sign up")

#Example
    response=input("Would you like food? (Y/N):")
    if response =="Y":
        print("Have some food!")
    else:
        print("No food for you!")   

#Example
        name=input("Enter your name: ")
        if name=="Shruthi":
            print("Name Shruthi is valid")
        else:
            print("Not valid")   















