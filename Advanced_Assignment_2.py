#!/usr/bin/env python
# coding: utf-8

# ### What is the relationship between classes and modules?
* Classes are used to create a blueprint for given objects while modules are used to reuse the code inside another program to encourage readbility and reduce code redundancy. Modules are generally .py files which may contains classes, methods or functions.
* Classes can be instantiates but modules can't be instantiated.
* Classes are defined using class keyword while modules are imported using import keyword.
* We can override the existing functionality of claases using inheritence while the functionality defined in modules can't be override.
# ### How do you make instances and classes?
A class is defines using class keyword followed by class name. A class created local namespace where all its attributes are defined. Attributes may be data or functions. As soon as we define a class a new object is created with same name as classname & is used for attributes references & instantiation of objects for the class.

As soon as we define class with help of class keyword followed by class name , it created a local namespace of its own which contains attributes and methods associated with the class, at the same time it created a class object with same name as the class. This class object has access to different attributes and is used to create class objects.
Class instance is used for two purposes.
1. Attribute references.
2. Instantiation
# ### What does the term "self" in a Python class mean?
* self in python points to the current object. We can access the attributes & methods of the current object using self. Python does not support implicit conversion that is methods in python are defined in such a way that the object can be passed automatically but can't be received. So the first parameter in class methods which deal with the instance attributes generally has self.


* the self name is just a convention to improve readibility of the code. We can use any name inplace of self because its not a keyword.
# ### What are the two most important concepts to grasp in order to comprehend Python OOP code?
1. Inheritance
2. Polymorphism

These are two main ingredient two make robust, flexible & easy-to-maintain softwares.
# ### When do you consider allowing operator overloading of your classes?
When you have to extend the meaning of existing operator as per your requirements, then you can consider operator overloading.

EXAMPLE: 2+3 (where + operator works on two operands two provide the result)

same "+" operator can be used to operate on two user-defined class objects.
# ### Where and how should be class attributes created?
class attributes are generally created at the top, just below the class headers.These attributes are shared among all the instances of the class.Hence we can access class attributes using class name as well as instance name.
# In[16]:


class Voter:
    age=18
    
    def __init__(self, name):
        self.name = name
        
obj = Voter("Shakti")
print(obj.name)
print(Voter.age)
print(obj.age)
    


# In[17]:


#class with attribute defines in the bottom

class Voter:

    
    def __init__(self, name):
        self.name = name
        
    age=18
    
    def getInfo(self):
        print(f"{self.name} is of age {Voter.age}")
        
        
obj = Voter("Shakti")
print(obj.name)
print(Voter.age)
print(obj.age)
obj.getInfo()


# ### Where and how are instance attributes created?
# 
Instance attributes are created inside the __init__(). They are uniquue to each instance of the class. These are the variables which belong to one & only one object. The can only be accessed by the instance of the class since they're only accessible in the scope of that object.
# In[18]:


class Sample:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = Sample('Shakti', 24)
print(obj.name)
print(obj.age)


# ### What is the most popular form of operator overloading?

# In[19]:


#The most popular form of operator overloading is the overloading of addition operator.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def __add__(self, other):
        return f"Total Salary = {self.salary + other.salary}"
    
emp1 = Employee("Shakti", 80)
emp2 = Employee("Piyush", 82)

print(emp1+emp2)
print(emp1.__add__(emp2))


# ### How does a Python class handle operator overloading?
Python operators works with built-in types. But the same operator works differently with different types. The operator functionalities are defined using special methods called double underscore methods(dunder methods). In order to change the existing behavior of operators we overload these special methods to accept different objects instead of built-in types.
# In[20]:


print(2+3)
print(int.__add__(2, 3))


# In[ ]:




