#!/usr/bin/env python
# coding: utf-8

# 1. Why are functions advantageous to have in your programs?
# 
#         Functions reduces writing duplicate coding.makes programs shorter, easier to read, and easier to update
#         
# 2. When does the code in a function run: when it's specified or when it's called?
# 
#        Code in a function runs when the specified function is called 
#        
# 3. What statement creates a function?
#         
#        The def statement defines (i.e. creates) a function.     
# 

# 4. What is the difference between a function and a function call?
# 
#         A function consists of the def statement and return statement, and code
#         A function call is what moves the program execution into the function, and the function call evaluates to the 
#          function's return value.
# 

# In[1]:


# defining a Function
def sum(a=0,b=0):
    return a+b


# In[2]:


# calling a function
sum(2,3)  


# In[3]:


# calling a function
sum(2)


# 5. How many global scopes are there in a Python program? How many local scopes?
# 
#         There's only one global Python scope per program execution. 
#         This scope remains in existence until the program terminates and all its names are forgotten. Otherwise, the next 
#         time you were to run the program, the names would remember their values from the previous run
#         
#         local scope is created whenever a function is called.
#         only available or visible to the code within the scope.
# 
# 6. What happens to variables in a local scope when the function call returns?
# 
#         When a function returns the output, the local scope is removed.
# 
# 7. What is the concept of a return value? Is it possible to have a return value in an expression?
# 
#         A return value is the value that a function calls and  evaluates to give output. Like any value, a return value can 
#         be used as part of an expression.
#         
# 8. If a function does not have a return statement, what is the return value of a call to that function?
# 
#         If the funtion does not have a return statement it will not return anything.
#         
# 9. How do you make a function variable refer to the global variable?
# 
#         To make function variable as a global variable you can use the global keyword to declare which variables are 
#         global.
#         
# 10. What is the data type of None?
# 
#          The data type of None is NoneType.
#          
# 11. What does the sentence import areallyourpetsnamederic do?
# 
#         import statement imports a module named areallyourpetsnamederic. 
#         (But a module of this name doesnt exists in Python)

# In[4]:


import areallyourpetsnamederic


# 12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
# 
# 
#         import spam
#         spam.bacon()

# 13. What can you do to save a programme from crashing if it encounters an error?
# 
#         try except block can be used  to save a program from crashing.
# 
# 14. What is the purpose of the try clause? What is the purpose of the except clause?
# 
#          Try and Except clause is used to handle the errors within our code . 
#          The try block is used to check some code for errors i.e the code inside.
#          the try block will execute when there is no error in the program. 
#          Whereas the code inside the except block will execute whenever the program encounters some error in the try block.

# In[10]:


a=b+2


# In[9]:


# with try and except
try:
    a=b+2
except NameError:
    print('NameError')


# In[ ]:




