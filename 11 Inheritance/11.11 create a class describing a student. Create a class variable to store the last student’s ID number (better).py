class Student():
    university = "UEK Kraków"
    studentID = 100000
    
    def __init__(self, name, surname, studyfield):
        self.name = name
        self.surname = surname
        self.studyfield = studyfield
        Student.studentID += 1
    
    def __str__(self):
        return (self.name).capitalize() + " " + (self.surname).upper() + " (" + (str(self.studentID)) + "), " + self.studyfield + " " + Student.university

student1 = Student("Ludwig", "van Beethoven","Filozofia")
print(student1)
student2 = Student("Giuseppe", "Verdi","Kulturoznastwo")
print(student2)
student3 = Student("Frédéric", "Chopin","Socjologia")
print(student3)