"""
Q1.
write a python prog to calculate the electricity bill based on the following criteria:
if the units are consumed are less than or equal to 100, the cost per unit is $5
if the units are consumed are between 101 and 200, the cost per unit is $7
if the units consumed are more than 200, the cost per unit is $10
if the total bill exceeds $1500, add an extra charge of $200
"""
# units_consumed = int(input("Enter the number of units Consumed in Electricity: "))

# if units_consumed <= 100:
#     cost_per_unit = 5
# elif 101 <= units_consumed <= 200:
#     cost_per_unit = 7
# else:
#     cost_per_unit = 10

# total_bill = units_consumed * cost_per_unit
# if total_bill > 1500:
#     total_bill += 200
#     print("Extra charge added.")
# print(f"Total bill: {total_bill}")

# x = 15
# y = 10
# if x > 20:
#     print("A")
# elif x > 50:
#     print("B")
# elif y < 5:
#     print("C")
# else:
#     print("D") 

### FOR LOOPS
""" FOR always checks with the iteration"""
"""LIST"""
# x = ["Rahul", "Age","20"]
# for student in x:
#     print(x)

"""TUPLE"""
# x = ("Rahul", "Age","20")
# for student in x:
#     print(student)

"""DICTIONARY"""
# server = {
#     "name" : "webserver",
#     "status" : "running",
#     "cpu" : 75
# }
# for keys in server:
#     print(keys, server[keys])

"""LIST WITH FOR LOOP AND FORMATTED STRING"""
# friends = ["aman", "rohan", "pratham"]
# for friend in friends:
#     print(f"Good Morning", {friend})


# ### BREAK 
"""BREAK FUNCTION BREAKS THE FURTHER VALUE AFTER THE BREAK STATEMENT"""
# for number in range(1, 8):
#     if number == 4:
#         break
#     print(number) # 1 2 3

# ### CONTINUE
""" CONTINUE SKIPS THE PARTICULAR ITERATION"""
# for number in range(1, 8):
#     if number == 4:
#         continue
#     print(number) # 1 2 3 5 6 7 

# for number in range(1, 8):
#     if number == 4:
#         pass
#     else:
#         print(number)

# if x > 5:
#     pass

# command = "start"
# match command:
#     case "start":
#         print("starting server")
#     case "stop":
#         print("stopped server")
#     case "status":
#         print("server running")

# cpu_values = [30, 60, 85, 95]
# for cpu in cpu_values:
#     if cpu >= 80:
#         print(cpu, "%, High_Class Level")
#     else:
#         print(cpu, "%, Normal CPU")

# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1
    # i += 1

# readings = [0, 45, 82, 0, 67]
# for value in readings:
#     if value == 0:
#         continue
#     if value >= 80:
#         print(value, "high")
#     else:
#         print(value, "OK")

# times = [120, 240, 610, 180, 720]
# for t in times:
#     print("checking ", t)
#     if t > 500:
#         print("Slow response Found")
#         break
# print("scan complete")

# statuses = ["healthy", "maintainance", "failed"]
# for status in statuses:
#     if status == "maintenance":
#         pass
#     elif status == "failed":
#         print("Investigate")
#     print("status checked: ", status)

# servers = {
#     "web-1" : "runnning",
#     "web-2" : "stopped",
#     "DB-1" : "running",
#     "App-1" : "stopped"
# }
# for server, status in servers.items():
#     if status == "stopped":
#         print(server, "Active")
#     else:
#         print(server, "Inactive")

# ### FUNCTIONS
# def greet(): #declared function
#     print("hello") #function body
# greet() #fucntion call