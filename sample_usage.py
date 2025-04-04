import json

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

class Employee(Person):
    def __init__(self, name, age, gender, emp_id, department, salary):
        super().__init__(name, age, gender)
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def get_details(self):
        person_details = super().get_details()
        return f"{person_details}, Emp ID: {self.emp_id}, Department: {self.department}, Salary: ₹{self.salary}"

    def is_eligible_for_bonus(self):
        return self.salary < 50000

    @classmethod
    def from_string(cls, data_string):
        name, age, gender, emp_id, department, salary = data_string.split(',')
        return cls(name, int(age), gender, emp_id, department, int(salary))

    @staticmethod
    def bonus_policy():
        print("Bonus Policy: Employees with salary below 50000 are eligible ")

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_average_salary(self):
        if not self.employees:
            return 0
        total_salary = sum(employee.salary for employee in self.employees)
        return total_salary / len(self.employees)

    def get_all_employees(self):
        return self.employees

def save_employees_to_json(departments, filename="employees.json"):
    data = []
    for dept in departments:
        for emp in dept.employees:
            data.append({
                "name": emp.name,
                "age": emp.age,
                "gender": emp.gender,
                "emp_id": emp.emp_id,
                "department": emp.department,
                "salary": emp.salary
            })
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Employee data saved to '{filename}'")

def load_employees_from_json(filename="employees.json"):
    departments = {}
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            for emp_data in data:
                emp = Employee(
                    emp_data["name"], emp_data["age"], emp_data["gender"],
                    emp_data["emp_id"], emp_data["department"], emp_data["salary"]
                )
                if emp.department not in departments:
                    departments[emp.department] = Department(emp.department)
                departments[emp.department].add_employee(emp)
        print(f"Employee data loaded from '{filename}'")
        return list(departments.values())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{filename}'. The file might be empty or corrupted.")
        return []

# -----------------------
# Sample Main Execution
# -----------------------

if __name__ == "__main__":
    # Sample Employee Data
    data_strings = [
        "Alice,30,Female,E101,HR,48000",
        "Bob,28,Male,E102,IT,55000",
        "Charlie,35,Male,E103,HR,60000",
        "Diana,26,Female,E104,IT,47000",
        "Evan,40,Male,E105,Finance,53000"
    ]

    employees = [Employee.from_string(s) for s in data_strings]

    # Create Departments and Assign Employees
    hr_dept = Department("Human Resources")
    it_dept = Department("Information Technology")
    finance_dept = Department("Finance")

    for emp in employees:
        if emp.department == "HR":
            hr_dept.add_employee(emp)
        elif emp.department == "IT":
            it_dept.add_employee(emp)
        elif emp.department == "Finance":
            finance_dept.add_employee(emp)

    all_departments = [hr_dept, it_dept, finance_dept]

    # Print Bonus Policy
    Employee.bonus_policy()

    # Print Employee Details
    print("\n--- Employee Details ---")
    for emp in employees:
        print(emp.get_details())

    # Print Department Average Salaries
    print("\n--- Average Salaries by Department ---")
    for dept in all_departments:
        print(f"{dept.name}: {dept.get_average_salary():.2f}")

    # Save Data to JSON
    save_employees_to_json(all_departments)

    # Load Data from JSON
    loaded_departments = load_employees_from_json()

    # Print Loaded Employee Details
    if loaded_departments:
        print("\n--- Loaded Employee Details ---")
        for dept in loaded_departments:
            print(f"\nDepartment: {dept.name}")
            for emp in dept.get_all_employees():
                print(emp.get_details())