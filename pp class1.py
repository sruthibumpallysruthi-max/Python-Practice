#oops
#while loop – Executes a block of statements repeatedly while the condition is true.
#for loop – Used for iterating over a sequence.
#Nested loop – A loop inside another loop.
#break statement – Stops the loop.
#continue statement – Stops the current iteration and continues with the next iteration.
#range() – Returns a sequence of numbers.


#sum of n numbers
'''c=0
n=int(input("Enter a number:"))
s=0
while c<=n:
    print("count=",c)
    s=s+c
    c=c+1
print("sum=",s)'''    

#write a py program to display even numbers and odd numbers separately and find even sum and odd sum from 1 to n
'''i=1
ES=0
OS=0
n=int(input("Enter n value:"))
while i<=n:
    if (i%2==0):
        print(i)
        ES=ES+i
    else:
        print(i)
        OS=OS+i    
    i+=1
print(f"Even sum is {ES}")
print(f"Odd sum is {OS}")'''

#write a py program to find sum of individual digits of given number
'''i=1
while i<6:
    print(i)
    if i==3:
        break
    i +=1'''

#WAPP to display the pattern
'''for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print() 
print("STOP")'''       

#WAPP to print even numbers from 2000 to 2100 in a givne interval

'''for i in range(2000,2100,2):
    print(i)'''

'''a="pyhton" 
print(len(a))#length
print(max(a))#max
print(min(a))#min
print(a[-1])#indexing'''

#String – A sequence of characters.
#Indexing – Used to access individual characters.
#Slicing – Used to access a part of a string.
#len() – Returns the length.
#max() – Returns the maximum value.
#min() – Returns the minimum value.
#split() – Splits a string into a list.
#isalpha() – Checks whether all characters are alphabetic.
#isdigit() – Checks whether all characters are digits.
#isupper() – Checks whether all characters are uppercase.
#islower() – Checks whether all characters are lowercase


#String slicing
'''S="IIT-MADRAS"
S[::]
S[::-1]
print(S)'''

#Operator
'''s1="HEllo"
s2=3*s1
print(s2)

s1="abcd"
s2="ABCD"
print(s1>s2)

s1="C c++ java python"
print(s1.split())

s="Akshitha"
print(s.isalpha())
print(s.isdigit())
print(s.isupper())
print(s.islower())'''

#List – An ordered and changeable collection of values/items.
#List elements are enclosed in square brackets [ ].
#Indexing and Slicing – Used to access list elements.
#append() – Adds an element to the list.
#remove() – Removes a specified element.
#del – Deletes an element.
#clear() – Removes all elements.
#List comprehension – Creates a new list using an expression and iteration.

#list
'''l1=[10,20,30]
print(l1)
l2=list("xyz")
print(l2)
l3=["Apple","BAnana","Grapes","1"]
print(type(l3))'''

'''list=[1,2,3,4,5]
list[4]=15
list[1:3]=[23,48]
list.append(4)  
list.remove(1)
del list[2]
print(list)
print(list.clear()) '''

'''import random
list=[1,3,5,6,7]
random.shuffle(list)
print(sum(list))
print(len(list))'''

'''A="Microsoft"
B="Microsoft"
print(A is B)

A=["p","m","n"]
B=["a","n","a"]
print(A is B)

#list comprehension
list1=[10,20,30,40]
list1=[x+25 for x in list1]
print(list1)'''


# WAPP to find the sum of even numbers in a list using list comprehension

'''lst = [10, 15, 20, 25, 30, 35, 40]

even_sum = sum([i for i in lst if i % 2 == 0])

print("Sum of even numbers:", even_sum)'''

'''numbers=input("Enter list numbers and use comma operator to separate").split(",")
nmmbers=[int(num) for num in numbers]
for i in range(len(numbers)):
    if(numbers[i]%4==0 and numbers[i]%5!=0):
        print(numbers[i])
print("END")'''

#Tuple – An ordered and immutable collection.
#Tuple supports Indexing, Slicing and Tuple operations.
#Tuple unpacking – Assigns tuple elements to variables.
#zip() – Combines elements from two or more iterables.

'''t=(1,2)
t+=(3,4)
print(t)

a=1,2,3
b=(1,2,3)
print(type(a))
print(type(b))

x,y,z=(1,2,3)
print(x==1)
print(y==2)
print(z==3)
print(type(x))

a=1,2,3,4
_,x,y,_ =a
print(x)
print(_)'''

