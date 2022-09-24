class Student:

    def __init__(self, name, age, roll_no, grade):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.grade = grade

    def accept(self, Name, Age, Roll_num, Rank):
        Name = input("Enter the Name")
        Age = int(input("Enter the age"))
        Roll_num = input("Roll_no")
        Rank = input("Enter the Grade")


obj = Student(Name, Age, Roll_num, Rank)
list.append(obj)
