# ### Dictionary
# """ A dictionary is a Python data structure that stores information as key-value pairs. 
# Each key is a label used to access its associated value.
# """
# student = {
#     "name" : "Rahul",
#     "age" : 24,
#     "course" : "BCA",
#     "city" : "Pune",
#     "city" : "Mumbai"
# }
# print(student)

# """Dictionary VS List"""
# students = ["rahul", "tia", "mia", "sia"]
# print(students[1])

# students = { "name" : "ria", "age" : 20, "course" : "BCS"}
# print(students["name"], students["age"])

# ec2 = {
# "instance_id": "i-123456",
# "instance_type": "t2.micro",
# "region": "ap-south-1",
# "state": "running"
# }
# print(ec2["instance_id"]) # i-123456
# print(ec2["region"]) # ap-south-1

# students = { "name" : "ria", "age" : 20}
# students["course"] = "BCA"
# print(students)

# ### GET METHOD : get(key)
# student = {
#      "name" : "Rahul",
#      "age" : 24,
#      "course" : "BCA",
#      "city" : "Pune",
#      "city" : "Mumbai"
# }
# print(student.get("age"))
# print(student.get("name"))

# ### KEYS() VALUES() ITEMS()
# student = {
#      "name" : "Rahul",
#      "age" : 24,
#      "course" : "BCA",
#      "city" : "Pune"
# }
# print(student.keys())
# print(student.values())
# print(student.items())

# ### LEN WITH DICT
# student = {
#      "name" : "Rahul",
#      "age" : 24,
#      "course" : "BCA",
#      "city" : "Pune"
# }
# print(len(student))

# ### Removing Dictionary Entries :
# ### POP(KEY)
# student = {"name": "Rahul", "age": 22, "course": "BCA"}
# student.pop("age")
# print(student) # age entry removed
# """pop(key) removes the named entry and returns its value. 
# If the key is missing and no default is supplied, it raises KeyError"""

# ### del ["key"]
# del student["course"]
# print(student)

# ### CLEAR .clear()
# """clear() removes all entries but leaves the dictionary itself available as an empty dictionary."""
# student.clear()
# print(student) # removed all enteries but leaves dictionary as empty dict

# ### Nested Dictionaries
# """A nested dictionary is a dictionary stored inside another dictionary. 
# It helps organize related groups of information."""
# students = {
#     "student1" : {"name" : "ria", "age" : 20},
#     "student2" : {"name" : "sia", "age" : 20}
# }
# print(students)
# print(students["student1"]["name"])
# print(students["student2"]["name"])

# aws = {
# "ec2": {"region": "ap-south-1", "type": "t2.micro"},
# "s3": {"bucket": "student-data"}
# }
# print(aws["ec2"]["region"]) # ap-south-1

# ### Different Data Types as Values
# """A dictionary can mix data types. 
# For example, name is a string, port is an integer, active is a Boolean, and tags is a list."""
# server = {
# "name": "WebServer",
# "port": 80,
# "active": True,
# "tags": ["training", "demo"]
# }

# ec2 = {
# "instance_id": "i-98765",
# "type": "t2.micro",
# "region": "ap-south-1",
# "status": "running"
# }
# # Try these tasks:
# # 1. Print the instance ID.
# print(ec2["instance_id"])
# # 2. Print the region.
# print(ec2["region"])
# # 3. Change status to "stopped".
# ec2["status"] = "Stopped"
# print(ec2["status"])
# # 4. Add an IP address.
# ec2["ip_address"] = "Pune 11"
# print(ec2)
# # 5. Print the number of fields
# print(ec2.keys())
# print(len(ec2))

# ### SETS
# """A set is a collection of distinct (unique) elements. 
# It is useful when duplicate values should be removed or when comparing membership across groups.
# Sets are unordered collections. Do not rely on the order in which elements are displayed."""
# num = (1, 77, 8, 24)
# print(num)

# cities = {"Pune", "Delhi", "Mumbai"}
# empty_set = set() # emptyset
# empty_dictionary = {} #empty dict

# ### Sets Do Not Support Indexing
# cities = {"Pune", "Delhi", "Mumbai"}
# # cities[0] # TypeError: sets are not subscriptable
# """A set is not organized by positions. 
# Use it for uniqueness and membership, not for retrieving an item by index."""

# ### ADD()
# cities = {"Pune", "Delhi"}
# cities.add("Mumbai")
# cities.add("Pune") # Pune is already present; no duplicate is added
# print(cities)

# ### remove() and discard()
# cities = {"Pune", "Delhi"}
# cities.remove("Delhi") # error if Delhi is absent
# cities.remove("Ratnagiri") # error if Ratnagiri is absent
# cities.discard("Mumbai") # no error if Mumbai is absent
# """remove(element) raises KeyError if the element is missing. 
# discard(element) does nothing if the element is missing."""

# ### len() with a Set
# skills = {"Python", "AWS", "SQL"}
# print(len(skills))

# ### Union — |
# # Union combines the elements from both sets without duplicates.
# students_python = {"Rahul", "Amit", "Priya"}
# students_aws = {"Amit", "Priya", "Ravi"}
# print(students_python | students_aws)
# # Contains Rahul, Amit, Priya, and Ravi
# ### Intersection — &
# # Intersection returns elements common to both sets.
# print(students_python & students_aws)
# # Contains Amit and Priya

# ### Difference — -
# # Difference returns elements in the left-hand set that are not in the right-hand set.
# print(students_python - students_aws)
# # Contains Rahul
# # Set output order is not guaranteed. Compare the members, not the printed order