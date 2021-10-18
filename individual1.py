import math

first = input("Input cords separated with a whitespace: ").split()
second = input("Input cords separated with a whitespace: ").split()
third = input("Input cords separated with a whitespace: ").split()

for i in range(2):
    first[i] = int(first[i])
    second[i] = int(second[i])
    third[i] = int(third[i])

d1 = math.sqrt((second[1] - second[0]) ** 2 + (first[1] - first[0]) ** 2)
d2 = math.sqrt((third[1] - third[0]) ** 2 + (second[1] - second[0]) ** 2)
d3 = math.sqrt((first[1] - first[0]) ** 2 + (third[1] - third[0]) ** 2)

P = d1 + d2 + d3
p = P / 2
S = math.sqrt(p * (p - d1) * (p - d2) * (p - d3))

print("P =", P, "S =", S)
