#indexing=accessing elements of a sequence using [](indexing operator) [start:end:step]
credit_number="1234-5678-9012-3456"
'''print(credit_number[4])
print(credit_number[0:4])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[:4])
print(credit_number[-1])
print(credit_number[-2])
print(credit_number[::2])'''

#format specifiers={value:flags} format a value based on what flags are inserted
#.(number)f=round to that many decimal places (fixed point)
#:(number)=allocate that ma ny spaces 
#:03=allocate and zero pad that many spaces
#:<=left justify
#:>=right justify 
#:^=center align 
#:+ =use aplus sign to indicate positive value
#:= =place sign to leftmost position
#:  =insert a space before positive numbers
#:, =comma separator

'''price1=3.14159
price2=-987.65
price3=12.34
print("Price1 is",price1)
print("Price2 is",price2)
print("Price3 is",price3)'''
#while loop=execute a some code WHILE some condition remains true

'''name=input("Enter your name:")
while name=="":
    print("You did not enter the name ")
    name=input("Enter your name:")
print("hello",name) '''   

'''age=int(input("Enter your age:"))
while age<0:
    print("Age cant be negative")
    age=int(input("Enter your age:"))
print("Your age is ",age)''' 

'''food=input("Enter a food you like (q to quit):")
while not food=="q":
    print("You like",food)
    food =input("Enter a food tou like(q to quit):")
print("Byee")'''

'''num=int(input("Enter a number between 1-10:"))
while num<1 or num>10:
  print("It is not valid",num)
  num=int(input("Enter a number between 1-10:"))
print("Your num is ",num) '''

#Pyhton compound interest calculator
'''principle=0
rate=0
time=0
while principle<=0:
    principle=float(input("Enter the principle amount:"))
    if principle <=0:
        print("Principle cant be less than or equal to zero")
       
while rate<=0:
    rate=float(input("Enter the interest rate:"))
    if rate <=0:
        print("Interest rate cant be less than or equal to zero")
   
while time<=0:
    time=float(input("Enter the time in years:"))
    if time <=0:
        print("Time cant be less than or equal to zero")

total=principle*pow((1+rate/100),time)
print(f"Balance after {time} years: ${total:.2f}")
print("Balance after", time, "years: $", round(total, 2))'''


'''principle=0
rate=0
time=0
while True:
    principle=float(input("Enter the principle amount:"))
    if principle <0:
        print("Principle cant be less ")
    else:
        break    
       
while True:
    rate=float(input("Enter the interest rate:"))
    if rate <0:
        print("Interest rate cant be less ")
    else:
        break    
   
while True:
    time=float(input("Enter the time in years:"))
    if time <0:
        print("Time cant be less ")
    else:
        break    

total=principle*pow((1+rate/100),time)

print("Balance after", time, "years: $", round(total, 2))'''

#for loops=execute a block a code a fixed number of times.
#          You can iterate over a range,string,sequence,etc.
'''for x in reversed(range(1,11)):
    print(x)
print("HAPPY NEW YEAR!") 
for x in (range(1,11,2)):
    print(x)   

credit_card="1234-4567-9012"
for x in credit_card:
    print(x)'''

for x in range(1,21):
    if x==13:
        break
    else:
        print(x)
            

