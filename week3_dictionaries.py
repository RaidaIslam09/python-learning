# ==========================================
# Week 3 : Dictionaries
# Author : Raida Tasnim Islam
# ==========================================

# --- Creating a dictionart ---
Customer = {
    "name" : "Raida",
    "city" : "Dallas",
    "sales" : 15000,
    "active" : True,
    "gpa" : 3.5

}

# --- Accessing value by key ---
print(Customer["name"])
print(Customer["sales"])
print(Customer["city"])
print(Customer["active"])

# --- Adding a new-key value pair ---
Customer ["company"] = "Dell"
print(Customer["company"])

# --- Updating a existing value ---
Customer ["sales"] = 18000
print (Customer["sales"])

# --- Looping through a dictionary ---
print()
print("Full Customer Profile")
for key, value in Customer.items():
    print(f"{key} : {value}")