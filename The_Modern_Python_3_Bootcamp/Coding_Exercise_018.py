# Create a list called instructors
# Add the following strings to the instructors list "Colt" "Blue" "Lisa"

# Do it using append method
instructors = []
instructors.append("Colt")
instructors.append("Blue")
instructors.append("Lisa")
print(instructors)

# Do it using extend method
instructors = []
instructors.extend(["Colt", "Blue", "Lisa"])
print(instructors)

# Do it using insert method
instructors = []
instructors.insert(0, "Colt")
instructors.insert(1, "Blue")
instructors.insert(2, "Lisa")
print(instructors)