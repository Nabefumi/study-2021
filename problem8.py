'''
- Imagine, each student is represented by the following properties:
o firstName
o lastName
o address
o Year of birth
o gpa
Write a function which receives a list of students as its input parameter and return the
student who has the highest average.
- Hint: Use a dictionary (the properties are the keys and the values are the values of the properties, for
instance, “FirstName”:”Ali”). And the define a list of dictionaries and each dictionary represents a student
'''

def findStudentWithHighestGPA(students):
    
    highestGPA = "0"
    studentWithHighestGPA = None
    
    for student in students:
        if student["gpa"] >= highestGPA:
            highestGPA = student["gpa"]
            studentWithHighestGPA = student
            
    return studentWithHighestGPA
    
def main():
    listOfStudents = []
    student1 = {"firstName":"Peter", "lastName":"Brown", "address":"Vancouver", "Yearofbirth":"2000", "gpa":"78"}
    listOfStudents.append(student1)
    
    student2 = {"firstName":"Sarah", "lastName":"Jones", "address":"Burnaby", "Yearofbirth":"1999", "gpa":"80"}
    listOfStudents.append(student2)
    
    student3 = {"firstName":"Philipe", "lastName":"Jackson", "address":"Vancouver", "Yearofbirth":"1998", "gpa":"81"}
    listOfStudents.append(student3)
    
    student4 = {"firstName":"Mary", "lastName":"Moh", "address":"Surrey", "Yearofbirth":"2000", "gpa":"70"}
    listOfStudents.append(student4)
    
    student = findStudentWithHighestGPA(listOfStudents)
    print(student)
    
main()
    
    
    
    
    
    
    
    
    