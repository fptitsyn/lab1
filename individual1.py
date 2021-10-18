import math

first = input("Input cords separated with a whitespace: ")
second = input("Input cords separated with a whitespace: ")
third = input("Input cords separated with a whitespace: ")

a1 = first.split()
a2 = second.split()
a3 = second.split()

for i in range(2):
    a1[i] = int(a1[i])

d1 = math.sqrt((second[1] - second[0]) ** 2 + (first[1] - first[0]) ** 2)
