students={
    "Asha":"Python",
    "Ravi":"Data Analytics",
    "Neha":"Ai"
}
print("Student Names:")
for name in students.keys():
    print(name)
print("\nEnrolled Coureses:")
for course in students.values():
    print(course)
name=input("\nEnter student name to check:")
if name in students:
    print(name,"is enrolled in",students[name])
else:
    print(name,"does not exist")
