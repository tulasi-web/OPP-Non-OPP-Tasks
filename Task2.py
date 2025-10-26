"""Task is 
Write a class student with attributes name,roll_no,marks.Add a method to calculate grade.Create a subclass GraduateStudent with addition research_topic attribute"""



class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def Calculate_grade(self):
        print("Name:", self.name)
        print("Roll Number is:", self.roll_no)
        print("Marks:", self.marks)
        if self.marks is not None:
            if self.marks >= 90:
                grade = "A+"
            elif self.marks >= 75:
                grade = "A"
            elif self.marks >= 60:
                grade = "B"
            elif self.marks >= 50:
                grade = "C"
            elif self.marks >= 35:
                grade = "D"
            else:
                grade = "F (Fail)"
            print("Grade:", grade)
        else:
            print("Grade: Not available (marks not provided)")
class Graduate_Student(Student):
    def __init__(self, name=None, roll_no=None, marks=None, research_topic=None):
        super().__init__(name, roll_no, marks)
        self.research_topic = research_topic

        if self.research_topic:
            self.Calculate_grade()
        else:
            super().Calculate_grade()

    def Calculate_grade(self):
        super().Calculate_grade()
        print("Research Topic is:", self.research_topic)
        
s2 = Graduate_Student("Mary", 21, 85)  

"""Output is 
Name: Mary
Roll Number is: 21
Marks: 85
Grade: A
"""