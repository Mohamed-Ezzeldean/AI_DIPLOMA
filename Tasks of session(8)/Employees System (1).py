#!/usr/bin/env python
# coding: utf-8

# In[12]:


from os import sys
class EmployeesSystem : 
    employeelist = []
    def _init_(self,name,age,salary,employeelist):
        self.name=name
        self.age=age
        self.salary=salary
        self.employeelist = list (employeelist)



    def AddNewEmployee (self):
        self.employeelist.append(employee1) 

        
    def PrintAllEmployees(self):
        if len (self.employeelist)==0:
            print ("No Employees At The Moment!")
        for emp in self.employeelist :
            print (emp.name , "has age" , emp.age ,"and salary" , emp.salary)
            

    def DeleteByAge(self):
        
        x=int(input("enter age from"))
        y=int(input("enter age to"))
        for employee1 in self.employeelist:
           if int(employee1.age) in range(x,y+1) :
            
             self.employeelist.remove (employee1)

            
    def UpdateSalaryByName(self):
        na = input ("enter the name of the employee")
        sa = int(input("the old salary of the employee to change it"))
        for employee in self.employeelist :
            if employee.name == na:
                if int( employee.salary) != sa :
                    print ("the employee does not have this salary check again")
                else :
                    employee.salary = int(input("enter the new salary"))


class employee:
    name = None
    age = None
    salary = None
   
    def init (self , name="" , age="", salary="" ) :
        self.name = name
        self.age = age
        self.salary = salary
while 5 :
  option = 0
  option = int(input ('''program options:
        1)Add new employee
        2)print all employees
        3)Delete by age
        4)Update salary by name
        5)End the program
        ''')) 
  

  
  while (True):
     if option >0 and option <6 :
         break
     else :
        option = input ("Invalid range. Try again!\nEnter your choice(from 1 to 5):")
  
  

  if option ==1:
   employee1 = employee()
   employee1.name = input("Enter employee data:\nEnter your name:")
   employee1.age = input("Enter the age:")
   employee1.salary = input("Enter the salary:")
  if (option == 1):
   EmployeesSystem.AddNewEmployee (EmployeesSystem)
   
   
   
  if (option == 2):
    EmployeesSystem.PrintAllEmployees(EmployeesSystem)
  if (option == 3):
    EmployeesSystem.DeleteByAge(EmployeesSystem)
  if (option == 4):
    EmployeesSystem.UpdateSalaryByName (EmployeesSystem)


  if (option == 5):
      break
      sys.exit(0)
             


# In[ ]:





# In[ ]:




