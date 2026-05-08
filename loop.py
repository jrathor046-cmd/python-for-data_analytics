# Simple For Loop

for i in range(1, 6):
    print("Number:", i)

# Output:
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Number: 5



# Even Numbers Using For Loop

for i in range(2, 11, 2):
    print(i)

# Output:
# 2
# 4
# 6
# 8
# 10



# Odd Numbers Using For Loop

for i in range(1, 10, 2):
    print(i)

# Output:
# 1
# 3
# 5
# 7
# 9



# Multiplication Table

num = 5

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50



# Sum of Numbers

total = 0

for i in range(1, 6):
    total += i

print("Total:", total)

# Output:
# Total: 15



# While Loop Example

count = 1

while count <= 5:
    print(count)
    count += 1

# Output:
# 1
# 2
# 3
# 4
# 5



# While Loop with Text

num = 1

while num <= 3:
    print("Hello")
    num += 1

# Output:
# Hello
# Hello
# Hello



# Infinite Loop Example

# while True:
#     print("Running Forever")



# Nested Loop Example

for i in range(1, 4):

    for j in range(1, 4):
        print(i, j)

# Output:
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3



# Star Pattern Using Nested Loop

for i in range(1, 6):

    for j in range(i):
        print("*", end="")

    print()

# Output:
# *
# **
# ***
# ****
# *****



# Break Statement Example

for i in range(1, 10):

    if i == 5:
        break

    print(i)

# Output:
# 1
# 2
# 3
# 4



# Continue Statement Example

for i in range(1, 6):

    if i == 3:
        continue

    print(i)

# Output:
# 1
# 2
# 4
# 5



# Pass Statement Example

for i in range(5):
    pass

# Output:
# No Output



# Loop with String

name = "Python"

for ch in name:
    print(ch)

# Output:
# P
# y
# t
# h
# o
# n



# Loop with List

numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)

# Output:
# 10
# 20
# 30
# 40



# Loop with Tuple

fruits = ("Apple", "Banana", "Mango")

for fruit in fruits:
    print(fruit)

# Output:
# Apple
# Banana
# Mango



# Loop with Dictionary

student = {
    "Name": "Aman",
    "Marks": 85
}

for key, value in student.items():
    print(key, value)

# Output:
# Name Aman
# Marks 85



# Loop with Set

colors = {"Red", "Blue", "Green"}

for color in colors:
    print(color)

# Output:
# Red
# Blue
# Green



# Student Marks Analysis

marks = [78, 85, 92, 67, 88]

total = 0

for mark in marks:
    total += mark

average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)

# Output:
# Total Marks: 410
# Average Marks: 82.0



# Find Maximum Number

numbers = [12, 45, 67, 23, 89]

maximum = numbers[0]

for num in numbers:

    if num > maximum:
        maximum = num

print("Maximum Number:", maximum)

# Output:
# Maximum Number: 89



# Count Vowels in String

text = "Data Analytics"

count = 0

for ch in text.lower():

    if ch in "aeiou":
        count += 1

print("Total Vowels:", count)

# Output:
# Total Vowels: 5



# Dictionary Values Example

employee = {
    "Aman": 25000,
    "Rahul": 30000,
    "Priya": 40000
}

for salary in employee.values():
    print(salary)

# Output:
# 25000
# 30000
# 40000



# Dictionary Keys Example

for name in employee.keys():
    print(name)

# Output:
# Aman
# Rahul
# Priya



# List Comprehension Example

numbers = [1, 2, 3, 4, 5]

squares = [x**2 for x in numbers]

print(squares)

# Output:
# [1, 4, 9, 16, 25]



# Nested List Example

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:

    for value in row:
        print(value)

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
