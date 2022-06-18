#!/usr/bin/env python
# coding: utf-8

# # Assignment 1

# In[ ]:


1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.

* (Expression)
'hello' (value)
-87.8 (Value)
- (Expression)
((Expression))
+ (Expression)
6 (Value)


# In[ ]:


2. What is the difference between a string and a variable

Variable is some memory location assinged with a value and string is one such value which can be assigned to a variable


# In[ ]:


3. Describe three different data types.
->  Numeric Data Types:
    Integer: These are positive or negative whole numbers Ex: 5
    Float: These are real numbers along with floating point or decimal number representation Ex; 5.8
    Complex: These are used to represent complex numbers like 1+2j (Imaginary + real part)
-> Boolean:
    There are two keywords for boolean (True and False) which are equivalent to 1 or 0 in binary. Like they are used to determine either presence/occurance or absence/non-occurance of an event or value
-> String: 
    A stream of characters(just like a word) are used to represent a string. Ex: "Hello"
-> List:
    This is used to represent a collection of different datatypes. Lists are mutable, like they are editable. Index of list starts
    from 0 and ends at length of list - 1
    Ex: [1,2,3.0,4+5j,"Hello",(1,2,3),{1,2,"hello","there"}]
-> Set: 
    Set is another kind of data type present in python, it is represented using set() keyword. It can not be accessed with indexes
    since set is unordered.
-> Dictionary:
    Dictionary is used to store key value pairs of different data types. 


# In[ ]:


4. What is an expression made up of? What do all expressions do
-> Expression is made up of values and mathematical operators. Expressions evaluate the LHS and assign the result to RHS


# In[ ]:


5. This assignment statements, like spam = 10. What is the difference between an xpression and a statement
-> Expression evaluates the LHS and assigns to LHS. But in assignment there is no evaluation. Direct assignment of value is applicable


# In[ ]:


6. After running the following code, what does the variable bacon contain
bacon = 22
bacon + 1
-> 22 will become 23, so the variable bacon will contain 23


# In[ ]:


7. What should the values of the following two terms be
'spam' + 'spamspam' => 'spamspamspam'
'spam' * 3 => "spamspamspam"


# In[ ]:


8. Why is eggs a valid variable name while 100 is invalid
-> Because variable names can not start with numbers, while they can start with words


# In[ ]:


9. What three functions can be used to get the integer, floating-point number, or string ersion of a value
-> int(), float(), str()


# In[ ]:


10. Why does this expression cause an error? How can you fix it?
'I have eaten' + 99 + ' burritos.'
-> Because strings can not be concatenated with integers. To fix this, we have to wrap 99 in single quotes

