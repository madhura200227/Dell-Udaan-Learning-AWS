'''
Q1. Create a text file student.txt write 3 details each on seperate file 
name : rahul, course : aws, duration : 3 months closed the file and 
print student data saved successfully 
'''

# file = open("student2.txt", 'w')
# file.write("name : Rahul\n", "course : aws\n", "duration : 3 months\n")
# file.close
# print("student data saved successfully")

# Q2.
"""student.txt already contains rahul and priya each on seperate line,
add amit and sneha on new line without deleting existing names display all four names open file in 'a' mode in append,
reopen it in read mode to display contents"""

# file = open("student.txt", 'a')
# file.write("Amit\n")
# file.write("Sneha\n")
# file.close
# file = open("student.txt", 'r')
# print(file.read())
# file.close

# Q3.
"""create a function named finde_bigger that accepts two numbers and returns the bigger number"""

# def find_bigger(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# print("Result: ",find_bigger(40, 60))

# Q4.
"""an aws practice lab has a list of EC2 instance status.
write program to count how many"""

### ERROR HANDLING
""" THE ART OF CONTROL"""
'''TRY, EXCEPT,'''

# ZERO DIVISION ERROR (dividing a number by zero)
# try: 
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Cannot Divide by zero!")

#  VALUE ERROR invalid value
# try:
#     age = int("Hello")
# except ValueError:
#     print("Invalid age!")

# TYPE ERROR invalid operation betwn data types
# try:
#     result = 10 + "Hello"
# except TypeError:
#     print("cannot add integer and string!")

# NAME ERROR invalid operation betwn variables
# try:
#     print(student_name)
# except NameError:
#     print("Variable is not defined")

# INDEX ERROR invalid index operation
# try:
#     numbers = [10, 20, 30]
#     print(numbers[5])
# except IndexError:
#     print("Index does not exist")


# KEY ERROR invalid key operation
# try:
#     student = {
#         "name" : "Rahul",
#         "age" : 10,
#     }
#     print(student["course"])
# except KeyError:
#     print("course key does not exist")

# MULTIPLE EXCEPT BLOCKS
# try:
#     a = int(input("Enter first num: "))
#     b = int(input("Enter second num: "))

#     result = a / b
#     # print("")

# except ZeroDivisionError:
#     print("dividing by zero")

# except ValueError:
#     print("Invalid value!")

# else:
#     print(a)
#     print(b)

# # FINALLY KEYWORD
# try:
#     a = int(input("Enter first num: "))
#     b = int(input("Enter second num: "))

#     result = a / b
#     # print("")

# except ZeroDivisionError:
#     print("dividing by zero is not allowed!")

# except ValueError:
#     print("Invalid value!")

# finally:
#     print("thankyou for using our prog")

# RAISE KEYWORD

# try:
#     age = int(input("Enter age: "))

#     if age < 18:
#         raise ValueError("age must be 18 or above")
#     print("you are eligible")
# except ValueError as e:
#     print("Error:", e)


# FILENOTFOUNFERROR
# file = None
# try:
#     file = open("student3.txt", "r")
#     content = file.read()
#     print(content)

# except FileNotFoundError:
#     print("File not found!")

# Q Create a simple ATM withdrawal program.
"""requirements: available balance is 5000
ask user to enter the amount to withdraw
if the withdrawal amount is greater than the available balance, raise value error
if amount is zero or negative, raise value error
if withdrawal is successful, print the remaining balance
handle invalid input and display a suitable meessage to the user
"""
"""hint : use try, except, raise, else, finally"""
# balance = 5000
# try:
#     amount = float(input("Enter the amount to withdraw: "))

#     if amount > balance:
#         raise ValueError("Withdrawal amount exceeds available balance.")
#     elif amount <= 0:
#         raise ValueError("Withdrawal amount must be greater than zero.")

#     balance -= amount # balance = balance - amount
#     print(f"Withdrawal successful. Remaining balance: {balance}")
    
# except ValueError as e:
#     print(f"Error: {e}")
