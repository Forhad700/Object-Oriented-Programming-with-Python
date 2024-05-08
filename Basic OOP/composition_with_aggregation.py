class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.appen(employee)

    def average_salary(self):
        if not self.employees:
            return 0
        total_salary = sum(employee.salary for employee in self.employees)
        return total_salary / len(self.employees)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


hr_department = Department("HR")
hr_department.add_employee(Employee("Alice", 50000))
hr_department.add_employee(Employee("Bob", 60000))
 
print(f"Average salary in {hr_department.name} department: ${hr_department.average_salary()}")