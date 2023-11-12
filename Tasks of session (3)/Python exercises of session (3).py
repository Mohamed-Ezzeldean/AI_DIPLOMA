#!/usr/bin/env python
# coding: utf-8

# # Q1

# ## Write a Simple Calculator in Python which will perform various Calculator operations such as Addition, Subtraction, Multiplication, Division. Note ---> Using elif.
# 
# Enter your first number: 10
# Enter your second number: 2 
# Enter operation, your options +, -, *, /: / 
# the division for 10 / 2 = 5.0

# # Sol:

# In[4]:


firstNum=int(input('Enter your first number:'))
secondNum=int(input('Enter your second number:'))
operation=input('Enter operation, your option +,-,*,/:')
if operation=='+':
    print(firstNum+secondNum)
elif operation=='-':
      print(firstNum-secondNum)
elif operation=='*':
      print(firstNum*secondNum)
elif operation == '/':
    if secondNum != 0:
        print(firstNum / secondNum)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation.")


# # Q2

# ## Write a Python script that takes input from the user and displays that input back in upper and lower cases.

# # Sol:

# In[6]:


userInput = input("Enter your input: ")

# Convert input to uppercase
uppercase = userInput.upper()

# Convert input to lowercase
lowercase = userInput.lower()

# Display the input in upper and lower cases
print("Input in uppercase:", uppercase)
print("Input in lowercase:", lowercase)


# # Q3

# ## Write a Python program to remove a newline in Python.

# # Sol:

# In[9]:


print('Programming', end = " ")
print('Language')


# # Q4
# 

# # Write a Python program to calculate the length of a string using (Two Ways).
# input = "ILovePython"

# # Sol:
# 

# Str = input("Please enter string:")
# print('No.OfString: ' ,len(Str))

# In[2]:


#second way
Str = input("Please enter string:")
count = 0
for i in Str:
    count +=1
print('No.OfString: ' ,count)


# # Q5
# 

# # Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead ("###Sample String : 'w3resource' Expected Result : 'w3ce' ###Sample String : 'w3' Expected Result : 'w3w3' ###Sample String : ' w' Expected Result : Empty String)

# # sol:

# In[3]:


Str = input("Please enter string:")
if len(Str) < 2:
    print(" ")
elif len(Str) == 2 :
    print(Str[0:2] * 2)
else:
    print(Str[0:2] + Str [-2 :])


# # Q6: Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. (Sample String : 'abc' Expected Result : 'abcing').
# Sol:

# In[5]:


Str = input("Please enter string:")
if len(Str) < 3:
    print(Str)
elif Str.endswith('ing'):
    print(Str.replace('ing' , 'ly'))
else:
    print(Str + 'ing')


# # Q7: Write a Python program that takes a list of words and return the longest word and the length of the longest one (Longest word: Exercises Length of the longest word: 9)
# Sol:
# 

# In[6]:


strList = ["ali", "Ahmed" , "yousef" ,"Shahed"]
maxLen = 0
maxWord= " "
for i in strList:
    if len(i) > maxLen:
        maxLen = len(i)
        maxWord = i
print(maxWord,":",maxLen)


# # Q8:Write a Python program to remove characters that have odd index values in a given string (Sample String:abca Expected Result:ac)
# Sol:
# 

# In[7]:


string=input("Please enter string:")
newString = " " 
for i in range(len(string)):
    if i % 2 == 0:
        newString +=string[i]
print(newString)


# # Q9: Write a Python program to count the occurrences of each word in a given sentence (Sample String:amr and ahmed are frindes but amr is the tallest Expected Result:2)
# Sol:
# 

# In[8]:


sentence = "amr and ahmed are frindes but amr is the tallest"
wordsLst = sentence.split()
lst = []
for word in wordsLst :
    if word not in lst :
        if not wordsLst.count(word) == 1 :
            print("tallestWord ({}) : withCount ({})".format(word,wordsLst.count(word)))
            lst.append(word)
    else :
        pass


# # Q10: Write a Python function to reverse a string if its length is a multiple of 4
# Sol:
# 

# In[9]:


string = input("Please enter string:")
if len(string) % 4 == 0:
    print(string[::-1])
