#========================================Exercises 1 =========================================#

o=lambda x=1, y=2, z=3: x+y+z
print(o())
print(o(10))
print(o(10,20))

#========================================Exercises 2 =========================================#

my_list = [1,2,3,4,5]
def multi(my_list):
    mut=1
    for x in my_list:
        mut =x * mut
    return mut
print(multi(my_list))
    

#========================================Exercises 3 =========================================#

x= lambda x,y: x*y
print(x(2,3))

#========================================Exercises 4 =========================================#

number_list= list(filter(lambda x: x<0,range(-5,5)))
print(number_list)

#========================================Exercises 5 =========================================#

x= lambda x,y,z: x+y+z
print(x(5,6,2))

#========================================Exercises 6 =========================================#

x=("Joey", "Monica", "Ross")
y=("Chandler", "Pheobe")
z=("David","Rachel", "Pheobe")
result = list(zip(x,y,z))
print(result)

#========================================Exercises 7 =========================================#

coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')
d=dict(zip(coin, code))
print(d)

#========================================Exercises 8 =========================================#

def fun(variable):
    letters = ['a','e','i','o','u']
    if(variable in letters):
        return True
    else:
        return False

sequence = ['g', 'j', 'e', 'j', 'k', 'o', 'p', 'r']
filtered = list(filter(fun,sequence))
print(filtered)

#========================================Exercises 9 =========================================#

x= list(map(int,input("Enter a multiple value: ").split()))
print("List of students: ", x)

#========================================Exercises 10 =========================================#

def newfunc(a):
    return a*a
x = list(map(newfunc,(1,2,3,4)))
print(x)

#========================================Exercises 11 =========================================#

def func(a,b):
    return a+b
a=list(map(func,[2,4,5],[1,2,3,2,4]))
print(a)

#========================================Exercises 12 =========================================#

c= map(lambda x: x+x, filter(lambda x : (x>=3),(1,2,3,4)))
print(list(c))

#========================================Exercises 13 =========================================#

c = filter(lambda x : (x>=3),map(lambda x:x+x,(1,2,3,4)))
print(list(c))

#========================================Exercises 14 =========================================#
import functools

my_list =[5,6,2,9,7]
print(functools.reduce(lambda a,b: a if (a<b) else b, my_list))



#========================================Exercises 15 =========================================#

numbers=[1,2,3]
letters=['a','b','c']
result = tuple(zip(numbers, letters))
print(result)





