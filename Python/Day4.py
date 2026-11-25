#Q.6 
# data = [
#     ["S3", 500],
#     ["EBS", 100],
#     ["EFS", 250]
#     ]

# print(data)
# print("s3 storage : ", data[0][1])
# print("EBS storage : ", data[1])

# result = data[0][1] + data[1][1]
# print("the sum of S3 and EBS: ",result)

# data[2][1] = 300
# print(data)

#Q.7

# data = [
#     ["Compute: ", "EC2", "Lambda"],
#     ["Storage: ", "S3", "EBS"],
#     ["Database: ", "RDS", "DynamoDb"]
# ]
# print(data)
# print("compute: ", data[0][1])
# print(data[1][1])
# print(data[1][2])
# print(data[2][2])

# data[2][2] = "ECS"
# print(data)

### TUPLE
"""tuple is a ordered collection of the elements which is immutable """

# student = "AWS"
# student1 = ["rahul", 20, True]
# student1[0] = "Akansh"
# print(student1)

# tuple1 = ("Rahul")
# print(tuple1)
# print(type(tuple1))

# tuple2 = ("Rahul",)
# print(tuple2)
# print(type(tuple2))

# tuple3 = ("Rahul", "BCA", True, 338)
# print(tuple3)
# print(type(tuple3))

"""becuase tuples are immutable that is we cannot change the values or elements in tuple"""
# print(tuple3[1]) = "AWS"
# print(tuple3)

### SLICING INDEXING IN TUPLE

# aws_service = ("EC2", "S3", "Lambda","RDS","VPC")
# print(aws_service[0])
# print(aws_service[1])
# print(aws_service[2])
# print(aws_service[3])
# print(aws_service[4])

# print(aws_service[0 : 3 : 2])
# print(aws_service[2 : 3])
# print("reversing the tuple through slicing: ",aws_service[ : : -1]) 
# lenght1 = len(aws_service)
# print(lenght1)

### MEMBERSHIP OPERATOR ( NOT IN AND IN)

# services = ("EC2","S3","Lambda")
# print("S3" in services)
# print("Azure" not in services)
# print("EC2" not in services)

### DIFFERENCE IN MUTABLE IN IMMUTABLE

# services = ["EC2","S3","Lambda","AWS","Azure","RDS","VPC"]
# print(services)
# services[0] = "Microsoft"
# print(services)

# services = ("EC2","S3","Lambda","AWS","Azure","RDS","VPC")


# data = ("AWS",["EC2", "S3"])
# print(data)
# data[0] = "Azure" because tuple is immutable
# data[1] = "Azure" because tuple is immutable

# data = ("AWS", ["EC2", "S3"])
# data[1].append("Lambda")
# print(data)
# data[1].pop(0)
# print(data)

###PACKING
"""packing is a process of storing multiple values in a single variable"""
# server = "web-server", "db-server", "app-server"
# print(type(server))
# print(server)

###UNPACKING
"""that is it stores different values in different variables"""
# server = "web-server", "db-server", "app-server"
# print(server)
# name, instance, OS = server
# print("name: ", name)
# print("instance: ", instance)
# print("OS: ", OS)

# service = ("EC2","VPC","Region")
# instance, network, cloud = service
# print("instance: ", instance)
# print("network: ", network)
# print("cloud: ", cloud)

# service = ("EC2","VPC","Region")
# instance, network, ap_south = service
# print("instance: ", instance)
# print("ap-south: ", ap_south)
# print("network: ", network)

"""number values should be equal to the number of variables in unpacking otherwise it will give error"""

# servers = (
#     ("web-server", "t2.micro"),
#     ("database-server", "t3.micro"),
# )
# print(servers)
# print(servers[0][1])
# print(servers[1][1])

### TUPLE METHODS in python 1. count() 2. index()
"""COUNT : it counts the number of occurences of a particular element in a tuple"""
"""INDEX : it returns the index of a particular element in a tuple"""

# aws = ("EC2", "EC2", "S3", "RDC", "Lambda", "RDS", "VPC")
# print(aws.count("EC2"))
# print(aws.index("S3"))

# server = "Cloud1", "Cloud2", "Cloud3"

### CONCATENATION
# services = aws + server
# print(services)

###REPITION
# result = aws * 4
# print(result)


# ### CONVERTING LIST into TUPLE
# services = ["EC2", "S3", "Lambda", "RDS", "VPC"]
# print(type(services))
# services_tuple = tuple(services)
# print(services_tuple)

# ### CONVERTING TUPLE into LIST
# services1 = "EC2", "S3", "Lambda", "RDS", "VPC"
# print(type(services1))
# services1_list = list(services)
# print(services1_list)

# Q1.

# aws = "EC2", "S3", "Lambda", "RDS", "DynamoDB"
# print(aws[0])
# print(aws[4])
# print(aws[2])
# print("S3" in aws)
# print("lenght: ", len(aws))

# Q2.

# servers = (
#     ("web-server", "t2.micro"),
#     ("db-server", "t3.micro")
# )

# print(servers[0][0])
# print(servers[0][1])

# Q3.

student_name = "Amit"
skills = ["python","aws","sql"]

student_tuple = ["Amit : ", "python","aws","sql"]
print("student name and their skills : ", student_tuple)

# Q4.

project = (
    "student portal",
    "EC2",
    "ap-south-1",
    80,
    "running"
)    
print("project name: ", project[0])
print("aws_service: ", project[1])
print("region: ", project[2])
print("port: ", project[3])
print("status: ", project[4])
