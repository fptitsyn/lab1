import math

a = 10.2
b = 9.2
c = 0.5
x = float(input())

f = math.log(a + x * x) + math.sin(x / 6) ** 2
z = math.exp(-c * x) * ((x + math.sqrt(x + a)) / (x - math.sqrt(x - b)))

print("f =", f)
print("z =", z)
