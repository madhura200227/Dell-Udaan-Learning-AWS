
# Q a company wants to calculate an employees annual salary after adding a bonus
""" creates a var salary = 30000, create a var bonus = 5000,
calculate the total salary by adding the bonus to the salary,
use try and except to handle any errors that may occur during the calculation,
if the calculation is successful, print the total salary,
if an appropriate data type causes an error, print a message indicating that 
the calculation could not be performed due to invalid data type."""
# salary = 30000
# bonus = 5000
# total_salary = 0

# try:
#     total_salary = salary + bonus
#     print(f"Total salary: {total_salary}")
# except TypeError as e:
#     print(f"Error: {e}")

"""USER CREATED IMPORT MODULE """
# import my_module
# my_module.aws("EC2")

# import my_module
# my_module.say_hello("Madhura")
# from my_module import person1
# print(person1["name"])
# print(person1["age"])
# from my_module import person2
# print(person2["name"])
# print(person2["age"])

# example Q
"""square root of a number"""
# number = 16
# sqrt = number ** 0.5
# print(f"square root of the {number} is {sqrt}")

"""PRE-DEFINED OR IN BUILT IMPORT MODULES"""
# import math
# print(math.sqrt(20))
# print(math.factorial(2))
# print(math.pi)

# from math import sqrt
# print(sqrt(100))

# import math as m
# print(m.sqrt(9))
# print(m.factorial(5))
# print(m.pi)

""" import * (all = *)"""
# def sqrt(x):
#     return "normal function"
# from math import *
# print(sqrt(25))
"""when we use import * --> it overrides the function """

"""NUMPY MODULE"""
# to intsall python -m pip install numpy
# to check the version python -m pip show numpy
# import numpy as np
# numbers = np.array([10, 20, 30, 40, 50])
# print(f"the numbers are: {numbers}")
# print(np.sum(numbers))
# print(np.mean(numbers))

"""IMPORT RANDOM MODULE"""
# import random
# number = random.randint(1, 10)
# print(f"random number between 1 and 10 is : {number}")

# write a python prog to dice a number between 1 to 6
# import random
# roll_dice = random.randint(1, 6)
# print(f"the dice number is : {roll_dice}")

# RANDOM CHOICE 
""" random choice() method means to select a random element from a list"""


# RANDOM SHUFFLE
"""random shuffle() method means to shuffle the elements of a list randomly"""


# import random
# number = random.randrange(1, 20, 2)
# print(number)

#  DAY TIME MODULE
# import datetime 
# today = datetime.datetime.now()
# formatted_date = today.strftime("%d - %B - %Y")
# print(formatted_date)

# Q imagine you are working on an aws cloud project every time a new server is created you want to generate a random server id

"""expected output: aws server managment system, server id: 1234, created on: 2023-06-20"""

# import random
# import datetime
# server_id = random.randint(1000, 9999)
# current_date = datetime.datetime.now().strftime("%Y-%m-%d")
# print(f"aws server management system \nserver id: {server_id} \ncreated on: {current_date}\n")

# Q write a prog that asks user for a limit and prints all even numbers from 1 to that limit using a for loop and if else
# limit = int(input("Enter the limit: "))
# for i in range(1, limit + 1):
#     if i % 2 == 0:
#         print(i, "is even")
#     else:
#         print(i, "is odd")

# Q write a prog that asks the user to enter starting number and prints a countdown until 1.
# display goal reaches
# starting_number = int(input("Enter the starting number: "))
# for i in range(starting_number, 0, -1):
#     print(i)
# print("Goal reached!")

# Q a company wants to calculate an employees annual salary after adding a bonus
# (exception handling using try excepts) and handle type error if the salary or bonus is not a number.
# try:
#     annual_salary = 30000
#     bonus = 5000
#     # bonus = "5000"  # This is a string, which will cause a TypeError
#     total_salary = annual_salary + bonus
#     print(f"Total salary: {total_salary}")
# except TypeError:
#     print("Error: Please enter valid numbers for salary and bonus.")
# except Exception as e:
#     print(f"An error occurred: {e}")

# try:
#     data = open("config.txt")
# except FileNotFoundError:
#     print("file missing - using default configuration")
# else:
#     print("file opened successfully")
#     content = data.read()
#     print(f"loaded {len(content)} Characters")
# finally:
#     print("cleanup: closing file")

"""write a prog that asks user to enter an index and display the corresponding aws service"""
"""use try except to handle errors, if the user enters index, display invalid index
if user enters text instead of index, display invalid number use indexerror and valueerror"""

services = ["EC2", "S3", "RDS", "lambda"]

try:
    index = int(input("enter the index : \n"))
    print(f"the aws service is : {services[index]}")
except IndexError:
    print("invalid index")
except ValueError:
    print("invalid number")
