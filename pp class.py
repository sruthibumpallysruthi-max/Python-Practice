#11 August
#issubset() – checks whether a set is a subset of another set.
#issuperset() – checks whether a set is a superset of another set.
#isdisjoint() – checks whether two sets have no common elements.
'''a={1,2,3,4}
b={5,6,8,4}
c={2,4,6,}
print(a.issubset(b))
print(a.issuperset(b))
print(a.isdisjoint(b))'''

#A block of reusable code Used to define,execute a function.
#Nested function - A function defined inside another function.

'''def fun():
    print("set object has no attribute")
    print("has an attribute")
fun()
fun()   

def fun1():
    print("Reached fun1")
    def fun2():
        print("inner avatar")
    print("Outer avatar")    
    fun2()
fun1()
print(type(fun1))


def cal_sum(x,y,z):
    return x+y+z
s1=cal_sum(10,20,30)
a,b,c=1,2,3
s2=cal_sum(a,b,c)
print(s1)
print(s2)'''

#positional arguments
#Positional arguments – arguments are passed according to their position.
'''def fun(i,j,k):
    print(i+j)
    print(k.upper( ))
fun(10,3.14,'Akshitha')'''

#Keyword arguments – arguments are passed using parameter names.
#keyword arguments
'''def print_it(i,a,str):
    print(i,a,str)
print_it(a=3.14,i=10,str='akshitha')   
print_it(str='akshitha',a=3.14,i=10) 
print_it(str='akshitha',i=10,a=3.14)'''

#Positional and keyword arguments – positional arguments should be passed first.
#positional and keyword
'''def print_it(i,a,str):
    print(i,a,str)
print_it(10,a=3.14,str='ngp')    #position should be first
print_it(10,str='ngp',a=3.14)'''

#Variable-length positional arguments – uses *args.
#varable-length positional arguments
'''def print_it(*args):
    print()
    for var in args:
        print(var,end='')
print_it(10)
print_it(10,3.14)
print_it(10,3.14,'silican')
print_it(10,3.14,'silican','punekar')        
print(type("args"))'''

#Variable-length keyword arguments – uses **kwargs.
#variable-length keyword arguments
'''def print_it(**kwargs):
    print()
    for name,value in kwargs.items():
        print(name,value,end='')
print_it(a=10)
print_it(a=10,b=3.14)        
print_it(a=10,b=3.14,s='silican')
dct={'student':'akshitha','age':18}
print_it(**dct)

def print_it(i,j,*args,x,y,**kwargs):
    print()
    print(i,j,end='')
    for var in args:
        print(var,end='')
    print(x,y,end='')
    for name,value in kwargs.items():
        print(name,value,end='') 
print_it(10,20,x=30,y=40)     
print_it(10,20,100,200,x=30,y=40) 
print_it(10,20,100,200,y=40,x=30) 
print_it(10,20,100,200,x=30,y=40,a=5,b=6,c=7)    

def fun(a,b=100,c=3.14):
    return a+b+c
w=fun(10)
print(w)
x=fun(20,50)
print(x)
y=fun(30,60,6.28)
print(y)
z=fun(1,c=3,b=5)
print(z)'''

#13 Aug
#Local variable – variable defined inside a function.
#Global variable – variable defined outside a function.
#global keyword is used to access/modify a global variable inside a function.

'''def demo():
    s='i love programming'
    print(s)
s='i love python'
demo()
print(s)    

a=20
def display():
    global a 
    a=30
    print('The value of a in function:',a)
display()
print('The value of an outside function:',a)  '''


#return statement returns a value from a function.
'''def minimum(a,b):
    if a<b:
        return a
    elif b<a:

        return b 
    else:
        return "Both the numbers are equal"
print(minimum(100,85))    

def calc_arith_op(num1,num2):
    return num1+num2,num1-num2
print('',calc_arith_op(6,7))

def compute(num1):
    print("Number=",num1)
    return num1*num1,num1*num1*num1
square,cube=compute(4)
print("Square=",square,"Cube=",cube) '''  

#Recursion is a process in which a function calls itself.
'''def factorial(n):
    if n==0:
     return 1
    return n*factorial(n-1)
print(factorial(5))

def func(x):
    return x*x*x
print(func(4))'''

#Lambda function – An anonymous function created using the lambda keyword that can take any number of arguments but has only one expression.
'''cube=lambda x:x*x*x
print(cube(2))'''

#31 August
#classes
class csd:
    x=5
print(csd) 

class hitam:
    pass

class green:
    x=5
    def display(self):
        print("HELLO GREEN CAMPUS")
obj=green()    
print(obj.x)
obj.display()

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Hello,i am "+self.name)
    def greet(self):
        print("Hello,my name is" + self.name)
p1=Person("Akshitha",18)
p1.greet()        

