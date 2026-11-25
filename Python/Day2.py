# name = "AWS"
# "AWS" is a string in a sequence of characters, so it is a string data type

# Aws = "12345"
# float = "19.33"
# symbol = "@#$%^&*()"
# string data type

# a = 30
# b = "50" 
# print(a + b) we cannot make addition with int and str
#  i want the output 80
# a = 30
# b = 50
# print(a + int(b))

# a = 30.2
# b = "43.2"
# #  i want output 73.4
# print(a + float(b))

# name = 'aws'
# name1 = """
# i am learning aws
# """
# print(name)
# print(name1)
# output 
'''aws

i am learning aws'''

# name2 = "aws"
# name2[0] = "b"
# strings are immutable (we cannot change them)
# output:  
'''name2[0] = "b"
    ~~~~~^^^
TypeError: 'str' object does not support item assignment'''

# INDEXING METHOD
#  P   Y   T   H   O   N
#  0   1   2   3   4   5 
# -6  -5  -4  -3  -2  -1

# lenght
# name = "python"
# print(len(name))

# name1 = "aws services"
# print(len(name1))

# string slicing
'''string (start(n) : end(n - 1))
start is included and end is excluded''' 

# name = "Python"
# print(name[0 : 3])

# provide me the output of amazon in console
# provide me the output of web in console
# text = "Amazon Web Services"
# print(text[0 : 6]) # amazon
# print(text[7 : 10]) # web

# name = "Python"
# print(name[1 : ])
# print(name[ : 5])
# print(name[-5 : -1])

# String Slicing
"""
String Slicicng with step
string[start : end : step] 
Step means here JUMP
"""
# name = "Python"
# print(name[0 : 6 : 2])
# print(name[0 : 6 : 1])
# print(name[1 : 6 : 3])
# print(name[  :   : -1])

# # String methods 
# '''Concatenation = Adding of Two Strings'''
# first = "AWS"
# second = "Cloud"
# print(first + second)
# print(first + " " + second)

# '''Repeatation of Strings'''
# text = "AWS"
# print(text * 2)

# '''Operators in String'''
# text = "AWS Cloud Computing"
# print("AWS" in text) 
# '''in to check the string is appearing in the variable text and give output in boolean values (True or False)'''

#Upper Case, Lower Case
# text = "AWS CLOUD"
# print(text.lower())

# text1 = "pyhton"
# print(text1.capitalize()) #makes only first letter capital of only first word
# print(text1.upper())

# text2 = "amazon web services"
# Amazon Web Services
# print(text2.title()) # make first letter capital of each word

# #Important String methods
# name = "   Madhura   "
# print(name)
# # STRIP : is a method  use to remove the extra spaces from the start and end
# print(name.strip())
# region = "   us-east-1   "
# print(region.strip())

# # REPLACE 
# '''REPLACE command replaces the new word'''
# services = "AWS Cloud"
# print(services.replace("AWS", "Azure"))
# services1= "EC2 Cloud Server"
# print(services1.replace("EC2","instance server"))

# # Split() : String -> List
# ''' Most Important Split() : it converts strings into list'''
# text = "AWS, CLoud, Python"
# print(text)
# print(text.split())
# data = "EC2, S3, Lambda, RDS"
# print(data.split())

# # JOIN 
# '''with the JOIN Method we can convert list into string'''
# services = ["EC2","S3","Lambda","RDS"]
# result = ",".join(services)
# print(result)

# # COUNT
# '''counts the str in one line'''
# data1 = "AWS AWS AWS AWS AWS"
# print(data1.count("AWS"))

# # startswidth
# region = "us-east-1"
# print(region.startswith("us"))

# # endswith
# file = "server-log"
# print(file.endswith("log"))

# #data type by default is tring for the input function
# college = input("Enter The College the Name") 

# # convert string input into int input
# age = int(input("enter the age: "))
# print(type(age))

# Formatting the STring
# ''Hello I'm Learningthe AWS Cloud Computing'''
# var1 = "Learning"
# var2 = "AWS"
# print(f" Hello I'm {var1} the {var2} Cloud Computing")'

# Question 1
# Student = "Rahul"
# Course = "AWS Cloud"
# Batch = "Batch1"
# print(f"{Student} {Course} {Batch}")

# Question 2

# the output should be : "s3://my-student-data/Student.csv"
# a1 = "s3:"
# a2 = "//my-student-data/"
# a3 = "Student.csv"
# print(f"\n {a1}{a2}{a3}")


### PDF 6TH OF OCTOBER 2026

# ============================================================
# Python Strings for AWS Cloud
# Student Handout — Lessons 1 to 23
# ============================================================

# Learning Goal:
# Learn Python strings from basic concepts to practical
# AWS-related examples.
#
# You will learn how to:
# create, access, slice, search, clean and format strings.


# ============================================================
# LESSON 1 — What is a String?
# ============================================================

# A string is text inside quotation marks.
# Its Python type is str.

name = "Deepak"
course = "AWS Cloud"

print(name)
print(type(course))

# AWS / Practical Connection:
# AWS resource names, regions, statuses, URLs and messages
# are commonly strings.


# ============================================================
# LESSON 2 — Creating Strings
# ============================================================

# Single and double quotes can both create strings.

name1 = 'Deepak'
name2 = "Deepak"

print(name1)
print(name2)

# AWS / Practical Connection:
# Use the quotation style that makes your text easy to read.


# ============================================================
# LESSON 3 — String vs Number
# ============================================================

# A value such as 100 is an integer,
# while "100" is a string.

x = 100
y = "100"

print(type(x))
print(type(y))

# AWS / Practical Connection:
# Cloud IDs and codes may look numeric but are usually
# handled as text.


# ============================================================
# LESSON 4 — Multi-word Strings
# ============================================================

# Spaces are characters and can be part of a string.

text = "AWS Cloud Computing"

print(text)
print(len(text))

# AWS / Practical Connection:
# Cloud descriptions, names and user input commonly
# contain spaces.


# ============================================================
# LESSON 5 — Multi-line Strings
# ============================================================

# Triple quotes allow strings to span multiple lines.

message = """Welcome to AWS
Today we learn Python
Python helps with cloud automation"""

print(message)

# AWS / Practical Connection:
# Useful for messages, documentation and text templates.


# ============================================================
# LESSON 6 — Immutability
# ============================================================

# Strings are immutable:
# you cannot change one character directly after creation.

name = "AWS"

# This will cause an error:
# name[0] = "B"

# Instead, create a new string.

name = "BWS"

print(name)

# AWS / Practical Connection:
# To change text, create a new string value.


# ============================================================
# LESSON 7 — Indexing
# ============================================================

# Indexing accesses one character.
# Python starts counting at 0.

name = "PYTHON"

print(name[0])
print(name[1])
print(name[3])

# Index map:
#
# P = 0
# Y = 1
# T = 2
# H = 3
# O = 4
# N = 5

# AWS / Practical Connection:
# Indexing can be used when working with parts of text.


# ============================================================
# LESSON 8 — Negative Indexing and len()
# ============================================================

# Negative indexes count from the end.
# len() gives the number of characters.

name = "PYTHON"

print(name[-1])
print(name[-2])
print(len(name))

# AWS / Practical Connection:
# Useful for accessing the last characters
# and finding total text length.


# ============================================================
# LESSON 9 — Slicing
# ============================================================

# Syntax:
# string[start:end]
#
# Start is included.
# End is excluded.

name = "PYTHON"

print(name[0:3])
print(name[2:5])
print(name[:3])
print(name[3:])

# AWS / Practical Connection:
# Slicing is useful for extracting parts of resource
# names or text.


# ============================================================
# LESSON 10 — Slicing With Step
# ============================================================

# Syntax:
# string[start:end:step]
#
# Step controls how characters are selected.

text = "PYTHON"

print(text[0:6:2])

# A step of 2 takes every second character.

# AWS / Practical Connection:
# Useful when selecting characters at regular intervals.


# ============================================================
# LESSON 11 — Reverse a String
# ============================================================

# A step of -1 moves backward through the string.

text = "PYTHON"

print(text[::-1])

# Output:
# NOHTYP

# AWS / Practical Connection:
# String slicing can be used to reverse text.


# ============================================================
# LESSON 12 — Concatenation
# ============================================================

# The + operator joins strings.

first = "AWS"
second = "Cloud"

result = first + " " + second

print(result)

# AWS / Practical Connection:
# Useful for building names, messages and paths.


# ============================================================
# LESSON 13 — Repetition
# ============================================================

# The * operator repeats a string.

text = "AWS "

print(text * 3)

# AWS / Practical Connection:
# Useful for simple repeated text.


# ============================================================
# LESSON 14 — Membership: in
# ============================================================

# in checks whether text exists inside another string.

text = "AWS Cloud Computing"

print("AWS" in text)
print("Python" in text)

# AWS / Practical Connection:
# Useful for checking keywords or service names.


# ============================================================
# LESSON 15 — Membership: not in
# ============================================================

