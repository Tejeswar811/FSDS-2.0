#!/usr/bin/env python
# coding: utf-8

# 1. What are the two values of the Boolean data type? How do you write them?
# 
#          True and False , which are special versions of 1 and 0

# 2. What are the three different types of Boolean operators?
# 
#         AND, OR, and NOT.

# 3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
# 
#         OR Operator:
# 
#         INPUT (A)	INPUT (B)	 OUTPUT(Y= A OR B)
# 
#         FALSE ( 0 )	FALSE ( 0 )	 FALSE ( 0 )
#         TRUE  ( 1 )	FALSE ( 0 )	 TRUE  ( 1 )
#         FALSE ( 0 )	TRUE  ( 1 )	 TRUE  ( 1 )
#         TRUE  ( 1 )	TRUE  ( 1 )	 TRUE  ( 1 )
# 
#         AND OPERATOR:
# 
#         INPUT (A)	INPUT (B)	 OUTPUT(Y=A AND B)
# 
#         FALSE ( 0 )	FALSE ( 0 )	  FALSE ( 0 )
#         TRUE  ( 1 )	FALSE ( 0 )	  FALSE ( 0 )
#         FALSE ( 0 )	TRUE  ( 1 )	  FALSE ( 0 )
#         TRUE  ( 1 )	TRUE  ( 1 )	  TRUE  ( 1 )
# 
#         NOT OPERATOR:
# 
#         INPUT (X)	 OUTPUT (Y=NOT(A))
#         TRUE  ( 1 )	  FALSE ( 0 )
#         FALSE ( 0 )	  TRUE  ( 1 )
# 
# 

# 4. What are the values of the following expressions?
#     (5 > 4) and (3 == 5)
#     not (5 > 4)
#     (5 > 4) or (3 == 5)
#     not ((5 > 4) or (3 == 5))
#     (True and True) and (True == False)
#     (not False) or (not True)

# In[22]:


(5 > 4) and (3 == 5)


# In[23]:


not (5 > 4)


# In[24]:


(5 > 4) or (3 == 5)


# In[25]:


not ((5 > 4) or (3 == 5))


# In[26]:


(True and True) and (True == False)


# In[27]:


(not False) or (not True)


# 5. What are the six comparison operators?  
# 
#         •	Less than ( < )
#         •	Less than or equal to (<=)
#         •	Greater than (>)
#         •	Greater than or equal to (>=)
#         •	Equal to ( == )
#         •	Not equal to ( != )

# 6. How do you tell the difference between the equal to and assignment operators? Describe a condition and when you would use one.
# 
#         =	is an Assignment Operator it is used to assign the value of variable or expression
#         ==	is an Equal to Operator and it is a relation operator used for comparison

# In[8]:


# Assignment operator
a=2
print(a)


# In[9]:


# Equal to operator
a=2
b=2
print(a==b)


# 7. Identify the three blocks in this code:
#         spam = 0
#         if spam == 10:
#         print('eggs')
#         if spam > 5:
#         print('bacon')
#         else:
#         print('ham')
#         print('spam')
#         print('spam')

# In[11]:


spam = 0
if spam == 10:
    print('eggs') #Block 1
if spam > 5:
    print('bacon') #Block 2
else:
    print('ham') #Block 3
    print('spam')
    print('spam')


# 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

# In[12]:


spam = int(input("Input a no."))
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")


# 9. If your programme is stuck in an endless loop, what keys you’ll press?
#        
#        CTRL+C	is used to kill a process. It terminates your program
# 

# 10. How can you tell the difference between break and continue?
#     
#         The break statement used to terminate the loop immediately when it is encountered.
#         The continue statement used to skip the current iteration of the loop and the control flow of the program goes to             the next iteration.

# In[14]:


# use of break
for i in range(5):
    if(i==3):
        break
    print(i)    
print('Break statement is exicuted, so it terminated the loop')


# In[17]:


#use of  continue
for i in range(5):
    if(i==3):
        print('skip 3rd  iteration of the loop and the control flow of the program goes to the next iteration.')
        continue
    print(i)


# 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# 
#         Syntax: range (start, stop, step)
#         Parameter:
#             •	start: optional, start value of the sequence
#             •	stop: next value after the end value of the sequence
#             •	step: optional, integer value, denoting the difference between any two numbers in the sequence.
# 
#     range(10)	Stop=10, start=not provided default is 0, step=not provided, default is 1
#     range(0, 10)	Stop=10, start= 0, step=not provided, default is 1
#     range(0, 10, 1)	Stop=10, start=0, step= 1
# 

# 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# In[18]:


#Use of For Loop
print("For Loop")
for i in range(1,11):
    print(i)


# In[19]:


#Use of While Loop
print("While Loop")
a =1
while a <= 10:
    print(a)
    a+=1


# 13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
# 
#         This function can be called with spam. bacon()
