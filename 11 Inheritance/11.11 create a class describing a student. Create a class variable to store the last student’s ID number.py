class Student():
    studentID = 100000
    
    def __init__(self, name, surname, studyfield):
        self.name = name
        self.surname = surname
        self.studyfield = studyfield
    
    def __str__(self):
        return (self.name).capitalize() + " " + (self.surname).upper() + " (" + (str(self.studentID)) + "), " + self.studyfield

student1 = Student("Ludwig", "van Beethoven","Filozofia, UEK Kraków")
Student.studentID += 1
print(student1)
student2 = Student("Giuseppe", "Verdi","Kulturoznastwo, UEK Kraków")
Student.studentID += 1
print(student2)
student3 = Student("Frédéric", "Chopin","Socjologia, UEK Kraków")
Student.studentID += 1
print(student3)