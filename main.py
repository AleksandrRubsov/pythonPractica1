import math
from math import *
import sympy

print("Задача:1.1")
print("Введите x: ")
x = int(input())
print("Введите y: ")
y = int(input())
print("Введите z: ")
z = int(input())

f = sqrt((39*(z ** 6) + z) / (2*(x ** 8) + (z ** 3))) - (((y ** 4) - y) / (((y ** 8)/89)- tan(y))) + sqrt (((y ** 7) + math.log(y) + 21) / ((z ** 6) + y ** 5))
print ('%.2e' % f)

print("_________________________________")

print("Задача:1.2")
print("Введите x: ")
x = int(input())


if(x < 97):
    {
        print('%.2e' % (tan(abs(x)) - (x**3) - 83))
    }

elif(x >= 97 & x < 121):
    {
       print('%.2e' % (abs(90*(x**7)) + 79*(x**4)))
    }

elif(x >= 121 & x < 217):
    (
        print('%.2e' % math.log(math.tan(cos(x))) - sin(x)),
    )

elif(x >= 217 & x < 268):
    {
        print('%.2e' % (math.log(72*x + 48*(x**8) + x**2 - 33)))
    }

elif(x>= 268):
    {
        print('%.2e' % (math.log(math.exp(x) + cos(x)) + math.exp(x) + 53))
    }

print("________________________________________________________________")

print("Задача:1.3")
import math
def ite(x,y):
	counter = 0
	for i in range(1,x+1):
		for j in range(1,y+1):
			counter+= 30 * (math.tan(y)-abs(x)-17)
		counter-= 90 * (abs(x) + 90 * (i**7))
	return "%.2e" % counter

x,y = int(input("Введите число n: ")),int(input("Введите число m: "))
print(ite(x,y))
print("_______________________________________________________________")

print("Задача:1.4")
print("Введите f: ")
n = int(input())

def f(n):
	if n == 0:
		return 2

	else:
		return cos(f(n-1)) + tan(f(n-1))

print('%.2e' % f(n))


