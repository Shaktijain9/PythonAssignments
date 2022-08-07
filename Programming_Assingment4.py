#!/usr/bin/env python
# coding: utf-8

# In[2]:


#6

n = int(input("Enter the number upto which sum is required: "))
print(f"Sum of n natural numbers : {n*(n+1)//2}")


# In[4]:


#2

n = int(input("Enter the number for which multiplication table is required: "))
for i in range(1, 11):
    print(f"{n}X{i}={n*i}")


# In[5]:


#1

n = int(input("Enter the number: "))
result=n
for i in range(n-1, 0, -1):
    result*=i
print(f"Factorial of {n} is : {result}")


# In[7]:


#3

n = int(input("Enter the number: "))
l=[]
a, b = 0, 1
for i in range(n):
    b=a+b
    a, b=b, a
    l.append(b)
print("Fibonacci Sequence upto nth place: ", l)    


# In[9]:


#4
n = int(input("Enter the number: "))
num=n
result=0
while(n>0):
    rem=n%10
    result+=rem**3
    n//=10
if num==result:
    print(f"{num} is a Armstrong number")
else:
    print(f"{num} is not a Armstrong number")


# In[11]:


#6

lower, upper = list(map(int, input("Enter the range: ").split()))
for i in range(lower, upper+1):
    n=i
    result=0
    while(n>0):
        rem=n%10
        result+=rem**3
        n//=10
    if i==result:
        print(f"{i} is a Armstrong number")


# In[ ]:




