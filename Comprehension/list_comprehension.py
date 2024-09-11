# Simple example
num = [1,2,3,4,5,6,7,8,9,10]
square = [i**2 for i in num]
print(square)
# ----------------------------------------------------
# 2 for loops
list = [2,3,4,5]
list1 = [1,2,3,4,5,6]

multiply = [x*y for x in list1 for y in list]
print(multiply)
# -------------------------------------------------------
# 2d list
list = [1,2,3,4]
x = [[a**2,a**3] for a in list]
print(x)
