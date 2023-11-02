#!/usr/bin/env python
# coding: utf-8

# In[57]:


import numpy as np


# In[7]:


# PRACTICE FOR DETERMINING WHAT EACH PART OF THE ARRAY DOCUMENTATION REPRESENTS

a = np.array([1,2,3])
a[:-1]


# In[9]:


# PRACTICE FOR DETERMINING WHAT EACH PART OF THE ARRAY DOCUMENTATION REPRESENTS

a = np.array([[1,2,3], [1,1,1]])
a[0][1]


# In[47]:


### PROBLEM 1 SOLUTION ###

arr = np.array([[1, 1, 1], [1, 2, 3], [2, 2, 2]])
solution = np.all(arr[:,1:] == arr[:,:-1], axis = 1) # this says that every row of the given array that has a column of index 1 and after... And if this is equal to every object in every row in the array with columns of index 1 and before (because the negative sign indicates we are looking at the array back to front), then this means we have an array in which all the values are equal. Axis = 1 means that it is assigning a boolean value based on reading all the values horizontally and comparing column to column ( comparing row to row would mean axis of 0 ). So it will assign a boolean value after analyzing all the values across a given row (column to column). If there is any false values, the ultimate boolean value at the end will be false.  
# the arr == arr part makes a matrix of boolean values and axis assigns a boolean value based on whether it is reading the values vertically or horizontally indicated by axis being 0 or 1... We get "False, False" when axis = 0 because the matrix is read vertically down and there is one false value in the first column and a second false value in the second column.
#print(arr)
#print(arr[:,1:] == arr[:,:-1])
arr[solution]
# How can i get python to output the associated values?


# In[74]:


# PRACTICE FOR DETERMINING WHAT EACH PART OF THE ARRAY DOCUMENTATION REPRESENTS

first_array = arr[1][1]
first_array


# In[15]:


# PRACTICE FOR DETERMINING WHAT EACH PART OF THE ARRAY DOCUMENTATION REPRESENTS

new_array = arr[:,1:] # this is accessing all the rows and each column after (and including) the first index 
new_array


# In[18]:


# PRACTICE FOR DETERMINING WHAT HAPPENS WHEN BRACKETS ARE USED AND WHAT EACH PART OF THE ARRAY DOCUMENTATION REPRESENTS

second_array = arr[:][1:] # this is accessing every element in the array. Then it is accessing every row after (and including) the first index
second_array


# In[25]:


# PRACTICE FOR DETERMINING WHAT HAPPENS WHEN ARRAYS OF DIFFERING SIZES ARE INPUTTED

arg = np.array([[1,2,3,4], [5,6,7], [8,9,0,0]], dtype = object) #creating a list of all the objects since they are of different arrays
third_array = arg[0] # this is accessing the entire array through the brackets. Then it is accessing every row after (and including) the first index. Then it is accessing the column located at index 2. 
print(np.shape(arg)) # treating arg above as a list and counting the objects in the list as elements
print(third_array) # accessing the 0th element of the array (in this case a list)


# In[36]:


# PRACTICE FOR DETERMINING WHAT HAPPENS WHEN ARRAYS OF DIFFERING SIZES ARE INPUTTED

second_array = arr[:][1:,2] # this accesses every row in the array. Then it indexes and accesses every object in the array that has a row of index 1 and after with a column of index 2.
second_array


# In[42]:


# PRACTICE FOR DETERMINING WHAT HAPPENS WHEN ARRAYS OF DIFFERING SIZES ARE INPUTTED

another_array = arr[:,1][0] # verdict. Everything inside the bracket is in row, column documentation. Meaning that even if I have [:], this means I am accessing every row of that matrix. But if I want to access every object in every row of that array that has a column of index 1, I would do [:,1]. And if I want to just access the 0th indexed object in that array, I would type [0] after.
another_array


# In[44]:


# PRACTICE FOR DETERMINING WHAT HAPPENS WHEN ARRAYS OF DIFFERING SIZES ARE INPUTTED

practice = arr[,:] # need to index by rows and columns. Row leads the way.
practice


# In[ ]:


# verdict. Everything inside the bracket is in row, column documentation. Meaning that even if I have [:], this means I am accessing every row of that matrix. But if I want to access every object in every row of that array that has a column of index 1, I would do [:,1]. And if I want to just access the 0th indexed object in that array, I would type [0] after.


# In[48]:


# PRACTICE FOR DETERMINING WHAT HAPPENS WHEN ARRAYS OF DIFFERING SIZES ARE INPUTTED

practice = arr[:,1] # this is accessing every row and column of index 1. 
practice


# In[5]:


### PROBLEM 2 SOLUTION ###

x = np.zeros((8,8),dtype=int) # this creates an 8x8 numpy array filled with zeros.
x[1::2,::2] = 1 # Assigns the value 1 to every other element in every other row (starts at row with index 1 and goes to every row after that with a step size of 2), starting from the second row (index 1). The remaining rows are filled with zeros. 
x[::2,1::2] = 1 # Assigns the value 1 to every other element in every other column, starting from the second column (index 1). This is written opposite of first line to fill in the gaps and address the lines not accounted for by the first line. This fills remaining spots with 1 to complete checkerboard pattern.
print(x)

#question and answer... what do the items inside the brackets really represent if not rows and columns? It represents [row, column] and within the bracket it is [start:stop:end, start:stop:end]


# In[39]:


# PRACTICE FOR UNDERSTANDING PROBLEM 2

x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1
x


# In[27]:


# PRACTICE FOR UNDERSTANDING HOW TO ADD TWO LISTS TOGETHER WITH FOR-LOOPS AND NOT USE NUMPY

#Question is how can i add two lists together without numpy and using for-loops
test_list1 = [1, 3, 4, 6, 8]
test_list2 = [4, 5, 6, 2, 10]
res_list = []
for i in range(0, len(test_list1)): # why can't i iterate through test_list1 by not putting range and len?... because i would be accessing ith element and trying to index through the second list using the value stored in that ith element of the first list. So once the loop gets to 6 in the first list, it would try to find the 6th index of the second list. 
    res_list.append(test_list1[i] + test_list2[i])
print ("Resultant list is :" + str(res_list))


# In[71]:


### PROBLEM 3 SOLUTION ###

myarr = np.array(["python","is","cool!"], dtype = str) # np.str is an old alias and is now delimited as str. Creates an array of strings 
r = np.char.join(" ", myarr) # this function allows for a space to be added in between each character in the myarr array. The documentation is np.char.join(separator,string) and the separator we want in this case is a space. The string in this case is the array of strings denoted by dtype strings.
print(r)


# In[69]:


# TEST TO SEE THAT CERTAIN DTYPE DOCUMENTATION HAS CHANGED

np.str


# In[99]:


### PROBLEM 4 SOLUTION ###

np.random.seed(12345) # initializes the random function? sets the seed for generating random values. but what does 12345 represent?
a = np.random.randint(1,50,(4,5)) #Return random integers from low (inclusive) to high (exclusive) of size (provided in form of integer or tuple-in this case tuple bc we want a 4x5 matrix)
np.sort(a[::], axis = 0) #np.sort returns a sorted array copy... the documentation for np.sort is "numpy.sort(a, axis=-1, kind=None, order=None)". We want np.sort to sort through the a object/array (in its entirety) and sort vertically (meaning sorting based on comparing row value to next row value) which means we need to set the axis to 0.


# In[ ]:





# In[89]:





# In[ ]:




