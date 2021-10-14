import math

x = 1.7
a = 0.5
b = 1.08
c = 2.1
m = 0.7

s = math.exp(-a * x) * math.sqrt(x + 1) + math.exp(-b * x) + math.sqrt(x + 1.5)
z = math.sin(x) / (math.sqrt(1 + m * m * math.sin(x * x)) / (-c * m * math.log(m * x)))

print("s =", s, "z =", z)
