#!/usr/bin/env python
# coding: utf-8

# In[1]:


#5

n=int(input("Enter the number: "))
print(f"The cube sum of first {n} natural numbers: {(n*(n+1)//2)**2}")


# In[2]:


#3

weight = float(input("Enter weight in kg: "))
height = float(input("Enter the height in meters: "))
print(f"The Body Mass Index (BMI) of the person is {weight/height}")


# In[2]:


#2

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

n = int(input("Enter the number: "))
print(f"The factorial of {n}: {factorial(n)}")


# In[8]:


#1

def fibonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
    

limit = int(input("Enter the range upto which fibonacci sequence is required: "))
for i in range(limit+1):
    print(fibonacci(i), end=" ")


# In[9]:


#4
import math

n = int(input("Enter the number: "))
print(f"Logarithm of {n}: {math.log(n)}")


# In[ ]:




