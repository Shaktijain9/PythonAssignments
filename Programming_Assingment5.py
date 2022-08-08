#!/usr/bin/env python
# coding: utf-8

# In[9]:


#3

num = int(input("Enter the decimal value: "))
print(f"Binary value for {num}: {bin(num)}")
print(f"Octal value for {num}: {oct(num)}")
print(f"HexaDecimal value for {num}: {hex(num)}")


# In[10]:


#4

ch = input("Enter the character: ")
print(f"ASCII value of {ch} is {ord(ch)}")


# In[1]:


#5

a, b =list(map(int, input("Enter two numbers : ").split()))
option = int(input("Select 1 for addition , 2 for substraction , 3 for multiply and 4 for division"))
if option==1:
    print(f"Result: {a+b}")
elif option==2:
    print(f"Result: {a-b}")
elif option==3:
    print(f"Result: {a*b}")
elif option==4:
    print(f"Result: {a/b}")
else:
    print("Invalid Choice")


# In[9]:


#2

num1, num2 =list(map(int, input("Enter two numbers : ").split()))
a=num1
b=num2
while b:
    a, b=b, a%b
print(f"HCF of {num1} & {num2} : {a}")


# In[14]:


#1

a, b =list(map(int, input("Enter two numbers : ").split()))
num = a if a>b else b
for i in range(num, a*b+1, num):
    if i%a==0 and i%b==0:
        print(f"LCM of {a} and {b} : {i}")
        break
    


# In[ ]:




