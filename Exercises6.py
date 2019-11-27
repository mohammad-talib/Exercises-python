import numpy as np
import matplotlib.pyplot as plt
# =============================================================================
#                                   Exercise 1
# =============================================================================

zero = np.zeros(10)
one = np.ones(10)
five = np.ones(10) * 5

print(zero, one, five)

# =============================================================================
#                                   Exercise 2
# =============================================================================

array_one = np.arange(30, 71, 1)
print(array_one)

# =============================================================================
#                                   Exercise 3
# =============================================================================

array_two = np.arange(30, 71, 2)
print(array_two)

# =============================================================================
#                                   Exercise 4
# =============================================================================

array_three = np.arange(27).reshape(3, 3, 3)
print(array_three)

# =============================================================================
#                                   Exercise 5
# =============================================================================

array_four = np.random.normal(0, 1)
print(array_four)

# =============================================================================
#                                   Exercise 6
# =============================================================================

array_five = np.arange(48).reshape(3, 4, 4)
for array in array_five:
    for arr in array:
        for ar in arr:
            print(ar)
#print(array_five)

# =============================================================================
#                                   Exercise 7
# =============================================================================

array_six = np.arange(0, 21)
counter = 0;
for array in array_six:
    if array > 8 and array <= 16:
         array_six[counter]  = array * -1
    counter+=1
print(array_six)
    

# =============================================================================
#                                   Exercise 8
# =============================================================================

x = [1, 8, 3, 5]
y = np.random.randint(0, 11, 4)
multiplay_number = x * y
print(multiplay_number)

# =============================================================================
#                                   Exercise 9
# =============================================================================

find_array = np.array([[1,2,3],[4,5,6]])
print(find_array.shape)

# =============================================================================
#                                   Exercise 10
# =============================================================================

array_ten = np.arange(27).reshape(3, 3, 3)
print(array_three)

# =============================================================================
#                                   Exercise 11
# =============================================================================

a = np.array([9, -1, 2, 5])
b = np.array([1, -6, 0, 10])
c = np.array([[1, 8, 2, 5],[3, 1, 7, 9]])

print("a+b: ", a-b)
print("a*b: ", a*b)
print("a.dot(b): ", a.dot(b))
print("a*2: ", a*2)
print("np.sin(a): ", np.sin(a))
print("a<3: ", a<3)
print("a.sum(): ", a.sum())
print("a.sum(axis=0): ", a.sum(axis=0))
print("c.sum(): ", c.sum())
print("c.sum(axis=0): ", c.sum(axis=0))
print("a.min(): ", a.min())
print("a.max(): ", a.max())
print("a.mean(): ", a.mean())
print("a average(): ", np.average(a))
print("a median(): ", np.median(a))
print("a std(): ", np.std(a))
print("a var(): ", np.var(a))
print("c cumsum(): ", c.cumsum())
print("a[1:2]: ", a[1:2])
print("a[1:2]: ", a[2:])
print("c[-1]: ", c[-1])



# =============================================================================
#                                   Exercise 12
# =============================================================================

x = range(1, 50)
y = [value * 3 for value in x]
plt.plot(y)
plt.ylabel('Y-axis')
plt.xlabel('X-axis')
plt.title('Draw a line')
plt.show()

# =============================================================================
#                                   Exercise 13
# =============================================================================

#x1 = [10, 20, 30]
#y1 = [20, 40, 10]
#
#x2 = [10, 20, 30]
#y2 = [40, 10, 30]
#
#Xlabel = 'x-axis'
#Ylabel = 'y-axis'
#title = 'Tow or more lines on same plot with suitable legends'
#
#plt.plot(x1,y2)
#plt.plot(x2,y1)
#
#plt.ylabel(Xlabel)
#plt.xlabel(Ylabel)
#plt.title(title)


# =============================================================================
#                                   Exercise 14
# =============================================================================


t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'g--', t, t**2, 'bs', t, t**3,'r^')
plt.show()



# =============================================================================
#                                   Exercise 15
# =============================================================================


x = ['Python', 'java', 'PHP', 'javaScript', 'C#', 'C++']
popularity = [22.0, 17.6, 8.8, 8, 7.7, 6.7]

plt.bar(x,popularity,align='center',color = ('red', 'black', 'green', 'blue', 'yellow', '#33FBF4'))

plt.ylabel("Popularity")
plt.xlabel("Languages")
plt.title("Popularity of Programming Language")

