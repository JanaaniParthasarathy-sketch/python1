# DICTIONARIES

# Creating Dictionary
student = {
    "name": "Janaani",
    "age": 18,
    "course": "AI & DS"
}

print("Original Dictionary:")
print(student)

# Access Values
print("Name:", student["name"])
print("Age:", student["age"])

# Add New Key
student["college"] = "HITS"

print("After Adding College:")
print(student)

# Loop Through Dictionary
print("Dictionary Contents:")
for key, value in student.items():
    print(key, ":", value)
