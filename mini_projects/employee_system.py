# Parent Class
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


# Child Class 1
class Developer(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


# Child Class 2
class Manager(Employee):
    def __init__(self, name, base_salary, allowance):
        super().__init__(name, base_salary)
        self.allowance = allowance

    def calculate_salary(self):
        return self.base_salary + self.allowance


# ---- Simulation ----

dev = Developer("Sumukh", 50000, 10000)
mgr = Manager("Yadh", 70000, 20000)

print(f"Developer Salary: {dev.calculate_salary()}")
print(f"Manager Salary: {mgr.calculate_salary()}")
