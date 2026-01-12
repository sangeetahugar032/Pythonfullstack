courses = {
    "Python":5000,
    "data analytics":8000,
    "ai & ml":12000
}
course_name = input("Enter course name:").lower()
is_student = input("Are you a student? (yes/no):").lower()
early_registration = input("Early registration? (yes/no):").lower()

if course_name in courses:
    original_fee = courses[course_name]
    discount = 0

    if is_student == "Yes":
        discount += original_fee * 0.10

    if early_registration == "yes":
        discount += original_fee * 0.05

    final_amount = original_fee - discount
    print("\n---- Fee Bill ----")
    print("Course Name :", course_name.title())
    print("Original Fee :$", original_fee)
    print("Total Discount :$", discount)
    print("Final payable Amt :$",final_amount)

else:
    print("Invalid course selected!")
