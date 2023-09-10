"""Write a python program by creating a class called Employee to store the details of 
Name, Employee_ID, Department and Salary, and implement a method to update 
salary of employees belonging to a given department."""


class Employee:
    def __init__(self):
        self.name = ""
        self.empId = ""
        self.dept = ""
        self.salary = 0
        
    def getEmpDetails(self):
        self.name = input("Enter Employee name: ")
        self.empId = input("Enter Employee ID: ")
        self.dept = input("Enter Employee Dept: ")
        self.salary = input("Enter Employee Salary: ")
        
    def showEmpDetails(self):
        print("Employee Details ")
        print("Name: ",self.name)
        print("ID: ",self.empId)
        print("Dept: ",self.dept)
        print("Salary: ",self.salary)
        
    def updtSalary(self):
        self.salary = int(input("Enter new Salary: "))
        print("Updated salary", self.salary)
        
        
e1 = Employee()
e1.getEmpDetails()
e1.showEmpDetails()
e1.updtSalary()

"""

Output:
Enter Employee name: abhi
Enter Employee ID: 1jss12
Enter Employee Dept: cs
Enter Employee Salary: 20000000
Employee Details
Name:  abhi
ID:  1jss12
Dept:  cs
Salary:  20000000
Enter new Salary: 80000000
Updated salary 80000000

"""