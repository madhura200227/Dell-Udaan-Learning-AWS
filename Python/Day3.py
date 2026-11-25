# project = "student"
# environments = "production"
# service = "EC2"
# """OUTPUT : student_production_EC2"""
# print(f"{project}_{environments}_{service}")

# create a prog that accepts from user 

"""
student, region, service, status, 
and the output : 
student : Rahul
region : ap-south-1
service : EC2
status : RUNNING
"""

# student = input("Enter student name : ")
# region = input("Enter AWS region : ")
# service = input("Enter AWS service: ")
# status = input("Enter AWS status : ")

# student = student.strip().title()
# region = region.strip().lower()
# service = service.strip().upper()
# status = status.strip().upper()

# print("---AWS Information---")
# print(f"student : {student}")
# print(f"region : {region}")
# print(f"service : {service}")
# print(f"status : {status}")

# string = "AWS"
# string[0] = "B"
# print(string)

# list1 = ["AWS","S3","VPC"]
# print(list)
# list is a collection of multiple values in a single list
# list can store multiple values with different data types
# list stores multiple values in a single variable

# server1 = "AWS1"
# server2 = "AWS2"
# server3 = "AWS3"
# server = ["AWS1","AWS2","AWS3"]
# data = ["AWS",123,12.10,True]
# print(server)
# print(data)
# print(server1[0])
# print(server1[-2])

# services = ["EC2", "S3","VPC"]
# """
# replace VPC with RDS
# """
# services[2] = "RDS"
# print(services)

# region = ["london", "mumbai", "pune"]
# print(region)
# region[0] = "ratnagiri"
# print(region)

### APPEND 
"""IT ADDS ONE ELEMENT AT LAST """

# services = ["AWS","S3"]
# services.append("RDS")
# print(services)

### EXTEND 
""" IT ADDS MULTIPLE ELEMENTS"""
# services = ["AWS", "S3"]
# services.extend(["RDS", "VPC"])
# print(services)

# region = ["a","b","c"]
# region.extend(["d","e","f"])
# print(region)

### INSERT
"""list insert the value in the given index (index, value)"""
# services = ["AWS", "S3"]
# services.insert(1,"VPC")
# print(services)

### REMOVE VALUES
"""removes the value directly """
# services = ["AWS", "S3", "VPC"]
# services.remove("VPC")
# print(services)

### POP
"""POP REMOVES OR DELETES THE VALUE THROUGH ITS INDEX"""
# services = ["AWS", "S3","RDS","VPC"]
# services.pop(2)
# print(services)

# data = ["java","tcs","python","os"]
# data.pop()
# print(data)
# a = data.pop(2)
# print(a)
#### POP GIVES RETURN VALUE 
""" IN POP IF WE DOES NOT GIVE INDEX IT AUTOMATICALLY REMOVES OR DELETES THE LAST INDEX VALUE"""

### DELETE
""" del removes THE VALLUE FROM THE GIVEN INDEXING 
"""
# services = ["AWS", "S3","RDS","VPC"]
# del services[1]
# print(services)

### CLEAR 
""" CLEAR: IT MAKES LIST EMPTY 
"""
# data = ["java","tcs","python","os"]
# data.clear()
# print(data)

### lenght
""" len : it gives total number of elements
"""
# data = ["java","tcs","python","os"]
# len(data)
# print(data)

### IN 
""" IN CHECKS IF THE VALUE OR ELEMENT IS PRESENT IN THE LIST OR NOT
"""
# data = ["java","tcs","python","os"]
# print("os" in data)
# print("ds" in data)

### MAX MIN SORT 
# cpu_usage = [20, 45, 30, 100, 102]
# print(max(cpu_usage))
# print(min(cpu_usage))
# print(sum(cpu_usage))

# cpu_usage.sort()
# print(cpu_usage)

### REVERSE
# cpu_usage = [20, 45, 30, 100, 102]
# cpu_usage.reverse()
# print(cpu_usage)

### NESTED LIST 

# server = [
#     ["webserver", "runnning"],
#     ["dbserver","start"]
# ]
# print(server[0][0])
# print(server[0][1])
# print(server[1][0])
# print(server[1][1])

#Q1.CREATE A LIST CONTAINING FIVE STUDENT NAMES: rahul, priya, amit, sneha, and rohit
# tasks : a] print the complete list, b]print the first student, c] print the last student, d] change amit to aman

# student = ["Rahul", "Priya", "Amit", "Sneha","Rohit"]
# print(student)
# print(f"the students names are : {student}")
# print(student[0])
# print(student[-1])
# student[2] = "Aman"
# print(student)

#Q2.list[EC2, S3, RDS, LAMBDA, VPC 

# aws_service = ["EC2", "S3", "RDS", "LAMBDA", "VPC"]
# print(aws_service[0])
# print(aws_service[2])
# aws_service.append("cloudfront")
# aws_service.remove("VPC")
# print(aws_service)

#Q3. list named ec2 server 

server = ["Running","stopped","Running","Running"]
print(server)
server[1] = "Running"
print(server)
server.append("Stopped")
print(server)
len(server)
print(len(server))

#Q4. nested

data = [
    ["Rahul", 20, "BCA"],
    ["Priya", 21, "BSc CS"],
    ["Amit", 22, "MCA"]
]
print("rahul's name : ",data[0][0])
print("priya's age : ",data[1][1])
print("amit's course : ",data[2][2])

data[0][1] = 21
print(data)
      