'''first,*more,last=(1,2,3,4,5)
print(first)
print(last)
print(more)


#zip() function
a=("John","Charles","Mike")
b=("Jenny","Christy","Monica")
x=zip(a,b)
print(tuple(x))

tuple1=(10,3,5,6,8,5,77,4,67,)
tuple2=(i for i in tuple1 if i%5==0)
print(tuple2)
print(tuple(tuple2))'''

#4th August
#dictionary

#Dictionary – Stores data in key-value pairs.
#get() – Returns the value of a specified key.
#keys() – Returns dictionary keys.
#values() – Returns dictionary values.
#items() – Returns key-value pairs.
#popitem() – Removes the last inserted key-value pair.
#clear() – Removes all elements.
#copy() – Returns a copy of the dictionary.
#Nested Dictionary – A dictionary inside another dictionary.
#Dictionary comprehension – Creates a dictionary using an expression and iteration.

'''my_dictionary={}
print(my_dictionary)
my_dictionary={1:'Akshitha',2:'Shruthi'}
print(my_dictionary)
my_dict={'name':'AKshitha',1:[1,2,3]}
print(my_dict)

my_dict=dict({1:'apple',2:'banana'})
my_dict=dict([(1,'apple'),(2,'banana')])
print(type(my_dict))
my_dict={'name':'Akshitha','age':18}
print(my_dict)
print(my_dict['name'])
print(my_dict['age'])
print(my_dict.get('name'))
print(my_dict.get('address'))
#print(my_dict.get['address']) ----- error traceback 
print('age' in my_dict)
print('adress' in my_dict)

my_dict={'name':'Akshitha','age':18,'subjects':['python','java','c++']}
print(my_dict)
print(my_dict['subjects'][0]) #index of one value
print(my_dict.popitem())  #pop 
print(my_dict.clear())  #clear

my_dict={'name':'Akshitha','age':18}
print(my_dict)
my_dict['address']='downtown'
print(my_dict)

thisdict={"brand":"Ford","model":"Mustang","year":1964}
for x in thisdict:
  print(x) 
  print(thisdict[x])
for x in thisdict.values(): #values
    print(x)
for x in thisdict.keys():  #keys
    print(x) 
for x,y in thisdict.items():  #both values and keys
    print(x,y) 

#use of copy()    
dict1={'name':'Akshitha','age':18}    
mydict=dict1.copy()
print(mydict)

thisdict={"brand":"Ford","model":"Mustang","year":1964}
mydict=thisdict.copy()
print(mydict)

myfamily={
    "child1":{
        "name":"Emil",
        "year":2004
    },
    "child2":{
        "name":"Tobias",
        "year":2007
    },
    "child3":{
        "name":"Linus",
        "year":2011
    }
}
print(myfamily)
print(myfamily["child1"]["name"])

numbers=[1,2,3,4,5]
squared_dict={x:x**2 for x in numbers}
print(squared_dict)'''

#6th august
#Sets

#Union | – Combines elements of two sets.
#Intersection & – Returns common elements.
#Difference - – Returns elements present in one set but not another.
#Symmetric difference ^ – Returns elements present in either set, but not both.
#Membership in – Checks whether an element is present in a set.
#isdisjoint() – Checks whether two sets have no common elements.
'''set={1,2,3,"hello",2.5,("A","b")}
print(set)
print(type(set))

set={2,2,2,4,6,5,4,}
set.add(8)
set.update([3,6,6,938])
set.update([99,898],{1919,376482,873298})
set.remove(2)
set.discard(5)
set.pop()
#set.clear()
print(set)'''

'''my_set=set("Hello world")
print(my_set.pop())

set1={'e','a','s'}
print(set1.pop())

numbers=[1,2,3,4,5]
squared_set={x**2 for x in numbers}
print(squared_set)'''

'''A={1,2,3,4,9,5,6}
B={9,10,9,8}
print(A|B)  #union
print(A.union(B))
print(A&B)  #intersection
print(B.intersection(A))
print(A-B)   #difference
print(A.difference(B))
print(B-A)
print(A^B) 
print(A.symmetric_difference(B))  #symmetric difference'''

#11 August
set=set("apple")
print('a' in set)

A={1,2,3,4}
B={5,6,7}
C={4,5,6}
print(A.disjoint(B))






