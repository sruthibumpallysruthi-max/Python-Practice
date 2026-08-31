
# WEEK 1

# A. Read the temperature in centigrade and convert it to Fahrenheit
# Formula: F = (C * 9/5) + 32

'''Temp = int(input("Enter the temperature in centigrade: "))
Fahrenheit = (Temp * 9/5) + 32
print("Temperature in Fahrenheit:", Fahrenheit)'''




# B. Consider two numbers as input and swap those two values  without using a 3rd variable


'''a = 10
b = 20

print("Before swapping:", a, b)

a, b = b, a

print("After swapping:", a, b)'''


# C. Read a list of numbers and check whether a particular number is present or not using membership operators


'''List = [1, 2, 3, 4, 5]

Ele = int(input("Enter any number: "))

if Ele in List:
    print("Number is present in the list")
else:
    print("Number is not present in the list")'''

# WEEK 2


# A. Read name, address, email and phone number of a person  through keyword and print the details

name = input("Enter your name: ")
address = input("Enter your address: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")

print("Name:", name)
print("Address:", address)
print("Email:", email)
print("Phone Number:", phone)



# B. Read the year and check whether it is a leap year or not


'''year = int(input("Enter the year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")'''



# C. Read 4 numbers and find maximum and minimum among them


'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

print("Maximum:", max(a, b, c, d))
print("Minimum:", min(a, b, c, d))'''



# WEEK 3


# A. Write a program to check whether the given input is  digit, lowercase character, uppercase character  or special character using if-elif-else

'''char = input("Enter any character: ")

if char.isdigit():
    print("It is a digit")
elif char.isupper():
    print("It is an uppercase character")
elif char.islower():
    print("It is a lowercase character")
else:
    print("It is a special character")'''

#B. write a python program to print even numbers from 2000 to 2100 in a given interval (use break)

'''for i in range(2000, 2101):
    if i > 2100:
        break
    if i % 2 == 0:
        print(i)'''

#WEEK 4

#A) Given a list of tuples. Write a program to find tuples which have all elements divisible by K from a list of tuples. test_list = [(6, 24, 12), (60, 12, 6), (12, 18, 21)], K = 6, Output : [(6, 24, 12), (60, 12, 6)]
'''test_list=[(6, 24, 12), (60, 12, 6), (12, 18, 21)]
K=6
res_list=[]
for tele in test_list:
    flag=True  
    for ele in tele:
        if(ele%K!=0):
            flag=False
            break;
    if(flag):
        res_list.append(tele)
print(res_list)'''


#using comprehension
'''test_list=[(6, 24, 12), (60, 12, 6), (12, 18, 21)]
K=6
res_list=[t for t in test_list if all (x%K==0 for x in t)]
print(res_list)'''


#B) Write a program to perform union, intersection and difference using Set A and Set B.

'''A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Union:", A.union(B)) #or (A|B)
print("Intersection:", A.intersection(B)) #OR (A&B)
print("Difference (A-B):", A.difference(B)) #OR (A-B)
print("Difference (B-A):", B.difference(A))  #OR (B-A)'''

#WEEK 5

#A) Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise.
'''def is_sorted(list):
    print(sorted(list))
    if list==sorted(list):
        return True
    else:
        return False
list=[1,3,6,4]  
print(is_sorted(list))'''  

#B) Write a function called has_duplicates that takes a list and returns True if there is any element that appears more than once. It should not modify the original list.
'''def has_duplicates(list):
    len1=len(list)
    set1=set(list)
    len2=len(set1)
    if len1>len2:
        return True
    else:
        return False
list=[1,2,3,2,3,4]
print(has_duplicates(list)) '''  

#WEEK 6
#A. Write a recursive function to compute gcd, factorial, fibonacci series
'''def gcd_rec(a,b):
    if b==0:
        return a
    else:
        return gcd_rec(b,a%b)
print(gcd_rec(8,12))    
 
def fac_rec(n):
    if n==0:
        return 1
    else:
        return n*fac_rec(n-1)
num=int(input("Enter any number to find factorial:"))
print(fac_rec(num))  


def fib_rec(a,b,n):
    if (n!=0):
        print(b)
        fib_rec(b,a+b,n-1)
x=0
y=1
num=int(input("Enter any number:"))
print(x,y)
fib_rec(x,y,num-2)'''  

#B.Write a function to compute gcd, factorial, fibonacci series
'''# GCD
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

print(gcd(8,12))


# Factorial
def fac(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

num=int(input("Enter any number to find factorial:"))
print(fac(num))


# Fibonacci series
def fib(n):
    a=0
    b=1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b

num=int(input("Enter any number:"))
fib(num)'''