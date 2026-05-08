# Simple If Statement

age = 18

if age >= 18:
    print("Eligible for Voting")

# Output:
# Eligible for Voting



# If-Else Statement

number = 10

if number % 2 == 0:
    print("Even Number")

else:
    print("Odd Number")

# Output:
# Even Number



# If-Elif-Else Statement

marks = 75

if marks >= 90:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")

# Output:
# Grade B



# Positive or Negative Number

num = -5

if num > 0:
    print("Positive Number")

elif num < 0:
    print("Negative Number")

else:
    print("Zero")

# Output:
# Negative Number



# Largest of Two Numbers

a = 20
b = 15

if a > b:
    print("A is Greater")

else:
    print("B is Greater")

# Output:
# A is Greater



# Largest of Three Numbers

a = 10
b = 25
c = 15

if a > b and a > c:
    print("A is Largest")

elif b > c:
    print("B is Largest")

else:
    print("C is Largest")

# Output:
# B is Largest



# Check Voting Eligibility

age = 16

if age >= 18:
    print("Can Vote")

else:
    print("Cannot Vote")

# Output:
# Cannot Vote



# Check Divisibility

num = 12

if num % 3 == 0 and num % 4 == 0:
    print("Divisible by 3 and 4")

else:
    print("Not Divisible")

# Output:
# Divisible by 3 and 4



# Nested If Statement

num = 15

if num > 0:

    if num % 2 == 0:
        print("Positive Even Number")

    else:
        print("Positive Odd Number")

else:
    print("Negative Number")

# Output:
# Positive Odd Number



# Check Leap Year

year = 2024

if year % 4 == 0:

    if year % 100 == 0:

        if year % 400 == 0:
            print("Leap Year")

        else:
            print("Not Leap Year")

    else:
        print("Leap Year")

else:
    print("Not Leap Year")

# Output:
# Leap Year



# Password Checking Example

password = "python123"

if password == "python123":
    print("Login Successful")

else:
    print("Wrong Password")

# Output:
# Login Successful



# Check Character Type

ch = 'A'

if ch.isalpha():
    print("Alphabet")

elif ch.isdigit():
    print("Digit")

else:
    print("Special Character")

# Output:
# Alphabet



# Student Pass or Fail

marks = 45

if marks >= 33:
    print("Pass")

else:
    print("Fail")

# Output:
# Pass



# ATM Balance Check

balance = 5000
withdraw = 2000

if withdraw <= balance:
    print("Transaction Successful")

else:
    print("Insufficient Balance")

# Output:
# Transaction Successful



# Find Smallest Number

a = 8
b = 3
c = 5

if a < b and a < c:
    print("A is Smallest")

elif b < c:
    print("B is Smallest")

else:
    print("C is Smallest")

# Output:
# B is Smallest



# Check Temperature

temp = 35

if temp > 40:
    print("Very Hot")

elif temp > 30:
    print("Hot")

elif temp > 20:
    print("Normal")

else:
    print("Cold")

# Output:
# Hot



# Login System Example

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login Successful")

else:
    print("Invalid Username or Password")

# Output:
# Login Successful



# Check Number Range

num = 25

if num >= 1 and num <= 50:
    print("Number is Between 1 and 50")

else:
    print("Out of Range")

# Output:
# Number is Between 1 and 50



# Real-Life Data Analytics Example

marks = [78, 45, 92, 30, 88]

for mark in marks:

    if mark >= 50:
        print(mark, "Pass")

    else:
        print(mark, "Fail")

# Output:
# 78 Pass
# 45 Fail
# 92 Pass
# 30 Fail
# 88 Pass



# Find Maximum Number Using Condition

numbers = [12, 45, 67, 23, 89]

maximum = numbers[0]

for num in numbers:

    if num > maximum:
        maximum = num

print("Maximum Number:", maximum)

# Output:
# Maximum Number: 89



# Check Vowel or Consonant

ch = 'e'

if ch in "aeiouAEIOU":
    print("Vowel")

else:
    print("Consonant")

# Output:
# Vowel
