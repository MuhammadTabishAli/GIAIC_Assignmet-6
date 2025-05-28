class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    
    def get_info(self):
        return f"Employee {self.emp_id}: {self.name}"

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def list_employees(self):
        print(f"Employees in {self.dept_name}:")
        for emp in self.employees:
            print(f"- {emp.get_info()}")

emp1 = Employee("Tabish", 1001)
emp2 = Employee("Ali", 1002)

# Create Department
dept = Department("Engineering")

# Add employees to department (aggregation)
dept.add_employee(emp1)
dept.add_employee(emp2)

# List department employees
dept.list_employees()