# Simple For Loop

for i in range(1, 6):
    print("Number:", i)



# Even Numbers Using For Loop

for i in range(2, 11, 2):
    print(i)



# Odd Numbers Using For Loop

for i in range(1, 10, 2):
    print(i)



# Multiplication Table

num = 5

for i in range(1, 11):
    print(num, "x", i, "=", num * i)



# Sum of Numbers

total = 0

for i in range(1, 6):
    total += i

print("Total:", total)



# While Loop Example

count = 1

while count <= 5:
    print(count)
    count += 1



# While Loop with Text

num = 1

while num <= 3:
    print("Hello")
    num += 1



# Infinite Loop Example

# while True:
#     print("Running Forever")



# Nested Loop Example

for i in range(1, 4):

    for j in range(1, 4):
        print(i, j)



# Star Pattern Using Nested Loop

for i in range(1, 6):

    for j in range(i):
        print("*", end="")

    print()



# Break Statement Example

for i in range(1, 10):

    if i == 5:
        break

    print(i)



# Continue Statement Example

for i in range(1, 6):

    if i == 3:
        continue

    print(i)



# Pass Statement Example

for i in range(5):
    pass



# Loop with String

name = "Python"

for ch in name:
    print(ch)



# Loop with List

numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)



# Loop with Tuple

fruits = ("Apple", "Banana", "Mango")

for fruit in fruits:
    print(fruit)



# Loop with Dictionary

student = {
    "Name": "Aman",
    "Marks": 85
}

for key, value in student.items():
    print(key, value)



# Loop with Set

colors = {"Red", "Blue", "Green"}

for color in colors:
    print(color)



# Student Marks Analysis

marks = [78, 85, 92, 67, 88]

total = 0

for mark in marks:
    total += mark

average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)



# Find Maximum Number

numbers = [12, 45, 67, 23, 89]

maximum = numbers[0]

for num in numbers:

    if num > maximum:
        maximum = num

print("Maximum Number:", maximum)



# Count Vowels in String

text = "Data Analytics"

count = 0

for ch in text.lower():

    if ch in "aeiou":
        count += 1

print("Total Vowels:", count)



# Dictionary Values Example

employee = {
    "Aman": 25000,
    "Rahul": 30000,
    "Priya": 40000
}

for salary in employee.values():
    print(salary)



# Dictionary Keys Example

for name in employee.keys():
    print(name)



# List Comprehension Example

numbers = [1, 2, 3, 4, 5]

squares = [x**2 for x in numbers]

print(squares)



# Nested List Example

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:

    for value in row:
        print(value)
