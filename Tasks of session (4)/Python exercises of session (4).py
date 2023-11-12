#!/usr/bin/env python
# coding: utf-8

# # 1. Write a Python program to print the following string in a specific format (see the output).Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
# In[1]:


print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


# # 2. Write a Python program to find out what version of Python you are using.

# In[2]:


import sys
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)


# # 3. Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

# In[3]:


import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))


# # 4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

# In[4]:


from math import pi
r = float(input("Input the radius of the circle : "))
area = pi * r ** 2
print("The area of the circle with radius " + str(r) + " is: " + str(area))


# # 5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

# In[5]:


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print("Hello  " + lname + " " + fname)


# # 6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

# In[6]:


values = input("Input some comma-separated numbers: ")
list = values.split(",")
tuple = tuple(list)
print('List : ', list)
print('Tuple : ', tuple)


# # 7. Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java

# In[7]:


filename = input("Input the Filename: ")
f_extns = filename.split(".")
print("The extension of the file is : " + repr(f_extns[-1]))


# # 8. Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]

# In[10]:


color_list = ["Red", "Green", "White", "Black"]
print(color_list[0], color_list[-1])


# # 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014
# 

# In[13]:


exam_st_date = (11, 12, 2014)
print("The examination will start from : %i / %i / %i" % exam_st_date)


# # 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615
# 
# 

# In[19]:


a = str(input("Input an integer: "))
n1= a
n2= a+a
n3= a+a+a

print(int(n1) + int(n2) + int(n3))


# # 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number:
# 
# 
# 
# Return the absolute value of the argument.
# 

# In[20]:


print(abs.__doc__)


# # 12. Write a Python program that prints the calendar for a given month and year.
# Note : Use 'calendar' module.

# In[23]:


import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))


# # 13. Write a Python program to print the following 'here document'.
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
# In[29]:


# Use triple double-quotes to create a multi-line string
print("""a string that you "don't" have to escape\nThis\nis a  ....... multi-line\nheredoc string --------> exampl """)


# # 14. Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

# In[32]:


from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)


# # 15. Write a Python program to get the volume of a sphere with radius six.

# In[33]:


pi = 3.14
r = 6.0
V = 4.0/3.0 * pi * r**3
print('The volume of the sphere is: ', V)


# # 16. Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference

# In[34]:


def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2
print(difference(22))
print(difference(14))


# # 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
# 

# In[37]:


def near_thousand(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))


# # 18. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
# 

# In[38]:


def sum_thrice(x, y, z):
    sum = x + y + z
    if x == y == z:
        sum = sum * 3
    return sum
print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))


# # 19. Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
# 

# In[39]:


def new_string(text):
    if len(text) >= 2 and text[:2] == "Is":
        return text
    else:
        return "Is" + text
print(new_string("Array"))
print(new_string("IsEmpty"))


# # 20. Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

# In[40]:


def larger_string(text, n):
    result = ""
    for i in range(n):
        result = result + text
    return result
print(larger_string('abc', 2))
print(larger_string('.py', 3))


# In[ ]:




