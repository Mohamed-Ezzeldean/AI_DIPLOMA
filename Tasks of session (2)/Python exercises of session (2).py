#!/usr/bin/env python
# coding: utf-8

# # Task1:

# #  Write a program to enter a number from a user and print its absolute value.

# In[7]:


#usinf function
x=float(input("enter numer: "))
absolute_value = abs(x)
print("the abolute value of " , x , "is" , absolute_value)


# In[9]:


#using if condition 
x = float(input("Enter a number: "))
if x < 0:
    print("The absolute value of", x , "is", -x )
else:
    print("The absolute value of", x , "is", x )


# # Task2:
# 

# # Write a program to enter a year from a user and check if it is a leap year or not.

# In[15]:


year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


# # Task3:

# # Write a program to enter the age of 3 person and print the oldest and the youngest among them.

# In[11]:


#using if condtion
age1 = int(input("enter age of first person: "))
age2 = int(input("enter age of second person: "))
age3 = int(input("enter age of third person: "))

if age1 > age2 and age1 > age3:
    print("first person is the oldest.")
elif age2 > age1 and age2 > age3:
    print("second person is the oldest.")
else:
    print("third person is the oldest.")

if age1 < age2 and age1 < age3:
    print("first person is the youngest.")
elif age2 < age1 and age2 < age3:
    print("second person is the youngest.")
else:
    print("third person is the youngest.")



# In[13]:


#using function
age1 = int(input("enter age of first person: "))
age2 = int(input("enter age of second person: "))
age3 = int(input("enter age of third person: "))
oldest = max(age1,age2,age3)
youngest = min(age1,age2,age3)
print("the youngest is: " , youngest)
print("the oldest is: " , oldest)


# # Task4:
# 

# # What is the name of the library that encrypted the number like the password?

# PyNaCl

# In[ ]:





# In[ ]:




