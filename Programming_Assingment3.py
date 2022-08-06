#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
num = int(input("Enter a number: "))
if num>0:
    print("Number is Positive")
elif num<0:
    print("Number is Negative")
else:
    print("Number is Zero")


# In[4]:


#2
num = int(input("Enter a number: "))
if num%2:
    print("Number is odd")
else:
    print("Number is even")


# In[8]:


#3
year = int(input("Enter the year: "))
if year%400==0:
    print("Leap year")
elif year%100==0:
    print("Not a leap year")
elif year%4==0:
    print("Leap year")
else:
    print("Not a leap year")
    


# In[18]:


#4
import math   
num = int(input("Enter the number: "))

for i in range(2, int(math.sqrt(num))+1):
    if num%i==0:
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")


# In[30]:


#5
#Sieve of Eratosthenes
import math
number = int(input("Enter the upper limit: "))
prime=[True]*(number+1)

for i in range(2, int(math.sqrt(number))+1):
    if prime[i]:
        for j in range(i*i, number, i):
            prime[j]=False
print([i for i in range(len(prime)) if prime[i]])


# In[ ]:




