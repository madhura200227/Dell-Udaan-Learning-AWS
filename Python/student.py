"""create functions 
get_name() returns student name, 
get_course() returns student course, 
get_age() returns student age"""

name = input("Enter student name: ")
def get_name():
    return name

course = input("Enter student course: ")
def get_course():
    return course

age = int(input("Enter student age: "))
def get_age():
    return age

# import this module in main.py and call the functions to get the student name, course, and age.