# Student Performance Analytics
# Requirement: RQ1 - Student Performance Data Analysis

students = [
    {"id": 101, "marks": [45, 48, 50], "attendance": 62},
    {"id": 102, "marks": [55, 60, 58], "attendance": 75},
    {"id": 103, "marks": [70, 72, 68], "attendance": 85}
]

for student in students:
    marks = student["marks"]
    attendance = student["attendance"]

    if len(marks) == 0:
        continue

    average = sum(marks) / len(marks)

    if average < 50 or attendance < 60:
        risk_level = "High"
    elif average < 65:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    print(
        "Student ID:", student["id"],
        "| Average:", round(average, 2),
        "| Attendance:", attendance,
        "| Risk Level:", risk_level
    )
