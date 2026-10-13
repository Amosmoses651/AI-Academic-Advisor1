
print("Welcome to the AI-Powered Academic Advisor System!")

student_name = input("Enter your name: ")
gpa = float(input("Enter your GPA: "))

print("\n--- Student Academic Profile ---")
print("Student:", student_name)
print("GPA:", gpa)

if gpa >= 3.5:
    print("Advice: Maintain your study habits and aim higher.")
elif gpa >= 2.5:
    print("Advice: Review difficult topics and practise regularly.")
else:
    print("Advice: Create a study timetable and seek academic support.")
