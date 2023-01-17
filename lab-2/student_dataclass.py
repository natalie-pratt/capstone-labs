from dataclasses import dataclass

@dataclass # This class is specifically for holding data and its types. I've overwritten the string function, but it requires no 'self'.
class Student:
    name: str
    school_id: str
    gpa: float

    def __str__(self): # To string method to neatly print information on a given student object
        return f'Student Name: {self.name}, ID: {self.school_id}, GPA: {self.gpa}'

def main():
    # Create student objects
    natalie = Student('Natalie', '12345', 4.0)
    angie = Student('Angie', '126543', 4.0)
    cole = Student('Cole', '987654', 3.8)
    james = Student('James', '876543', 3.9)

    # Create list and append student objects for printing
    students = []
    students.append(natalie)
    students.append(angie)
    students.append(cole)
    students.append(james)

    for student in students:
        print(student)

    # Verify you can access all different kinds of data within a Student object
    print(natalie.name)
    print(angie.school_id)
    print(cole.gpa)

# Call main function if __name__ is __main__
if __name__ == '__main__':
    main()