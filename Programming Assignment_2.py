#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1

kilometers = float(input("Enter the kilometers: "))
print("Miles: ", kilometers * 0.6213)


# In[3]:


#2

celsius = float(input("Enter the temperature in celsius: "))
print(celsius*1.8 + 32)


# In[5]:


#3
import calendar

yy = int(input("Enter the year: "))
mm = int(input("Enter the month: "))
         
print(calendar.month(yy, mm))         


# In[7]:


#4
import math

a = int(input("Enter the coefficient of x^2: "))
b = int(input("Enter the coefficient of x: "))
c = int(input("Enter the constant term: "))

print(f"Quadratic equation looks like: {a}x^2+{b}x+{c}")
determinant = math.sqrt(b**2-4*a*c)
r1 = (-b + determinant)/2*a
r2 = (-b - determinant)/2*a

print(f"Root of the equation are : {r1} & {r2}")


# In[8]:


#5
a, b = list(map(int, input("Enter value of a and vlue of b: ").split()))

a, b = b, a
print(f"Value of a = {a} & b={b}")


# In[ ]:




