"""
HW 4: Debugging and Lists

Q1 Debugging

Throughout this homework, whenever you encounter an error, we would like you to 
explain in a comment what it was and how you fixed it. You can write all these errors 
at any place in the file.

###
Errors experienced:
1. I received an error saying that the list_2D = #COMPLETE ins invalid syntax. I just added a "#" at the beginning of the variable to comment it out. I got the same error for a couple other lines in the template. I just added a "#" to comment those out.
2. I received an error that said 'builtin_function_or_method' object is not subscriptable. To fix this error, I googled this error and found that this error occurs when there is no parenthesis associated with the method. So I got this error when I had "empty_list.append[new_element]" in the code. To fix this error, I just changed the brackets in the previous code to parenthesis as shown here: "empty_list.append(new_element)". This fixed the error. To call a method in python, parenthesis instead of brackets must be used.
3. I received an error that said that a function "list_odd_integers() is missing 1 required positional argument: 'list'" when I had written "def list_odd_integers(list1)" in the code. So it was expecting me to pass in a list input. To bypass this, I defined the function as not having any input and took out the "list1" from the parenthesis so it was empty. And then I took out the "return" towards the end of the code and replaced it with list_odd_integers() at the end of the code (not indented at all) so that the terminal would automatically call and run this function without any input.
4. I received an error that said that it cannot access local variable 'i' where it is not associated with a value when I wrote "for i in listA and i in listB:" in my code. To fix this error, I just added a for-loop for listB separately so that two separate for-loops would run, one after the other.


Q2 List Slicing and Striding:

Part 1: Create a variable (name it anything you want but make it descriptive!) that 
is assigned to a list with the numbers 0 to 50. You should not have to write each 
number manually.
"""

its_peanutbutter_jelly_time = list(range(0,51))
print(its_peanutbutter_jelly_time)

# Q2 PART 1 CODE HERE 

"""
Part 2: Create a function that takes in a list and squares each element in the list.
"""
def list_squares(list1):
    empty_list = []
    for i in list1:
        new_element = i**2
        empty_list.append(new_element)
    print(empty_list)


# Q2 PART 2 CODE HERE

"""
Part 3: You are given two lists: listA and listB. listA contains the integers 1 through 
10 while listB contains the integers 20 through 30. Return a single, new list containing
only the odd integers of both lists in sorted order.
"""

listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listB = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

def list_odd_integers():
    new_list = []
    for i in listA:
        if i % 2 != 0:
            new_list.append(i)
    for i in listB:
        if i % 2 != 0:
            new_list.append(i)
    print(new_list)

list_odd_integers()


# Q2 PART 3 CODE HERE

"""
Q3 2D Lists
Using nested for-loops, create and print a 5x5 2D list with the odd numbers from 1 to 25.
"""

# Q3 PART 1 CODE HERE
list_2D = list(range(0,25))

# def list_odd_integers_1_to_25():
#     list_odd_integers_1_to_25 = []
#     for i in list_2D:
#         if i % 2 != 0:
#             list_odd_integers_1_to_25.append(i)
#     return list_odd_integers_1_to_25

#Hint: Outer loop will manage row indices, inner loop will manage column indices (or vice 
# versa).
import numpy as np

empty_array = np.empty((5,5))
integers_to_fill_matrix = 1

for i in range(0,5):
    for j in range(0,5):
        #paths = [i,j]
        empty_array[i,j] = integers_to_fill_matrix 
        integers_to_fill_matrix = integers_to_fill_matrix + 1
print(empty_array)

#print()



"""
Now with your completed list_2D, replace all multiples of 3 with '?' character and print
the resulting 2D list.
"""

# Q3 PART 2 CODE HERE
#What conditional can you use to check if numbers are multiples?

"""
Q4 More List Practice

Write a function that takes in a list and returns a copy of that list with duplicate 
values removed.
"""

#def remove_duplicates(a):
    # Q4 CODE HERE

#It may be helpful to create an array to test your function.
#test = [40, 10, 80, 50, 20, 60, 30]