else:
    print("string is not divided by 4")


# # Q11: Write a Python program to print the following numbers up to 2 decimal places.
# numbers = [2.225,5.33654,8.55677884]
# 
# Sol:
# 

# In[10]:


numbers = [2.225,5.33654,8.55677884]
for i in numbers:
    print("{:.2f}".format(i))


# # Q12: Write a Python program to count the number of non-empty substrings of a given string.
# input = "I Love Python"
# 
# Sol:
# 

# In[11]:


name = "I Love Python"
len(name.split())


# # Q13: remove duplicated elements from a list
# lst = [20,20,10,15,15,5]
# 
# Sol:
# 

# In[12]:


lst = [20,20,10,15,15,5]
newlst = []
for i in lst:
    if i not in newlst:
        newlst.append(i)
print(newlst)


# # Q14: Write a Python function that takes a list of numbers and return the Minimum number.
# Sol:
# 

# In[13]:


def find_minimum(numbers):
    return min(numbers)
numbers = [5, 2, 9, 1, 7]
minimum = find_minimum(numbers)
print("Minimum number:", minimum)


# # Q15: Write a Python program to replace the last value of tuples in a list. Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 1000), (40, 50, 1000), (70, 80, 1000)]
# 
# Sol:
# 

# In[15]:


def replace_last_value(tuples_list, new_value):
    result = []
    for tup in tuples_list:
        new_tup = tup[:-1] + (new_value,)
        result.append(new_tup)
    return result
tuples_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_value = 1000
updated_list = replace_last_value(tuples_list, new_value)
print("Updated list:", updated_list)


# # Q16: Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
# tuples = ((1,2,3) , (4,5,6) , (15,3,8,)) ------> Average= 15.666666666666666
# 
# Sol:
# 

# In[16]:


def calculate_average(tuples):
    total_sum = 0
    count = 0
    for tup in tuples:
        for num in tup:
            total_sum += num
            count += 1
    average = total_sum / count
    return average

tuples = ((1,2,3), (4,5,6), (15,3,8))
average = calculate_average(tuples)
print("Average:", average)


# # Q17: Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.
# lst = [0,1,2,3,4,5,6,7,8,9] , value = 4 ,Expected result ---- > [(0, 4), (1, 3)]
# 
# Sol:
# 

# In[17]:


def find_pairs(lst, value):
    pairs = []
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] + lst[j] == value:
                pairs.append((lst[i], lst[j]))
    return pairs

lst = [0,1,2,3,4,5,6,7]
value = 4
result_pairs = find_pairs(lst,value)
print("Pairs:", result_pairs)


# # Q18: Write a ((function)) that capitalizes the first and fourth letters of a name.
# Expected Result : 'python' -----> 'PytHon'
# 
# Sol:
# 

# In[18]:


def capitalize_letters(name):
    if len(name) >= 4:
        capitalized_name = name[0].upper() + name[1:3] + name[3].upper() + name[4:]
        return capitalized_name
    else:
        return name

name = "python"
capitalized_name = capitalize_letters(name)
print("Capitalized Name:", capitalized_name)


# # Q19: Write a ((function)) that given a sentence, return a sentence with the words reversed.
# 'I am home' --> 'home am I'
# 
# Sol:
# 

# In[19]:


def reverse_sentence(sentence):
    words_list = sentence.split()
    reversed_words_list = words_list[::-1]
    reversed_sentence = " ".join(reversed_words_list)
    return reversed_sentence
sentence = "I am home"
reversed_sentence = reverse_sentence(sentence)
print("Reversed Sentence:", reversed_sentence)


# # Q20: Write a function that checks whether a number is in a given range (inclusive of high and low)
# Expected Result : 5 is in the range between 2 and 7
# 
# Sol:
# 

# In[20]:


def check_range(number, low_limit , high_limit):
   if number >= low_limit and number <= high_limit:
       return True 
   else:
       return False 

number_to_check=5 
low_limit=2 
high_limit=7 
is_in_range=check_range(number_to_check , low_limit , high_limit) 
print(f"{number_to_check} is in the range between {low_limit} and {high_limit}: {is_in_range}")


# In[ ]:




