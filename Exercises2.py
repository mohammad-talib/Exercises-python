#================================== Exercise 1 ===============================================#

num1 = int(input("Enter First Number! "))
num2 = int(input("Enter second Number! "))

if num1>num2:
    print(num1)
else:
    print(num2)
    
#================================== Exercise 2 ===============================================#
    
multnum = int(input("Input a number! "))
for x in range(1,11):
    print(multnum,"X",x,"=", x * multnum)

#================================== Exercise 3 ===============================================#

for i in range(6):
    for j in range(i):
        print("*",end="")
    print("")
for z in range(i-1, 0,-1):
    for y in range(z):
        print("*",end="")
    print("")
   

#================================== Exercise 4 ===============================================#  
    
letters = ["x","y","z","a","b","c"]
for i in letters:
    if i == "a":
        continue
    elif i == "c":
        break
    print(i)
    
#================================== Exercise 5 ===============================================#

for x in range(12,25,3):
    print(x)    
    
    
#================================== Exercise 6 ===============================================#    
    
i=1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
    
    
#================================== Exercise 7 ===============================================#    
    
sumnum = int(input("Input a number! "))
summation=0
for x in range(0,sumnum+1):
    summation+=x
#    print(x+1)
print(summation)

    
#================================== Exercise 8 ===============================================#

number = int(input("Input a Number! "))
if number % 2 == 0:
    print("Even")
else:
    print("odd")

#================================== Exercise 9 ===============================================#










#================================== Exercise 10 ===============================================#

while True:
    try:
        num=input("please enter an integer: ")
        num=int(num)
        break
    except ValueError:
        print("Not integer number! please try again...")
print("Successfully Entered an Integer")


#================================== Exercise 11 ===============================================#

try:
    a=3
    if a < 4:
        b=a/(a-3)
    print("Value of b = ", b)
except(ZeroDivisionError, NameError):
    print("\nError Occurred and Handled")



end=6
increment = 1;
lines = 0;
for whiteSpaces in range(lines , end ,increment):
    if(end == (end//2)):
        lines = end;
        end = 0;
        increment = -1;
    for stars in range(whiteSpaces):
        print("*" , end=" ");
    print("\n");
    