# not in checks that text is absent.

text = "AWS Cloud"

print("Azure" not in text)
print("AWS" not in text)

# AWS / Practical Connection:
# Membership checks are often used with if statements.


# ============================================================
# LESSON 16 — Case Methods
# ============================================================

# upper(), lower(), capitalize() and title()
# change text presentation.

text = "amazon web services"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())

# AWS / Practical Connection:
# Useful for normalizing user input
# and displaying clean text.


# ============================================================
# LESSON 17 — strip() and replace()
# ============================================================

# strip() removes outside spaces.
#
# replace(old, new) replaces matching text.

# name = " Deepak "

# print(name.strip())

# text = "I use Azure"

# print(text.replace("Azure", "AWS"))

# AWS / Practical Connection:
# Very useful for cleaning user input
# and controlled text transformation.


# ============================================================
# LESSON 18 — split()
# ============================================================

# split() breaks a string into a list.

# services = "EC2,S3,Lambda,RDS"

# service_list = services.split(",")

# print(service_list)

# AWS / Practical Connection:
#
# String -> split() -> List


# ============================================================
# LESSON 19 — join()
# ============================================================

# join() combines list items into one string.

# services = ["EC2", "S3", "Lambda"]

# result = ", ".join(services)

# print(result)

# AWS / Practical Connection:
#
# List -> join() -> String


# ============================================================
# LESSON 20 — find()
# ============================================================

# find() returns the position of the first matching
# substring.
#
# If the substring is not found, it returns -1.

# text = "AWS Cloud Computing"

# print(text.find("Cloud"))
# print(text.find("Python"))

# AWS / Practical Connection:
# Useful for locating text within larger values.


# ============================================================
# LESSON 21 — count()
# ============================================================

# count() tells how many times a substring occurs.

# text = "AWS AWS AWS"

# print(text.count("AWS"))

# AWS / Practical Connection:
# Useful for simple text analysis.


# ============================================================
# LESSON 22 — startswith()
# ============================================================

# startswith() returns True if a string begins
# with the specified text.

# region = "ap-south-1"

# print(region.startswith("ap-"))
# print(region.startswith("us-"))

# AWS / Practical Connection:
# You can classify region strings by prefix.
#
# Note:
# This is not API validation.


# ============================================================
# LESSON 23 — endswith()
# ============================================================

# endswith() returns True if a string ends
# with the specified text.

filename = "server.log"

if filename.endswith(".log"):
    print("This is a log file")
else:
    print("This is not a log file")

# AWS / Practical Connection:
# Cloud applications commonly generate log files
# that can be processed by Python.


# ============================================================
# PRACTICE QUESTIONS
# Lessons 1 to 23
# ============================================================

# 1. Create strings for your name, course and city
#    and print them.

# 2. Explain the difference between 100 and "100".

# 3. Print the first and last character of "AWS Cloud".

# 4. Find the length of "Amazon Web Services".

# 5. Extract "AWS" from "AWS Cloud" using slicing.

# 6. Reverse "PYTHON" using slicing.

# 7. Join "AWS" and "Cloud" using +.

# 8. Check whether "Lambda" is in "AWS Lambda Service".

# 9. Convert "aws cloud" to uppercase.

# 10. Remove spaces from " ap-south-1 ".

# 11. Replace "Azure" with "AWS" in a sentence.

# 12. Split "EC2,S3,Lambda,RDS" into a list.

# 13. Join ["EC2", "S3", "Lambda"] using ", ".

# 14. Find "Cloud" in "AWS Cloud Computing".

# 15. Count "AWS" in "AWS AWS AWS".

# 16. Check whether "ap-south-1" starts with "ap-".

# 17. Check whether "application.log" ends with ".log".


# ============================================================
# AWS MINI PROJECT
# ============================================================

# Create a small program that collects cloud information
# and formats it cleanly.

student = input("Enter student name: ")
region = input("Enter AWS region: ")
service = input("Enter AWS service: ")
status = input("Enter instance status: ")

student = student.strip().title()
region = region.strip().lower()
service = service.strip().upper()
status = status.strip().lower()

print("\n========== AWS Cloud Information ==========")

print(f"Student: {student}")
print(f"Region: {region}")
print(f"Service: {service}")
print(f"Status: {status}")

print("============================================")


# ============================================================
# REMEMBER
# ============================================================

# Strings are fundamental to AWS automation because programs
# work with:
#
# - Instance IDs
# - Regions
# - Service names
# - Resource names
# - URLs
# - File names
# - Statuses
# - Configuration values