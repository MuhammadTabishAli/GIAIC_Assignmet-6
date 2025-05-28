class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

# Create student objects
s1 = Student("Tabish", 95)
s2 = Student("Ali", 87)

# Display student details
s1.display()
s2.display()