### IF CONDITION
# marks = 60
# # print(marks)
# if marks >= 65:
#     print("pass")
# print("Fail")

# ### IF ELSE CONDITION
# marks = 35
# if marks >= 65:
#     print("pass")
# else : 
#     print("Fail")
# server_running = False
# if(server_running):
#     print("Server is running")
# else:
#     print("server stopped")

# ### ELIF CONDITION
# age = 20
# if age < 13:
#     print("child")
# elif age < 18:
#     print("Teenager")
# elif age < 65:
#     print("Adult")
# else:
#     print("Senior")

# cpu_usage = 95
# if cpu_usage >= 90:
#     print("CPU usage is high")
# elif cpu_usage >= 45:
#     print("CPU usage is Normal") 
# """ always write high threshold condition"""
# """the correct sequence is : """


# servers = [
#     ["webserver", "running"],
#     ["dbserver", "stopped"]
# ]
# print(servers[0][1])


# registered = True
# fee_paid = True
# if (registered and fee_paid):
#     print("Lab access is granted")
# else:
#     print("Lab access is denied")

# cpu_high = False
# disk_full = True
# if cpu_high or disk_full:
#     print("send maintainace alert")
# else:
#     print("no alert needed")

# server_running = False
# if not server_running:
#     print("Start Investigation")


# ### NESTED IF CONDITION
# user_logged_in = True
# admin_user = False
# if user_logged_in:
#     if admin_user == False:
#         print("Admin access Granted")
#     else:
#         print("Normal user Grandted")
# else:
#     print("Please log in again")

# score = 85
# passed = True

# if passed:
#     if score >= 90:
#         print("Grade A")
#     elif score >= 75:
#         print("Grade B")
#     else:
#         print("Grade C")
# else:
#     print("Failed No grade Assigned")

### FOR LOOP
""" FOR always checks with the iteration"""
# for i in range(5):
#     print(i) 
# """ RANGE Always start from 0 to 5 but end is excluded so the output is : 0 1 2 3 4 """

# for i in range(1, 11):
#     print(i)

# for i in range(1, 11, 2):
#     print(i)

### WHILE CONDITION
""" WHILE always check with the condition"""
# i = 1
# while i <= 3:
#     print(i)
#     i = i + 1