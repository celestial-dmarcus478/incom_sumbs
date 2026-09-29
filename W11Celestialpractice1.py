students={
    "Ana": 85,
    "Ben": 98,
    "Carlo": 78,
    "Diana": 95
}
print("STUDENT GRADES")
print("-"*8)
print("Ana", students["Ana"])
print("Ben", students["Ben"])
#Add new student
students["Ella"]=88
#update grade
students["Carlo"]=82
students["Diana"]=91
name1=input("enter name")
grade1 = int(input("enter grade"))
students[name1] = grade1
print(students)
print("\nUpdated Student Grades")
print("-"*8)
for name, grade in students.items():
    print(name, ":" , grade)
#Search for student
search = input("\n Enter student name to search")
if search in students:
    print(search, "has grade of", students[search])
else:
    print("Student not found.")